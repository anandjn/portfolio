from django.db import models
# Create your models here.

def user_directory_path(instance, filename):
    #file will be uploaded to MEDIA_ROOT/images//user_<id>_<filename>
    ## need to implement a overwrite functionality
    return "images/profile/user_{0}_{1}".format(instance.id, filename)

class Home(models.Model):
    greeting = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    para_1 = models.TextField()
    para_2 = models.TextField()
    para_3 = models.TextField()
    picture = models.ImageField(upload_to = user_directory_path)

    def __str__(self):
        return self.name + "'s Homepage."

