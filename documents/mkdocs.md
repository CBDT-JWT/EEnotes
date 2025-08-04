# 🚀 用 MkDocs 搭建专业美观的文档网站

!!! info "创作声明"
    本文由AI(ChatGPT-4o)生成。
MkDocs 是一个简洁强大的静态网站生成器，专为文档项目而设计。它以 Markdown 编写内容，几行命令即可部署出漂亮的网站，适合开发文档、学习笔记、项目说明等用途。尤其配合 Material 主题和 MathJax，既美观又功能强大，非常适合写技术或数学类文档。

首先确保你已安装好 Python。使用 pip 安装 MkDocs，只需一行命令：

```
pip install mkdocs
```

然后创建你的文档项目目录，初始化配置：

```
mkdocs new my-docs
cd my-docs
```

为了让你的网站变得更现代化，我们推荐使用 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)。安装它也非常简单，只需执行下面命令：

```
pip install mkdocs-material
```

然后在 `mkdocs.yml` 文件中，将主题指定为 `material`：

```
theme:
  name: material
```

此时你已经可以运行 `mkdocs serve` 预览带 Material 主题的页面，体验极其清爽的 UI。如果你文档中涉及数学公式，可以进一步添加对 MathJax 的支持。Material 官方推荐的方式是启用 `pymdownx.arithmatex` 扩展，并加载 MathJax 资源。同时，可以配置警告框等内容。

首先，在 `mkdocs.yml` 中添加相关配置如下：

```
site_name: CBDT的资料屋
markdown_extensions:
  - pymdownx.arithmatex:
      generic: true
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - attr_list
  - md_in_html
site_url: http://www.jiangwt.org/index.html
extra_css:
- themes/css/custom.css
- themes/css/simpleLightbox.min.css
- themes/css/pied_piper.css
- https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css
  
theme:
  name: material
  icon:
    admonition:
      note: octicons/tag-16
      abstract: octicons/checklist-16
      info: octicons/info-16
      tip: octicons/squirrel-16
      success: octicons/check-16
      question: octicons/question-16
      warning: octicons/alert-16
      failure: octicons/x-circle-16
      danger: octicons/zap-16
      bug: octicons/bug-16
      example: octicons/beaker-16
      quote: octicons/quote-16
extra_javascript:
- themes/js/custom.js
- themes/js/simpleLightbox.min.js
- themes/js/optionalConfig.js
- themes/js/mermaidloader.js
- themes/js/umlconvert.js
- themes/js/mathjax.js
- themes/js/katex.js

- https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js
- https://cdnjs.cloudflare.com/ajax/libs/flowchart/1.17.1/flowchart.min.js
- https://cdnjs.cloudflare.com/ajax/libs/raphael/2.3.0/raphael.min.js
- https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.6/underscore-min.js
- https://cdn.jsdelivr.net/npm/@mermaid-js/mermaid-mindmap@9.3.0/dist/diagram-definition.0faef4c2.min.js
- https://cdn.jsdelivr.net/npm/markdown-it-plantuml@1.4.1/index.min.js
- https://cdnjs.cloudflare.com/ajax/libs/webfont/1.6.28/webfontloader.js
- https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-mml-chtml.js
- https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-chtml.js
- https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-chtml-full.js
- https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-svg-full.js
- https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js
- https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js
```
然后添加文件`/javascripts/mathjax.js`如下：
```js
window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };
  
  document$.subscribe(() => { 
    MathJax.startup.output.clearCache()
    MathJax.typesetClear()
    MathJax.texReset()
    MathJax.typesetPromise()
  })
```
这样你就可以在 Markdown 中书写 TeX 语法的数学公式了。例如你可以这样写行内公式 `$E=mc^2$` 或块公式：

```
$$
\int_{a}^{b} f(x)\,dx = F(b) - F(a)
$$
```

预览时所有数学内容都会自动渲染，无需手动刷新或转换。Material 主题还提供深色模式、搜索功能、响应式布局等现代化功能，使你的文档不仅实用还具有专业外观。

完成后你可以使用 `mkdocs build` 构建静态文件，或用 `mkdocs gh-deploy` 一键发布到 GitHub Pages。整个流程极为流畅，写文档的效率与体验都会大幅提升！

同时，为了兼容更多的markdown来源，可以使用如下python脚本将线上图床下载到本地：
```python
from pathlib import Path
import re
import shutil
import requests
import hashlib

# 设置根目录
root_dir = Path("/your/dir/to/docs")  # ← 修改为你的路径

# 匹配 markdown 图像（不含 style）
markdown_img_pattern = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)\)(?!\{:.*?\})')
# 匹配 HTML 图像
html_img_pattern = re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*>', re.IGNORECASE)

# 统一格式
def format_image(alt, src):
    return f'![{alt}]({src}){: style="display: block; margin: auto; width: 60%;" }{{: style="display: block; margin: auto; width: 60%;" }}'

# 下载远程图片
def download_image(url, asset_dir):
    asset_dir.mkdir(exist_ok=True)
    try:
        # 使用文件名或哈希作为本地名
        ext = Path(url).suffix or ".png"
        name_hash = hashlib.sha1(url.encode()).hexdigest()
        filename = f"{name_hash}{ext}"
        filepath = asset_dir / filename

        if not filepath.exists():
            print(f"Downloading {url} -> {filepath}")
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            filepath.write_bytes(resp.content)
        return filepath
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

# 处理所有 Markdown 文件
for file_path in root_dir.rglob("*.md"):
    content = file_path.read_text(encoding="utf-8")
    original_content = content
    file_dir = file_path.parent
    asset_dir = file_dir / "assets"

    # 替换 markdown 图片语法
    def replace_markdown(match):
        alt, src = match.group(1), match.group(2)
        if src.startswith("http://") or src.startswith("https://"):
            local_img = download_image(src, asset_dir)
            if local_img:
                rel_path = local_img.relative_to(file_dir)
                return format_image(alt, rel_path)
            else:
                return match.group(0)  # 保留原图
        else:
            return format_image(alt, src)

    content = markdown_img_pattern.sub(replace_markdown, content)

    # 替换 HTML 图片语法
    def replace_html(match):
        src, alt = match.group(1), match.group(2)
        if src.startswith("http://") or src.startswith("https://"):
            local_img = download_image(src, asset_dir)
            if local_img:
                rel_path = local_img.relative_to(file_dir)
                return format_image(alt, rel_path)
            else:
                return match.group(0)
        else:
            return format_image(alt, src)

    content = html_img_pattern.sub(replace_html, content)

    # 写入文件（若发生更改）
    if content != original_content:
        backup_path = file_path.with_suffix(file_path.suffix + ".bak")
        if backup_path.exists():
            backup_path.unlink()
        shutil.copy2(file_path, backup_path)
        file_path.write_text(content, encoding="utf-8")
        print(f"Updated: {file_path.relative_to(root_dir)} (backup replaced)")
    else:
        print(f"Skipped: {file_path.relative_to(root_dir)}")
```
最终编译出的效果可以参考本站。

