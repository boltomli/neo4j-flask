---
layout: default
title: 添加资产
index: 7
---

# 添加资产

用户成功登录或注册后，会被重定向到 `/` 主页视图。`session.username` 不是 `None` 时，会显示一个表单供用户添加资产。此表单将向 `/add_asset/<username>` 视图发送带有名称、唯一ID和特性列表的 `POST` 请求，`<username>` 即当前登录会话的用户名。`views.py` 中此视图定义如下：

```python
@app.route('/add_asset', methods=['POST'])
def add_asset():
    name = request.form['name']
    asset_id = request.form['asset_id']
    specs = request.form['specs']

    if not name or not asset_id or not specs:
        if not name:
            flash('You must give your asset a nick name.')
        if not asset_id:
            flash('You must give your asset an ID.')
        if not specs:
            flash('You must give your asset at least one property.')
    else:
        User(session['username']).add_asset(name, asset_id, specs)

    return redirect(url_for('index'))
```

资产名称、ID、特性经由 `POST` 请求发出后检查是否为空。若通过检查，以 `name`、`asset_id` 和 `specs` 作为参数调用 `User.add_asset()` 方法。`add_post()` 方法定义于 `User` 类：

```python
class User:

	...

    def add_asset(self, name, asset_id, specs):
        user = self.find()
        asset = Node(
            "Asset",
            id=str(uuid.uuid4()),
            name=name,
            asset_id=asset_id,
            timestamp=timestamp(),
            date=date()
        )
        rel = Relationship(user, "OWNS", asset)
        graph.create(rel)

        specs = [x.strip() for x in specs.split('|')]
        for t in set(specs):
            spec = graph.merge_one("Spec", "name", t)
            rel = Relationship(spec, "APPLIES_TO", asset)
            graph.create(rel)
```

经由 `User.find()` 返回用户的 `py2neo.Node` 对象。随后，另一个 `Node` 对象 `asset` 将以显示的属性创建。用 `uuid` 包的 [`uuid4()`](https://docs.python.org/2/library/uuid.html#uuid.uuid4) 方法生成随机ID（不同于我们按项目需求自定义的唯一资产ID）。时间戳与日期由 `models.py` 中定义的函数确定：

```python
def timestamp():
    epoch = datetime.utcfromtimestamp(0)
    now = datetime.now()
    delta = now - epoch
    return delta.total_seconds()

def date():
    return datetime.now().strftime('%F')
```

有了 `user` 和 `asset` 两个变量，我们可以在图中创建 `(:User)-[:OWNS]->(:Asset)` 关系对象 [`py2neo.Relationship`](http://py2neo.org/2.0/essentials.html#relationships) 传给 `Graph.create()`。最后，对于每个由竖线 `|` 分隔的特性，创建 `(:Spec)-[:APPLIES_TO]->(:Asset)` 关系。使用 `Graph.merge_one()` 方法确保找到已有的特性或用该 `name` 属性创建一个新的 `Spec` 结点。

添加资产的表单位于 `index.html`：

{% raw %}
```html
{% extends "layout.html" %}
{% block body %}

<h2>Home</h2>
  {% if session.username %}
    <h3>Add asset</h3>
    <form action="{{ url_for('add_asset') }}" method="post">
        <dl>
            <dt>Name:</dt>
            <dd><input type="text" size="30" name="name"></dd>
            <dt>Asset ID:</dt>
            <dd><input type="text" size="30" name="asset_id"></dd>
            <dt>Specs (separated by |)</dt>
            <dd><textarea name="specs" rows="5" cols="40"></textarea></dd>
        </dl>
        <input type="submit" value="Add">
    </form>
  {% endif %}

<br>

<h3>My assets</h3>
{% include "display_assets.html" %}

{% endblock %}
```
{% endraw %}

<p align="right"><a href="{{ site.baseurl }}/pages/display-assets.html">下节：显示资产</a></p>
