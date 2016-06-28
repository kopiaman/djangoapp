from django.shortcuts import render, get_object_or_404 ,redirect

from .models import Post

from .forms import PostForm

def post_list(request):
    postlist = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': postlist})

def post_detail(request, pk):
    post_pk = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post_pk })

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)  #we create a form we pass this post as an instance both when we save the form:
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)  #opened a form with this post to edit:
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_delete.html', {'post':post})    

