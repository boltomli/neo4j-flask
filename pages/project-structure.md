---
layout: default
title: 项目结构
index: 3
---

# 项目结构

Explore Flask 有[很好的文档](https://exploreflask.com/organizing.html)讲述组织项目的最佳实践。我们采用相对简单的结构：

```
run.py
requirements.txt
asset/
	__init__.py
	models.py
	views.py
	indexes.py
	static/
		style.css
	templates/
		index.html
		register.html
		login.html
		logout.html
		profile.html
		display_assets.html
```

上节里我们已经生成了 `requirements.txt`。一般来说，我们在 `models.py` 中定义类和方法等，在 `views.py` 中定义“视图”，也就是站点页面。`asset/` 目录里的 `__init__.py` 文件使得 `asset` 可以被用作[包](https://exploreflask.com/organizing.html#package)。

我们在 `views.py` 中引入 `models.py` 里必要的类和函数并初始化应用。在 `__init__.py` 中也要引入 `views.py` 和 `models.py`。

`run.py` 用来启动开发服务器，生产环境中用不到。`run.py` 文件内容如下：

```python
from asset import app
import os

app.secret_key = os.urandom(24)
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

设定 `secret_key` 以使用会话，后面会讲到。把 `debug` 设为 `True` 方便看到出问题时的错误栈信息，生产环境中应该设为 `False`。使用 `python run.py` 启动应用，并在浏览器中访问[http://localhost:5000](http://localhost:5000).

`asset/static` 目录包含所有 CSS，JavaScript 和图片文件。`asset/templates` 目录包含所有 Jinja2 模版.

如果使用 Neo4j 2.2 及以上版本，请分别设置环境变量 `NEO4J_USERNAME` 和 `NEO4J_PASSWORD`：

```
$ export NEO4J_USERNAME=username
$ export NEO4J_PASSWORD=password
```

也可以在 `conf/neo4j-server.properties` 中设置 `dbms.security.auth_enabled=false`。当然，生产环境中不能这样做。可以想想有没有其它办法。

<p align="right"><a href="{{ site.baseurl }}/pages/the-data-model.html">下节：数据模型</a></p>
