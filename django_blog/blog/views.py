from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Template to display all posts
    context_object_name = 'posts'
    ordering = ['-created_at']  # Show most recent posts first

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Template for a single post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the post's author to the logged-in user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can update

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can delete





class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['post', 'author',' created_at','updated_at','content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the post's author to the logged-in user
        return super().form_valid(form)

#def add_comment(request, post_id):
   # post = get_object_or_404(Post, id=post_id)
    #if request.method == 'POST':
       # form = CommentForm(request.POST)
        #if form.is_valid():
           # comment = form.save(commit=False)
            #comment.post = post
            #comment.author = request.user
            #comment.save()
           # return redirect('post_detail', pk=post.id)
   # else:
       # form = CommentForm()
   # return redirect('post_detail', pk=post.id)

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_edit.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})



def post_search(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()
    return render(request, 'blog/search_results.html', {'query': query, 'results': results})


def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name=tag_name)
    return render(request, 'blog/posts_by_tag.html', {'tag_name': tag_name, 'posts': posts})

