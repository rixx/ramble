---
layout: page
---
{% for post in site.posts %}

<article>
    <b><a href="{{site.baseurl}}{{post.url}}">{{ post.title }}</a>:</b>
    {{ post.summary }}

    {% assign refutes = "" %}
    {% assign refuted_by = "" %}
    {% assign is_refuting = false %}
    {% assign is_refuted_by = false %}
    {% for other_post in site.posts %}
        {% if post.refutes contains other_post.slug %}
            {% assign is_refuting = true %}
            {% capture refutes %}
                {{ refutes }}{% if refutes %}, {% endif %}<a href="{{ other_post.url }}">{{ other_post.title }}</a>
            {% endcapture %}
        {% endif %}
        {% if other_post.refutes contains post.slug %}
            {% assign is_refuted_by = true %}
            {% capture refuted_by %}
                {{ refuted_by }}{% if refuted_by %}, {% endif %}<a href="{{ other_post.url }}">{{ other_post.title }}</a>
            {% endcapture %}
        {% endif %}
    {% endfor %}

    {% if is_refuting %}
    This post refutes: {{ refutes|strip|remove_first: "," }}.
    {% endif %}
    {% if is_refuted_by %}
    This post is refuted by: {{ refuted_by|strip|remove_first: "," }}.
    {% endif %}
</article>

{% endfor %}
