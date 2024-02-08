from .models import Post
from .forms import NewPostForm
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_edit')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/add_post.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/update_post.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('post_list')

# def post_list_view(request):
#     posts_list = Post.objects.filter(status='pub').order_by('-datetime_edit')
#     return render(request, 'blog/posts_list.html', {'post_list': posts_list})

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})


# def add_post(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#             # return post_list_view(request)
#
#     else:
#         form = NewPostForm()
#         return render(request, 'blog/add_post.html', context={'form': form})

#part2
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     post_user = User.objects.all()[0]
    #
    #     Post.objects.create(title=post_title, text=post_text, author=post_user, status='pub')
    #     return post_list_view(request)
    # else:
    #     return render(request, 'blog/add_post.html')

# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#
#     return render(request, 'blog/update_post.html', context={'form': form})


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#
#     return render(request, 'blog/delete_post.html', context={'post': post})
