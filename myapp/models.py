from pyexpat import model
from django.db import models
from urllib.request import urlopen
import simplejson
# Create your models here.
class thumb(models.Model):
	url=models.CharField(max_length=200)
	rating=models.IntegerField(default=0)
	img_url=models.CharField(max_length=200,default=".")


	@property
	def urltoimg(self):
		if self.url and self.img_url==".":
			url=self.url
			vid_id=url[url.find('=')+1:]
			image_url="https://img.youtube.com/vi/"
			image_url+=vid_id
			image_url+="/hqdefault.jpg"
			self.img_url=image_url
			self.url=url
			self.save()
		return self.img_url

	def __str__(self):
		return f"video_url = {self.url}\nrating={self.rating}\nimg_url={self.img_url}"

