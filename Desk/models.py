from django.db import models
from .Authentication import User
from django.urls import reverse


class Record(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.title + '|' + str(self.author) +"| " +str(self.id)

    def get_absolute_url(self):
        return reverse("")
