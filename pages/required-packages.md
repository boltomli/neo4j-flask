---
layout: default
title: 需要的包
index: 2
---

# 需要的包

我们需要安装 Flask，py2neo，passlib 和 bcrypt：

```
pip3 install flask
pip3 install py2neo
pip3 install passlib
pip3 install bcrypt
```

再执行一次 `pip freeze`，可以看到很多包已被装上：

```
pip3 freeze
```

```
bcrypt==2.0.0
cffi==1.3.0
Flask==0.10.1
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
passlib==1.6.5
py2neo==2.0.8
pycparser==2.14
six==1.10.0
Werkzeug==0.11.2
wheel==0.24.0
```

按照 Flask 文档的建议，我们最好把这些依赖确定下来，以便于重建环境，且可以避免破坏性的升级包：

```
pip3 freeze > requirements.txt
```

<p align="right"><a href="{{ site.baseurl }}/pages/project-structure.html">下节：项目结构</a></p>