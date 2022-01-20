from multiprocessing import context
from django.shortcuts import render
from .models import thumb
from django.db.models import Q
from .forms import ThumbForm
from django.http.response import JsonResponse
import random

# Create your views here.

def home(request):
	pics=list(thumb.objects.all())
	a = random.randint(0,len(pics)-1)
	b = random.randint(0,len(pics)-1)


	if a==b:
		a = random.randint(0,len(pics)-1)

	# print("a = ",a," b = ",b)
	
	picpair=[pics[a],pics[b]]

	context={
		'pics':picpair,
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

def addthumb(request):
	print("working")
	form=ThumbForm(request.POST)

	# print("\n\n\nvalid\n\n\n\n")
	url=request.POST['url']
	rating=0
	img_url=urltoimg(url)
	new_thumb=thumb(url=url,rating=rating,img_url=img_url)
	new_thumb.save()
	a=thumb.objects.values().order_by('-rating')
	thumbs=list(a)

	context={
		'thumbs':thumbs,
	}

	return JsonResponse(context)

