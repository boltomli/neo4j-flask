---
layout: default
index: 1
title: 虚拟环境
---

# 虚拟环境

本节的概念对于几乎所有项目都适用，实现方法各有不同而已。Python 关于虚拟环境的[文档](http://docs.python-guide.org/en/latest/dev/virtualenvs/)值得一读。

在开始开发之前设置一个虚拟环境，使得其中的更改可以保存且不会影响其它项目。假如一个项目依赖 py2neo 1.6.4，另一个项目依赖 py2neo 2.0.0，虚拟环境可以保证每个项目都使用合适的包。

用 `pip` （Python 3版本）安装 `virtualenv`：

```
pip3 install virtualenv
```

创建一个叫做 `neo4j-asset` 的虚拟环境并激活：

```
virtualenv neo4j-asset
source neo4j-asset/bin/activate
```

激活之后，命令行提示符将显示当前使用的虚拟环境名。

用 `pip freeze` 查看 Python 包，确认当前处于何种状态：

```
pip3 freeze
```


```
wheel==0.24.0
```

<p align="right"><a href="{{ site.baseurl }}/pages/required-packages.html">下节：需要的包</a></p>