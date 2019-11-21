from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    """
    this line connects a post to an authorized user
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date =  models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    """
    this says, when I create a post, to which view do I go next?
    "get_absolute_url" is the required name for this method
    """
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    this line connects a comment to an actual post
    'blog.Post' means connect to the 'Post' model of the 'blog' app
    """
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    # THIS WILL BE CALLED IN A VIEW
    def approve(self):
        self.approved_comment = True
        self.save()

    # WHEN LEAVING THIS VIEW, GO TO THE LIST OF POSTS
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
