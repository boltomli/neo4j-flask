---
layout: default
title: 用户登录
index: 6
---

# 用户登录

用户可以注册帐号之后，我们就可以定义登录视图，允许用户登录站点并开始 [会话](http://flask.pocoo.org/docs/0.10/quickstart/#sessions)。`views.py` 中 `/login` 视图定义如下：

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not User(username).verify_password(password):
            flash('Invalid login.')
        else:
            session['username'] = username
            flash('Logged in.')
            return redirect(url_for('index'))

    return render_template('login.html')
```

代码和 `/register` 视图类似。`login.html` 中的表单用来输入用户名和密码。`User` 对象以给定用户名初始化。填入表单的密码通过 [`bcrypt.verify()`](https://pythonhosted.org/passlib/lib/passlib.hash.bcrypt.html) 和数据库中取出的哈希比对。验证成功返回 `True`，之后创建 `session` 对象，`session['username']` 被设为给定用户名。`session` 对象让我们可以用 cookie 请求跟随用户。用户随后被转向首页，可以开始添加资产了。`models.py` 中 `User.verify_password()` 方法定义为：

```python
class User:

    ...

    def verify_password(self, password):
        user = self.find()
        if user:
            return bcrypt.verify(password, user['password'])
        else:
            return False
```

可以像 Python 字典一样获取 `py2neo.Node` 的属性。在这里，从 `user` 对象获取密码属性用 `user['password']`。

`login.html` 模版和 `register.html` 几乎一样，除了表单动作改向 `/login` 视图发 `POST` 请求：
{% raw %}
```html
{% extends "layout.html" %}
{% block body %}
  <h2>Login</h2>
	<form action="{{ url_for('login') }}" method="post">
        <dl>
            <dt>Username:</dt>
            <dd><input type="text" name="username"></dd>
            <dt>Password:</dt>
            <dd><input type="password" name="password"></dd>
        </dl>
        <input type="submit" value="Login">
	</form>
{% endblock %}
```
{% endraw %}

<p align="right"><a href="{{ site.baseurl }}/pages/add-an-asset.html">下节：添加资产</a></p>