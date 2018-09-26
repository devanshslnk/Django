from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
	
	arstist=models.CharField(max_length=250)
	album_name=models.CharField(max_length=250)
	album_code=models.IntegerField(default=0)
	def get_absolute_url(self):
		return  reverse('details',kwargs={'pk':self.pk})
	def __str__(self):
		return self.album_name+'-'+self.arstist
class Song(models.Model):
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
	file_type=models.CharField(max_length=10)
	song_title=models.CharField(max_length=250)
	def __str__(self):
		return self.song_title


