---
layout: default
title: 添加样式
index: 10
---

# 添加样式

以下改自 [Flask tutorial](http://flask.pocoo.org/docs/0.10/tutorial/css/) ，存储在 `/asset/static` 里的 `style.css` 文件：

```css
body            { font-family: sans-serif; background: #eee; }
a, h1, h3       { color: #377ba8; }
h1, h2, h3      { font-family: 'Georgia', serif; margin: 0; }
h1, h2          { border-bottom: 2px solid #eee; padding: 3px; }
h3              { padding: 3px; }
dd              { display: block; margin-left: 0px; }
dl              { font-weight: bold; }
a:visited 		{ color: #800080; }
.page           { margin: 2em auto; width: 35em; border: 5px solid #ccc; padding: 0.8em; background: white; }
.assets         { list-style: none; margin: 0; padding: 0; }
.assets li      { margin: 0.8em 1.2em; }
.assets li h2   { margin-left: -1em; }
.metanav        { text-align: right; font-size: 0.8em; padding: 0.3em; margin-bottom: 1em; background: #fafafa; }
.flash          { background: #cee5F5; padding: 0.5em; border: 1px solid #aacbe2; }
.error          { background: #f0d6d6; padding: 0.5em; }
```

<p align="right"><a href="{{ site.baseurl }}/pages/run-application.html">下页：运行应用</a></p>