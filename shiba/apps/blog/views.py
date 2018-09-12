# -*- coding: utf-8 -*-

from operator import itemgetter
from itertools import groupby
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from apps.blog.models import Article, Category


def index(request):
    articles = Article.objects.filter(pubished=True).order_by('-create_time').values('title', 'slug', 'create_time', 'content')
    datas = []
    for a in articles:
        datas.append({
            "title": a['title'],
            "slug": a['slug'],
            "time": a['create_time'].strftime("%Y-%m-%d"),
            "content": _get_content(a['content'])[:200],
        })
    param_page = request.GET.get('page')
    paginator = Paginator(datas, settings.PAGE_LIMIT)
    try:
        datas = paginator.page(param_page)  # 获取某页对应的内容
    except PageNotAnInteger:
        datas = paginator.page(1)  # 如果页码不是个整数则取第一页
    except EmptyPage:
        datas = paginator.page(paginator.num_pages) 
    context = {'datas': datas}
    return render(request, 'blog/index.html', context=context)


def _get_content(content):
    lines = content.split('\n')
    ldatas = []
    nums = 0
    for l in lines:
        if not l or l.startswith('#'):
            continue
        ldatas.append(l)
        nums += 1
        if nums == 8:
            break
    return ''.join(ldatas)


def article(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        print('no article with slug')

    context = {'article': article}
    return render(request, 'blog/article.html', context=context)


def category(request):
    # datas = [
    #     {'category_slug': 'a', 'category_name': '沙巴', 'articles': [{'name': 'a', 'time': "2018-08-04"}, {'name': 'a', 'time': "2018-08-05"}]},
    #     {'category_slug': 'b', 'category_name': '沙巴2', 'articles': [{'name': 'b', 'time': "2018-08-05"}]},
    #     {'category_slug': 'c', 'category_name': '沙巴2', 'articles': [{'name': 'b', 'time': "2018-08-05"}]},
    #     {'category_slug': 'd', 'category_name': '沙巴2', 'articles': [{'name': 'b', 'time': "2018-08-05"}]},
    #     {'category_slug': 'e', 'category_name': '沙巴2', 'articles': [{'name': 'b', 'time': "2018-08-05"}]},
    # ]
    datas = []
    articles = list(Article.objects.filter(pubished=True).values('category', 'create_time', 'title', 'slug'))
    categories = Category.objects.all().values('id', 'slug', 'name')
    cid_2_category = {}
    for c in categories:
        cid_2_category[str(c['id'])] = (c['slug'], c['name'])

    articles.sort(key=itemgetter('category'))
    group_articles = groupby(list(articles), key=itemgetter('category'))
    for key, gas in group_articles:
        category_info = cid_2_category.get(str(key), '')
        data = {'category_slug': category_info[0], 'category_name': category_info[1], 'articles': []}
        for ga in gas:
            data['articles'].append({
                'slug': ga['slug'],
                'name': ga['title'],
                'time': ga['create_time'].strftime('%Y-%m-%d'),
            })
        datas.append(data)

    # 每一个分类，按照time降序排列
    for d in datas:
        d['articles'].sort(key=itemgetter('time'), reverse=True)

    context = {'datas': datas}
    return render(request, 'blog/category.html', context=context)