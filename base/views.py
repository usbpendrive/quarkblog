from django.shortcuts import render
from django.core.paginator import Paginator

from blog.models import Post


def home(request):
    items = Post.objects.all()
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'base/home.html', {'items': items, 'title': 'Home'})
