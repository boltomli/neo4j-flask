---
layout: default
title: 数据模型
index: 4
---

# 数据模型

我们目前只考虑 IT 资产，大致需要 User（用户）、Asset（资产）以及 Spec（特性）三种结点。概念上讲，用户拥有资产，资产有其特性，用户还可能汇报给另一用户。（图片待加）

`<img width="100%" height="100%" src="http://i.imgur.com/9Nuvbpz.png">`

在开始之前先创建唯一性约束（从而也就有了索引）。用户、资产和特性都不应有重复。`__init__.py` 包含了如下代码，因此每次应用启动都会运行：

```python
from .views import app
from .models import graph

def create_uniqueness_constraint(label, property):
    query = "CREATE CONSTRAINT ON (n:{label}) ASSERT n.{property} IS UNIQUE"
    query = query.format(label=label, property=property)
    graph.cypher.execute(query)

create_uniqueness_constraint("User", "username")
create_uniqueness_constraint("Asset", "asset_id")
create_uniqueness_constraint("Spec", "name")
```

接下来，我们将探讨 `views.py` 中定义的每个视图及其在 `models.py` 中对应的逻辑。

<p align="right"><a href="{{ site.baseurl }}/pages/register-a-user.html">下节：用户注册</a></p>