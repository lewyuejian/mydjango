from django.db import models

# Create your models here.


class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    c_Time = models.DateTimeField(auto_now_add=True)
    i_time = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.userId,self.username

    class Meta:

        ordering = ['-c_Time']
        verbose_name = '用户'
        verbose_name_plural = '用户'





