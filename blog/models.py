from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Description: Model Description
    """
    author=models.ForeignKey('auth.User' )
    title=models.CharField(max_length=200 )
    text=models.TextField()
    rate=models.IntegerField(default=1)
    
class Review(models.Model):
    """
    Description: Model Description
    """
    user_id=models.IntegerField(default=1)

class Like(models.Model):
    """
    Description: Model Description
    """
    user_id=models.IntegerField(default=0)
