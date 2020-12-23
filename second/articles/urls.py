from django.urls import path

from . import views
app_name = 'articles'
urlpatterns = [
    path('api/Article/', views.ArticleListCreate.as_view() ),
    ]