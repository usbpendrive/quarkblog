from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Tag


def home(request):
    items = Post.objects.all()
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'base/home.html', {'items': items, 'title': 'Home'})


def tag(request, slug=None):
    _tag = get_object_or_404(Tag, slug=slug)
    items = Post.objects.filter(tags__slug=slug)
    title = 'Items tagged with "%s"' % _tag
    return render(request, 'base/tag.html', {'items': items, 'tag': tag, 'title': title})


def profile(request):
    return render(request, 'base/profile.html', {'title': 'Profile'})


class Register(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
