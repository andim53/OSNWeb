from django.db import models

# Create your models here.
class Soal(models.Model):
	title = models.CharField(max_length=255) # title less than 255 words
	intro = models.TextField()
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	
