---
layout: default
title: 显示资产
index: 8
---

# 显示资产

主页（`/` 视图）和用户页（`/profile/<username>` 视图）都将显示资产。主页显示最近添加的5件资产；用户页显示用户的全部资产。函数 `get_recent_assets` 获取最近添加的10件资产，方法 `User.get_assets` 获取用户的全部资产（实际不会有很多）。

```python
def get_recent_assets():
    query = """
    MATCH (user:User)-[:OWNS]->(asset:Asset)<-[:APPLIES_TO]-(spec:Spec)
    RETURN user.username AS username, asset, COLLECT(spec.name) AS specs
    ORDER BY asset.timestamp DESC LIMIT 10
    """

    return graph.cypher.execute(query)
```

```python
class User:

    ...

    def get_assets(self):
        query = """
        MATCH (user:User)-[:OWNS]->(asset:Asset)<-[:APPLIES_TO]-(spec:Spec)
        WHERE user.username = {username}
        RETURN asset, COLLECT(spec.name) AS specs
        ORDER BY asset.asset_id DESC LIMIT 20
        """
        # In general one user won't own many assets.
        # Limit for performance in case.
        return graph.cypher.execute(query, username=self.username)
```

[`Graph.cypher.execute()`](http://py2neo.org/2.0/cypher.html#py2neo.cypher.CypherResource.execute) 的结果是 [`RecordList`](http://py2neo.org/2.0/cypher.html#py2neo.cypher.RecordList)，其中每个元素都是 [`Record`](http://py2neo.org/2.0/cypher.html#py2neo.cypher.Record)。`Record` 可以通过属性或键访问。

在 `index.html` 模版和 `profile.html` 模版中均包含 `display_assets.html` 模版：

{% raw %}
```
{% include "display_assets.html" %}
```
{% endraw %}

`display_assets.html` 如下，使用 `include` 就等同于直接插入代码：

{% raw %}
```html
  <ul class="assets">
  {% for row in assets %}
    <li>
    	<b>{{ row.asset.name }}</b>
        {% if request.path == "/" %}
    	by <a href="{{ url_for('profile', username=row.username) }}">{{ row.username }}</a>
        {% endif %}
        with ID {{ row.asset.asset_id }}<br>
    	<i>{{ ", ".join(row.specs) }}</i><br>
  {% else %}
    <li>There aren't any assets yet!
  {% endfor %}
  </ul>
```
{% endraw %}

用 `if request.path == "/"` 来检查是否位于主页。如果在主页上，显示资产所属用户名，因为最近添加的资产可能来自多个用户。否则，如果在用户页，无需显示用户名，正在访问的用户页即是。

Cypher 返回的集合，如 `COLLECT(DISTINCT spec.name) AS specs`，在 Python 中作为 `list` 返回。模版中的一小段 Python 代码即可处理；如上述 `", ".join(row.specs)` 将列表转换为逗号分隔的字符串。

<p align="right"><a href="{{ site.baseurl }}/pages/logout-a-user.html">下节：用户登出</a></p>
