from django.db import models
import datetime
from django.utils import timezone





# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')#'date published' is an optional first argument to deginate a human redable name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
#each model is a class that subclasses django.db.model.Model
#Each model has a number of class variables, each of which represents a database field in the model.
#jo models.charfield hai wo represent karta hai ek type ko like varchar

#each field is represented by an instance of a FIELD class like CharField