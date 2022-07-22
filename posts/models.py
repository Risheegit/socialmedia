from django.contrib.auth.models import User
from PIL import Image
from django.db import models
from django.utils import timezone

# Create your models here.
class Post (models.Model):
    op_id = models.CharField(max_length = 15)
    op_name = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'post_images', default = 'default.jpg')
    no_of_likes = models.IntegerField(default = 0 ) 
    likes = models.ManyToManyField(User, blank = True, related_name = "likes")
    dislikes = models.ManyToManyField(User, blank = True, related_name = "dislikes")
    caption = models.CharField(max_length=100)
    pub_date = models.DateTimeField (default= timezone.now)

    def __str__ (self):
        return 'Post by {}'.format(self.op_name)
    #Check what kind of images to put
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 500 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        elif img.height < 200 :
            output_size = (300, 300)
            img.thumbnail (output_size)
            img.save(self.image.path)

class LikePost (models.Model):
    post_id = models.CharField(max_length=100)
    username = models.CharField(max_length = 100)

    def __str__ (self):
        return self.username

class Comment(models.Model):
	post =models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
	username =models.CharField(max_length = 50)
	body =models.TextField()
	likes = models.ManyToManyField(User, blank = True, related_name = "comments_likes")
	pub_date = models.DateTimeField (default= timezone.now)
	def __str__(self):
		return 'Comment by {}'.format(self.username)

class Report (models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, null = True)
    report_id = models.CharField(max_length=100, blank=True, null = True)
    poster = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null = True)
    reporter = models.CharField(max_length=100, blank = True)
    image = models.ImageField(upload_to = 'post_images', default = 'default.jpg')
    caption = models.CharField(max_length=100)
    reportcount = models.IntegerField (default = 0)

    def __str__ (self):
        return self.caption
# Maybe make a report model to show initial report as in store the post content would be complex Do in end