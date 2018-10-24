from django.db import models

# Create your models here.


class Category(models.Model):
    '''
    文章分类
    '''
    caption = models.CharField(max_length=16)


class ArticleType(models.Model):
    '''
    文章类型
    '''
    caption = models.CharField(max_length=16)


class Article(models.Model):
    '''
    title 标题， content 内容
    '''
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)
    category = models.ForeignKey(to=Category, on_delete=True)
    article_type = models.ForeignKey(to=ArticleType, on_delete=True)


    # 不需要Articletype表的情况下，可以使用如下方式
    # 此种方式，分类存在内存中，不经常变动，减少DB交互
    # type_choice = (
    #     (0, '类型1'),
    #     (1, '类型2'),
    #     (2, '类型3'),
    # )
    # article_type_id = models.IntegerField(choices=type_choice)