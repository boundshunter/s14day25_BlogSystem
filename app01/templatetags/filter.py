#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag
def filter_all(kwargs_dict, k):
    '''
    {% if kwargs_dict.article_type_id == 0 %}
        <a class="active" href="/article-0-{{ kwargs_dict.category_id }}.html">全部</a>
    {% else %}
        <a href="/article-0-{{ kwargs_dict.category_id }}.html">全部</a>
    {% endif %}
    :return:
    '''
    ret = ""
    if k == 'article_type_id':
        n1 = kwargs_dict[k]  # n1=kwargs_dict['article_type_id']
        n2 = kwargs_dict['category_id']
        if kwargs_dict['article_type_id'] == 0:
            ret = '<a class="active" href="/article-0-%s.html">全部</a>' % n2
        else:
            ret = '<a href="/article-0-%s.html">全部</a>' % n2
    else:
        n1 = kwargs_dict[k]  # kwargs_dict['category_id']
        n2 = kwargs_dict['article_type_id']
        if kwargs_dict['article_type_id'] == 0:
            ret = '<a class="active" href="/article-%s-0.html">全部</a>' % n2
        else:
            ret = '<a href="/article-%s-0.html">全部</a>' % n2
    return mark_safe(ret)


@register.simple_tag
def filter_article_type_list(article_type_list, kwargs_dict):
    '''
    {% for atel in article_type_list %}
        {% if kwargs_dict.article_type_id == atel.id %}
            <a class="active" href="/article-{{ atel.id }}-{{ kwargs_dict.category_id }}.html">{{ atel.caption }}</a>
        {% else %}
            <a  href="/article-{{ atel.id }}-{{ kwargs_dict.category_id }}.html">{{ atel.caption }}</a>
        {% endif %}
    {% endfor %}
    :return:
    '''
    ret = []
    for atel in article_type_list:
        if atel.id == kwargs_dict['article_type_id']:
            temp = '<a class="active" href="/article-%s-%s.html">%s</a>' % (atel.id, kwargs_dict['category_id'], atel.caption)
        else:
            temp = '<a href="/article-%s-%s.html">%s</a>' % (atel.id, kwargs_dict['category_id'], atel.caption)
        ret.append(temp)
    return mark_safe("".join(ret))



@register.simple_tag
def filter_category_list(category_list, kwargs_dict):
    '''
     {% for ctgy in category_list %}
        {% if kwargs_dict.category_id == ctgy.id %}
            <a class="active" href="/article-{{ kwargs_dict.article_type_id }}-{{ ctgy.id }}.html">{{ ctgy.caption }}</a>
        {% else %}
            <a  href="/article-{{ kwargs_dict.article_type_id }}-{{ ctgy.id }}.html">{{ ctgy.caption }}</a>
        {% endif %}
    {% endfor %}
    :param category_list:
    :param kwargs_dict:
    :return:
    '''

    ret = []
    for ctgy in category_list:
        if kwargs_dict['category_id'] == ctgy.id:
            temp = '<a class="active" href="/article-%s-%s.html">%s</a>' % (kwargs_dict['article_type_id'], ctgy.id,
                                                                            ctgy.caption)
        else:
            temp = '<a href="/article-%s-%s.html">%s</a>' % (kwargs_dict['article_type_id'], ctgy.id, ctgy.caption)
        ret.append(temp)
    return mark_safe("".join(ret))
