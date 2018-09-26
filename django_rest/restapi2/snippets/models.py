from django.db import models

# Create your models here.
class Snippets(models.Model):
	created=models.DateTimeField(auto_now_add=True)
	title=models.CharField(max_length=101,blank=True,default='')
	code=models.TextField();
	linenos=models.BooleanField(default=False)

	class meta:
		ordering=('created',)