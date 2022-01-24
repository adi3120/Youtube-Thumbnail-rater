
import random
from django.db import models
from urllib.request import urlopen
import simplejson
import requests
from bs4 import BeautifulSoup


# Create your models here.
class thumb(models.Model):
	url=models.CharField(max_length=200)
	rating=models.IntegerField(default=0)
	img_url=models.CharField(max_length=200,default=".")
	title=models.CharField(max_length=200,default=".")


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
	
	@property
	def updatetitle(self):
		self.title=getitle(self.url)
		self.save()

	def adds(self,url):
		addimg(url)

	def randrate(self):
		print("\n\n\n\nupdating rating....")
		rate = random.randint(900,3000)
		print("\n\n\nnew rating = ",rate)

		self.rating=rate
		print("\n\n\nRating updated for id = ",self.id)
		self.save()

	@property
	def addimg(url):
		title=getitle(url)
		vid_id=url[url.find('=')+1:]
		image_url="https://img.youtube.com/vi/"
		image_url+=vid_id
		image_url+="/hqdefault.jpg"
		thumb(url=url,rating=0,img_url=image_url,title=title).save()
		

	def __str__(self):
		return f"video_url = {self.url}\nrating={self.rating}\nimg_url={self.img_url}"

def getitle(url):
	# print("getitle")
	r = requests.get(url)
	s = BeautifulSoup(r.text, "lxml")
	img_title = str(s.find("title"))
	img_title=img_title[7:-18]
	# print(f"\n\n\n\n{img_title}\n\n\n")

	return img_title

def addimg(url):
		title=getitle(url)
		vid_id=url[url.find('=')+1:]
		image_url="https://img.youtube.com/vi/"
		image_url+=vid_id
		image_url+="/hqdefault.jpg"
		print("\n\n\nCreated new thumbnail object: Title = ",title)
		thumb(url=url,rating=0,img_url=image_url,title=title).save()
		