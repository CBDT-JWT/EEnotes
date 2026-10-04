#!/usr/bin/env python3
"""Export built, public nav pages and install the shared chatJWT companion.

Run after MkDocs/Zensical build. Uses only Python's standard library. The
deployment workflow also runs this against the checked-in static site.
"""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_URL = 'https://www.weitao-jiang.cn/static/js/chatjwt.js?v=6'
ORIGIN = 'https://note.weitao-jiang.cn'


class ArticleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_article = False
        self.skip = 0
        self.in_title = False
        self.parts = []
        self.title = []

    def handle_starttag(self, tag, attrs):
        if dict(attrs).get('id') == '__comments':
            self.in_article = False
        if tag == 'article':
            self.in_article = True
        if tag in ('script', 'style', 'svg'):
            self.skip += 1
        if self.in_article and tag == 'h1':
            self.in_title = True
        if self.in_article and tag in ('p', 'li', 'h1', 'h2', 'h3', 'h4', 'tr', 'pre', 'br'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag == 'article':
            self.in_article = False
        if tag in ('script', 'style', 'svg'):
            self.skip = max(0, self.skip - 1)
        if tag == 'h1':
            self.in_title = False

    def handle_data(self, value):
        if self.in_article and not self.skip:
            value = value.replace('¶', '').strip()
            if value:
                self.parts.append(value + ' ')
                if self.in_title:
                    self.title.append(value)


def build(site_dir, inject=True, extra_output=None):
    config = (ROOT / 'mkdocs.yml').read_text(encoding='utf-8')
    nav = re.search(r'(?ms)^nav:\s*\n(.*?)(?=^\S|\Z)', config)
    if not nav:
        raise ValueError('Cannot find the public nav in mkdocs.yml')
    # Preserve the course hierarchy: many chapters share “课程说明” or “前言”.
    paths, sections, ancestors = [], {}, []
    for line in nav.group(1).splitlines():
        entry = re.match(r'^( *)(?:-)\s*([\'"])(.*?)\2:\s*(.*?)\s*$', line)
        if not entry:
            continue
        indent, label, value = len(entry[1]), entry[3], entry[4]
        ancestors = [(depth, name) for depth, name in ancestors if depth < indent]
        if not value:
            ancestors.append((indent, label))
        elif re.fullmatch(r'([\'"])([^\'"]+\.md)\1', value):
            path = value[1:-1]
            if path not in sections:
                paths.append(path)
                sections[path] = ' / '.join(name for _, name in ancestors)
    records = []
    missing = []
    for path in paths:
        relative = Path(path)
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('Invalid public page path')
        page_path = relative.with_suffix('') / 'index.html' if relative.name != 'index.md' else relative.with_suffix('.html')
        built_page = site_dir / page_path
        if not built_page.is_file():
            missing.append(str(page_path))
            continue
        html = built_page.read_text(encoding='utf-8')
        parser = ArticleText()
        parser.feed(html)
        content = re.sub(r'\n\s*\n+', '\n', ''.join(parser.parts)).strip()
        if not content:
            raise ValueError(f'No article body in {page_path}')
        public_path = str(page_path).removesuffix('index.html')
        url = ORIGIN + '/' + quote(public_path, safe='/')
        records.append({'title': ' '.join(parser.title) or relative.stem,
                        'section': sections[path],
                        'url': url, 'content': content[:60000]})
    if missing:
        raise ValueError('Build the site first. Missing public pages: ' + ', '.join(missing[:8]))
    if not records:
        raise ValueError('No public pages were exported')
    payload = json.dumps({'version': 1, 'origin': ORIGIN, 'docs': records}, ensure_ascii=False, separators=(',', ':'))
    if len(payload.encode()) > 8 * 1024 * 1024:
        raise ValueError('Public index exceeds the chatJWT 8 MB import limit')
    (site_dir / 'chatjwt-index.json').write_text(payload, encoding='utf-8')
    if extra_output:
        extra_output.parent.mkdir(parents=True, exist_ok=True)
        extra_output.write_text(payload, encoding='utf-8')
    changed = 0
    if inject:
        for page in site_dir.rglob('*.html'):
            html = page.read_text(encoding='utf-8')
            # Remove the previous independent assistant so there is one launcher.
            updated = re.sub(r'<script\b[^>]*src=[\'"][^\'"]*(?:ai-chat(?:-config)?|chatjwt)\.js[^\'"]*[\'"][^>]*>\s*</script>\s*', '', html)
            updated = re.sub(r'<link\b[^>]*href=[\'"][^\'"]*ai-chat\.css[^\'"]*[\'"][^>]*>', '', updated)
            tag = f'<script src="{SCRIPT_URL}" defer></script>'
            updated = updated.replace('</body>', tag + '\n</body>')
            if updated != html:
                page.write_text(updated, encoding='utf-8')
                changed += 1
    print(f'chatJWT: exported {len(records)} public notes, {len(payload.encode())} bytes; updated {changed} HTML pages.')
    return records


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--site-dir', type=Path, default=ROOT / 'site')
    parser.add_argument('--no-inject', action='store_true')
    parser.add_argument('--extra-output', type=Path)
    args = parser.parse_args()
    build(args.site_dir, not args.no_inject, args.extra_output)
