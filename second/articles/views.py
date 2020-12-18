from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/choose_purse')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def index(request):
    latest_artiles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_artiles_list': latest_artiles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Чек лист не найден")
    render(request, 'articles/detail.html', {'article': a})

class ArticleListCreate(generics.ListCreateAPIView):
     queryset = Article.objects.all()
     serializer_class = ArticleSerializer
