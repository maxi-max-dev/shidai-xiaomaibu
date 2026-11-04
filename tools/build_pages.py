#!/usr/bin/env python3
"""把 desk.html 和 index.html 包成完整网页，放进 docs/ 给 GitHub Pages 用。

源文件按 claude.ai 试玩页的格式写，不带 <!doctype>、<head>、<body>，
发布到试玩页时会自动补上；GitHub Pages 需要我们自己补。
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEAD = ('<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<style>:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}'
        '[hidden]{display:none!important}img{max-width:100%}</style>\n</head>\n<body>\n')
PAGES = {'desk.html': 'index.html', 'index.html': 'chapter1.html'}

out = ROOT / 'docs'
out.mkdir(exist_ok=True)
for src, dst in PAGES.items():
    body = (ROOT / src).read_text(encoding='utf-8')
    (out / dst).write_text(HEAD + body + '\n</body>\n</html>\n', encoding='utf-8')
    print(f'{src} -> docs/{dst}')
(out / '.nojekyll').write_text('', encoding='utf-8')
