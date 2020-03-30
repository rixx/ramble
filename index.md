---
layout: page
---
{% for post in site.posts %}

<article>
    <b><a href="{{site.baseurl}}{{post.url}}">{{ post.title }}</a>:</b>
    {{ post.summary }}
</article>

{% endfor %}
