from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import SubscriberForm
from .forms import ContactForm
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.defaultfilters import slugify
from taggit.models import Tag
from django.views.generic import DetailView, ListView



# Create your views here.
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context

class PostList(TagMixin, ListView):
    template_name = 'blog/post_list.html'
    model = Post
    paginate_by = '10'
    queryset = Post.objects.all()
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetail(TagMixin, DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'post'
"""
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
"""
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(Post.title)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def contact(request, template='contact/contact.html'):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            post = form.save()
            post.save()
            return HttpResponseRedirect('/success')
    else: 
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

def success(request):
    return render(request, 'contact/success.html')

def about(request):
    return render(request, 'blog/about.html')
            

class TagIndexView(TagMixin, ListView):
    template_name = 'blog/post_list.html'
    model = Post
    paginate_by = '10'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


        