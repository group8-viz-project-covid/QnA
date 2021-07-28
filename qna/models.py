from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.
class Question(models.Model):
	user = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,null = True)
	question = models.TextField()
	timestamp = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.question

class Answer(models.Model):
	question = models.ForeignKey(Question,on_delete = models.CASCADE,related_name = "answers")
	answer = models.TextField()
	timestamp = models.DateTimeField(default = timezone.now)
	user = models.ForeignKey(get_user_model(),on_delete = models.CASCADE, null = True)

	def __str__(self):
		return self.answer
