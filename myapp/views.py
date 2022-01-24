from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import thumb
from django.db.models import Q
from .forms import ThumbForm
from django.http.response import JsonResponse
import random
from bs4 import BeautifulSoup
import requests
import lxml

# Create your views here.

def home(request):
	pics=list(thumb.objects.all())
	a = random.randint(0,len(pics)-1)
	b = random.randint(0,len(pics)-1)


	if a==b:
		a = random.randint(0,len(pics)-1)

	# print("a = ",a," b = ",b)
	
	picpair=[pics[a],pics[b]]
	# titpair=[getitle(picpair[0].url),getitle(picpair[1].url)]

	context={
		'pics':picpair,
		# 'titles':titpair,
	}

	if request.method=="POST":
		tid=request.POST['tid']
		print(tid)
		thumbobj=thumb.objects.get(id=tid)
		# thumbobj=thumb.objects.get(Q(id=tid))
		thumbobj.rating+=1
		thumbobj.save()
	return render(request,'myapp/home.html',context)

def details(request):
	thumbs=thumb.objects.all().order_by("-rating")

	form=ThumbForm()
	context={
		'tmbs':thumbs,
		'form':form,
	}

	return render(request,'myapp/details.html',context)

def urltoimg(url):
	vid_id=url[url.find('=')+1:]
	image_url="https://img.youtube.com/vi/"
	image_url+=vid_id
	image_url+="/hqdefault.jpg"
	return image_url


def getitle(url):
	# print("getitle")
	r = requests.get(url)
	s = BeautifulSoup(r.text, "lxml")
	img_title = str(s.find("title"))
	img_title=img_title[7:-18]
	# print(f"\n\n\n\n{img_title}\n\n\n")

	return img_title


def addthumb(request):
	# print("working")
	form=ThumbForm(request.POST)

	# print("\n\n\nvalid\n\n\n\n")
	url=request.POST.get('thumburl')
	rating=0

	img_url=urltoimg(url)


	img_title=getitle(url)

	

	
	new_thumb=thumb(url=url,rating=rating,img_url=img_url,title=img_title)
	new_thumb.save()
	a=thumb.objects.values().order_by('-rating')
	thumbs=list(a)

	context={
		'thumbs':thumbs,
	}

	return JsonResponse(context)

def delthumb(request):
	context={}
	if request.method=="POST":
		imgid=request.POST['imgid']
		tmb=get_object_or_404(thumb,id=imgid)
		tmb.delete()

		context={
			'delid':imgid,
		}

	return JsonResponse(context)
