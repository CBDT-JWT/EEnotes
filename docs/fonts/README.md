Home Editorial SC is a renamed WOFF2 display subset of Noto Serif CJK SC Medium.
Source: https://github.com/notofonts/noto-cjk/blob/main/Serif/OTF/SimplifiedChinese/NotoSerifCJKsc-Medium.otf
License: SIL Open Font License 1.1, included as OFL-home-editorial.txt.

The subset contains Latin, punctuation, homepage UI characters and the profile name.
It is used for homepage display headings and the date. Dynamic article titles and
body copy retain the site's sans-serif stack. Songti SC/Noto Serif SC are fallbacks
for future profile-name characters that are outside the bundled subset.

The shared Site Editorial SC family uses editorial-base.woff2 for interface text
and editorial-cjk-01.woff2 onward for remaining GB2312 common Chinese characters.
editorial-fonts.css declares disjoint Unicode ranges, so a page downloads only
the characters it uses. These are renamed subsets of the same licensed source.
