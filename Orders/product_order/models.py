from django.db import models
from django.utils import timezone
from datetime import timedelta


class product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/',default='Null')

    def __str__(self):
        return self.name

class post(models.Model):
    post_text = models.CharField(max_length=250)
    date_published = models.DateTimeField('date published')

    def recently_published(self):
        return self.date_published >= timezone.now() - timedelta(days=1) <= self.date_published <= timezone.now()


    def __str__(self) :
        return self.post_text
    
class choice(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)   
    choice_text = models.CharField(max_length=250)
    vote = models.IntegerField(default=0)

    def __str__(self) :
        return self.choice_text

class chat_post(models.Model):
    advice = models.CharField(max_length=200)
    advice_text = models.TextField()
    published_on = models.DateField("date added")

    def __str__(self) :
        return self.advice

class chat_comment(models.Model):
    comment = models.ForeignKey(chat_post,on_delete=models.CASCADE,related_name='comments')
    author = models.CharField(max_length=100) 
    comment_text = models.TextField() 
    added_on  = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.comment_text


 


    
