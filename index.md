---
layout: page
---

## Featured posts

<ul>
{% for post in site.posts %}{% if post.featured %}
    <li><b><a href="{{site.baseurl}}{{post.url}}">{{ post.title }}</a></b><br>{{ post.summary }}</li>
{% endif %}{% endfor %}
</ul>


## All posts

<ul>
{% for post in site.posts %}
    <li><b><a href="{{site.baseurl}}{{post.url}}">{{ post.title }}</a></b><br>{{ post.summary }}</li>
{% endfor %}
</ul>
