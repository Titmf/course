from django.db import models

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length = 100)
    article_text = models.TextField('текст статьи', max_length = 100)
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.TextField('афффтор')
    comment_text = models.TextField('коммент зис')
    
    def __str__(self):
        return self.author_name
    
    class Meta:
        verbose_name = 'Коментраий'
        verbose_name_plural = 'Комментарии'
