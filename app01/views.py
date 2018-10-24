from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.


def article(request, *args, **kwargs):
    # 获取当前Url
    condition = {}
    for k, v in kwargs.items():
        kwargs[k] = int(v)
        if v == '0':
            pass
        else:
            condition[k] = v

    # 筛选条件
    result = models.Article.objects.filter(**condition)
    article_type_list = models.ArticleType.objects.all()
    category_list = models.Category.objects.all()
    # 根据url中的name反生成url,而不仅是获取Url
    from django.urls import reverse
    url = reverse("article", kwargs={'article_type_id': '1', 'category_id': '2'})
    print(request.path_info)
    print(kwargs)
    print(url)
    return render(request, 'article.html',
                  {
                      'result': result,
                      'article_type_list': article_type_list,
                      'category_list': category_list,
                      'kwargs_dict': kwargs,
                  })


def req(request):
    print(request.GET)

    return render(request, 'req.html')