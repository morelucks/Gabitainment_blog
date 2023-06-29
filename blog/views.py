from datetime import date
from .models import Post, Comment, Author
from .forms import CommentForm, PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

all_posts=[]
def get_date(post):
    return post['date']

# Create your views here.
# def adminDashboard(request):
#     return render(request, 'blog/admin/index.html')
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
            print(user) 
        except:
            messages.error(request, "User does Not exist")
 
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("starting-page")
        else:
            messages.error(request, 'Username or password does not exist')
    context={}
    return render(request, "blog/include/login.html", context)
class StartingPageView(ListView):
    template_name="blog/index.html"
    model=Post
    # ordering=["-date"]
    

    def get_queryset(self):
        queryset= Post.objects.order_by("-date")
        return queryset
    def get_context_data(self, **kwargs):
        context=super(StartingPageView, self).get_context_data(**kwargs)
        context['posts']=Post.objects.all().order_by("-date")[3:7]
        context['sposts']=Post.objects.all().order_by("-date")[:1]
        context['twopost']=Post.objects.all().order_by("-date")[1:3]

        return context
class PostView(ListView):
    template_name="blog/all-post.html"
    model=Post
    ordering=["-date"]
    context_object_name="all_posts"

    # THE FUNCTION METHOD
# def posts(request):
#     all_posts=Post.objects.all().order_by("-date")
#     return render(request, "blog/all-post.html",{
#         "all_posts":all_posts
#     })
class PostDetailView(DetailView):
   def get(self, request, slug):
    post=Post.objects.get(slug=slug)
    context={
        "post":post,
        "post_tags":post.tags.all(),
        "comment_form":CommentForm(),
        "comments":post.comments.all().order_by("-id")
    }
    return render(request, "blog/post-detail.html", context)
   def post(self, request, slug):
    comment_form = CommentForm(request.POST)
    post=Post.objects.get(slug=slug)

    if comment_form.is_valid():
        comment=comment_form.save(commit=False)
        comment.post=post
        comment.save()

        return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        post=Post.objects.get(slug=slug)

    context={
        "post":post,
        "post_tags":post.tags.all(),
        "comment_form":CommentForm,
        "comments":post.comments.all().order_by("-id")
    } 
    return render(request, "blog/post-detail.html", context)

class DeleteComment(DeleteView):
    model=Comment
    success_url ="/"

    template_name="blog/include/delete-comment.html"


class CreatePost(CreateView):
    model=Post
    form_class=PostForm
    template_name="blog/include/create-post.html"
    def get_context_data(self, **kwargs):
        context=super(CreatePost, self).get_context_data(**kwargs)
        context['postform']=PostForm()
        return context
    def post(self, request):
     savem= PostForm(request.POST)

     if savem.is_valid():
        savem.save()
     return HttpResponseRedirect(reverse("login"))

def createPost(request):
    form=PostForm()
    if request.method=='POST':
        print(request.POST)
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("starting-page"))

    context={
        'postform':form
    }
    return render(request, "blog/include/create-post.html", context)

def updatePost(request, pk):
    post=Post.objects.get(id=pk)
    form=PostForm(instance=post)

    if request.method=='POST':
        form=PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("starting-page"))


    context={
        'postform':form
    }
    return render(request, "blog/include/create-post.html", context)
def deletePost(request, pk):
    post=Post.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return HttpResponseRedirect(reverse("starting-page"))

    context={
        'obj':post
    }
    return render(request, "blog/include/delete.html", context)

class CreateAuthor(CreateView):
    model=Author
    success_url ="/"

    fields=["first_name", "last_name", "email_address"]
    template_name="blog/include/author-form.html"

class DeleteAuthor(DeleteView):
    model=Author
    success_url ="/"

    template_name="blog/include/delete.html"

class UpdateAuthor(UpdateView):
    model=Author
    success_url="/"
    late_name="blog/include/author-form.html"
