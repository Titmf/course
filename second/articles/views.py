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
            return redirect('/api/Article')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

class ArticleListCreate(generics.ListCreateAPIView):
     queryset = Article.objects.all()
     serializer_class = ArticleSerializer
