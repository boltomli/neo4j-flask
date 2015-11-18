---
layout: default
title: 用户登出
index: 9
---

# 用户登出

用户点击页面顶端的 logout 链接以登出，发送 `GET` 请求给 `/logout` 视图：

```python
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out.')
    return redirect(url_for('index'))
```

将把 `username` 从会话中移除，把访问者带回到主页。登出后访问者无法添加资产，除非再次登录。

<p align="right"><a href="{{ site.baseurl }}/pages/add-style.html">下节：添加样式</a></p>