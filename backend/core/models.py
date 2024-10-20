from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
class User_Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=300)
    image = models.FileField(upload_to='user_profile', default='default.jpg')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    
@receiver(post_save, sender=User)
def create_users_profile(sender, created, instance, **kwargs):
    if created:
        add_users_profile = User_Profile.objects.create(user=instance)
        add_users_profile.save()
    


