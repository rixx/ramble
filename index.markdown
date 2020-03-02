---
layout: page
---
{% for post in site.posts %}

<article>
    <h2><a href="{{site.baseurl}}{{post.url}}">{{ post.title }}</a></h2>
    <p class="meta">{{ post.date|date:"%Y-%m-%d" }}</p>
    {{ post.content }}
</article>

{% endfor %}
