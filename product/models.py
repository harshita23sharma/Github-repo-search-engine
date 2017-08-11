from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 220,)
	body = models.TextField(max_length = 220,)
	date = models.DateTimeField(max_length = 220,)
	url = models.CharField(max_length = 22,)

	def __str__(self):
		return str(self.title)

'''
python manage.py makemigrations
python manage.py migrate
'''