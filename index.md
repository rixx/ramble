---
layout: page
---

<p>This is a practice blog for unpolished, somewhat-kinda daily writing. You can find similar blogs
<a href="https://notebooks.rixx.de/">here</a>.</p>

<h2>Posts</h2>

<ul>
{% for post in site.posts %}
    <li>{% if post.featured %}🌟 {% endif %}<b><a href="{{site.baseurl}}{{post.url}}">{{ post.title }}</a></b><br>{{ post.summary }}</li>
{% endfor %}
</ul>
