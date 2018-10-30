from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import PostForm


def post(request, slug=None):
    item = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {
        'item': item,
        'title': item
    })


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()
            form.save_m2m()
            return redirect(item.get_absolute_url())
    else:
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form, 'title': 'Add Post'})


def edit_post(request, pk=None):
    item = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect(item.get_absolute_url())
    else:
        form = PostForm(instance=item)
        title = 'Edit: %s' % item
        return render(request, 'blog/post_form.html', {'form': form, 'item': item, 'title': title})
