from django.shortcuts import render,get_object_or_404,redirect

from blog.models import Post, Comment
from blog.forms import PostForm,CommentForm

from django.urls import reverse_lazy
from django.utils import timezone

# TO MAKE SURE THE USER IS LOGGED IN TO UTILIZE CERTAIN VIEWS
from django.contrib.auth.mixins import LoginRequiredMixin

# TO MAKE SURE THE USER IS LOGGED IN TO UTILIZE CERTAIN FUNCTIONS
from django.contrib.auth.decorators import login_required

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'


# ##################################
# COMMENTS VIEWS
# ##################################

class PostListView(ListView):
    # template_name =
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


# ##################################
# FUNCTION VIEWS
# ##################################

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # CHECK THAT THE FORM IS CORRECTLY FILLED OUT
            # SAVE THE FORM, BUT MAKE SURE THE COMMIT IS FALSE
            comment = form.save(commit=False)
            # THIS RELATES BACK TO THE COMMENT MODEL HAVING A FIELD FOR THE POST PRIMARY KEY: PK
            comment.post = post
            comment.save()
            # THIS TAKES YOU BACK TO THE POST DETAIL PAGE FOR THAT PARTICULAR POST
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()

    return render(request,'blog/comment_form.html',{'form': form})

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    # SINCE THE COMMENT WILL HAVE BEEN DELETED AFTER comment.delete(), WE NEED TO KEEP THE POST PK AS A VARIABLE
    post_pk = comment.post.pk
    comment.delete()
    # USING THE POST PK
    return redirect('post_detail',pk=post_pk)
