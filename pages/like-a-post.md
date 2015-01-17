---
layout: default
title: Like a Post
index: 9
---

# Like a Post

On both the home page (the `/` view) and a user's profile page (the `/profile/<username>` view), a series of posts is displayed accompanied with a link beside each post to 'like' the post. Clicking this link sends a `GET` request to the `/like_post/<post_id>` view, which is defined as:

```python
@app.route('/like_post/<post_id>', methods=['GET'])
def like_post(post_id):
    username = session.get('username')
    if not username:
        abort(400, 'You must be logged in to like a post.')

    user = User(username)
    user.like_post(post_id)
    flash('Liked post.')
    return redirect(request.referrer)
```

A `User` object is initialized with the logged-in user's username, and the `User.like_post()` method is called, which is defined within the `User` class in `models.py`:

```python
class User:

	...

    def like_post(self, post_id):
        user = self.find()
        post = graph.find_one("Post", "id", post_id)
        graph.create_unique(Relationship(user, "LIKED", post))
```

Both `user` and `post` are `py2neo.Node` objects. We'll pass a `py2neo.Relationship` object to the [`Graph.create_unique()`](http://py2neo.org/2.0/essentials.html#py2neo.Graph.create_unique) method to create the `(:User)-[:LIKED]->(:Post)` relationship in the database if it doesn't exist yet. This'll prevent someone from liking a post more than once.

The link that sends the request is defined in the `display_posts.html` template, which you already saw in the previous section:

{% raw %}
```html
  <ul class=posts>
  {% for post in posts %}
    <li>
    	<b>{{ post.title }}</b>
        {% if request.path == '/' %}
    	by <a href="{{ url_for('profile', username=post.username) }}">{{ post.username }}</a>
        {% endif %}
    	on {{ post.date }}
    	<a href="{{ url_for('like_post', post_id=post.id) }}">like</a><br>
    	<i>{{ ', '.join(post.tags) }}</i><br>
    	{{ post.text }}
  {% else %}
    <li>There aren't any posts yet!
  {% endfor %}
  </ul>
```
{% endraw %}

When a user clicks the link, the `GET` request is sent to `/like_post/<post_id>`, and `<post_id>` is replaced with the id of the post.

<p align="right"><a href="{{ site.baseurl }}/pages/similarity-between-users.html">Next: Similarities Between Users</a></p>