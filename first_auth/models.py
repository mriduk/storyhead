from django.db import models
from django.contrib.auth.models import User

class readers(models.Model):
    username = models.CharField(max_length=200,null=False,primary_key=True)


    def __str__(self):
            return self.username
 

    class Meta:
        verbose_name = "Reader"
        verbose_name_plural = "Readers"







class story(models.Model):
    
   
    story_id=models.IntegerField(primary_key=True)
    story_name=models.CharField(max_length=150)
    description=models.TextField()
    current_view=models.ManyToManyField(User,related_name='current_reads',blank=True)
    total_read=models.ManyToManyField(User,related_name='total_reads',blank=True)
    

    def total(self):
            return self.total_read.count()

    def total1(self):
            return self.current_view.count()

 


    def __str__(self):
            return self.story_name

    
    class Meta:
        verbose_name = "Story section"
        verbose_name_plural = "Stories"


# Create your models here.
