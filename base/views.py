from django.shortcuts import render

from blog.models import Post


def home(request):
    items = Post.objects.all()
    return render(request, 'base/home.html', {'items': items, 'title': 'Home'})
