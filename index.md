---
layout: page
---

## Featured posts

{% for post in site.posts %}{% if post.featured %}
    {% include post_snippet.html %}
{% endif %}{% endfor %}


## All posts

{% for post in site.posts %}
    {% include post_snippet.html %}
{% endfor %}
