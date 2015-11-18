---
layout: default
title: 用户注册
index: 5
---

# 用户注册

每个用户都要注册一个账号。注册成功将在数据库中创建一个 `User` 结点，具有 `username` 和 `password` 属性，密码经过哈希处理。

注册页面位于 `/register`，接受 `GET` 和 `POST` 请求。访问者打开页面时发出 `GET` 请求，填写注册表单时发出 `POST` 请求。`views.py` 中 `/register` 视图定义如下：

```python
from .models import User, get_recent_assets
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(username) < 1:
            flash('Your username must be at least one character.')
        elif len(password) < 5:
            flash('Your password must be at least 5 characters.')
        elif not User(username).register(password):
            flash('A user with that username already exists.')
        else:
            session['username'] = username
            flash('Logged in.')
            return redirect(url_for('index'))

    return render_template('register.html')
```

`request` 变量是 Flask 对象，用来处理传入请求，可以用来访问请求的数据。比如请求的方法就储存在 `request.method`，无论是 `GET`、`POST` 还是其它可能的类型。如上所述，访问者打开页面时发出 `GET` 请求，填写注册表单时发出 `POST` 请求。此视图检查方法的类型，如果是 `GET` 请求就简单地交由 Flask [`render_template()`](http://flask.pocoo.org/docs/0.10/api/#flask.render_template) 返回来自 `asset/templates` 目录的 `register.html` 模版，并传递必要的上下文（在此例中，为错误信息）。然而, 如果是 `POST` 请求，`username` 和 `password` 将被处理，假如满足一切条件，用户将被创建。为了更好地理解，我们看下 `models.py` 中定义的 `User` 类。

```python
from py2neo import Graph, Node, Relationship, authenticate
from passlib.hash import bcrypt
from datetime import datetime
import os
import uuid

url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')

if username and password:
    authenticate(url.strip('http://'), username, password)

graph = Graph(url + '/db/data/')

class User:
    def __init__(self, username):
        self.username = username

    def find(self):
        user = graph.find_one("User", "username", self.username)
        return user

    def register(self, password):
        if not self.find():
            user = Node("User", username=self.username, password=bcrypt.encrypt(password))
            graph.create(user)
            return True
        else:
            return False
```

`User` 类的一个对象由 `username` 参数初始化。`User.find()` 方法调用 py2neo 的 [`Graph.find_one()`](http://py2neo.org/2.0/essentials.html#py2neo.Graph.find_one) 方法用给定用户名在数据库中查找标签为 User 的结点，返回一个 [`py2neo.Node`](http://py2neo.org/2.0/essentials.html#nodes) 对象。对于 User 结点我们基于用户名属性建立了唯一性约束，则不能有多于一个用户使用同一用户名。`User.register()` 方法检查数据库中是否有同名用户；如果没有，用给定用户名和密码创建用户，传递 `py2neo.Node` 对象给 [`Graph.create()`](http://py2neo.org/2.0/essentials.html#py2neo.Graph.create) 方法。注册成功返回 `True`。

最后，为了完整地理解注册过程，我们必须要看下 `register.html` 模版：

{% raw %}
```html
{% extends "layout.html" %}
{% block body %}
  <h2>Register</h2>
    <form action="{{ url_for('register') }}" method="post">
        <dl>
            <dt>Username:</dt>
            <dd><input type="text" name="username"></dd>
            <dt>Password:</dt>
            <dd><input type="password" name="password"></dd>
        </dl>
        <input type="submit" value="Register">
    </form>
{% endblock %}
```
{% endraw %}

`views.py` 中的 `register()` 方法用 flash 提供了 `message` 字符串。与 `render_template()` 一起传递的变量叫做 “上下文”，可以在相对应的 `.html` 模版中使用双大括号访问。在此是通过嵌入的 `layout.html`：

{% raw %}
```html
<!doctype html>
<title>My Assets</title>
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
<div class="page">
  <h1>My Assets</h1>
  <div class="metanav">
  {% if session.username %}
  Logged in as {{ session.username }}
  {% endif %}
  <a href="{{ url_for('index') }}">Home</a>
  {% if not session.username %}
    <a href="{{ url_for('register') }}">Register</a>
    <a href="{{ url_for('login') }}">Login</a>
  {% else %}
    <a href="{{ url_for('profile', username=session.username) }}">Profile</a>
    <a href="{{ url_for('logout') }}">Logout</a>
  {% endif %}
  </div>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block body %}{% endblock %}
</div>
```
{% endraw %}

表单能够发出 `POST` 请求给 `/register` 视图，是由于此动作 {% raw %}`action="{{ url_for('register') }}"`{% endraw %}。[`url_for()`](http://flask.pocoo.org/docs/0.10/api/#flask.url_for) 是 Flask 用来访问视图函数中定义的 URL 的方法。表单数据可通过输入组件的名称获取；比如，用户填在 `username` 文本框里的字符串就用 `request.form['username']`。

<p align="right"><a href="{{ site.baseurl }}/pages/login-a-user.html">下节：用户登录</a></p>
