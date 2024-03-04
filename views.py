from django.shortcuts import render, redirect
from .models import Video



def index_view(response):
    obj = Video.objects.all()
    p ={
        'obj': obj,
    }

    return render(response, 'main/index.html', p)

def add_view(response):
    return render(response, 'main/add.html', {})

def upload(response):
    obj = Video()
    if response.method == "POST":
        title = response.POST['title']
        video_url = response.POST['videourl']

        obj.title = title
        obj.videos = video_url
        obj.save()

        return redirect('/')
    return render(response, 'main/add.html', {})

def search_view(response):
    vid = Video()
    search_input = response.POST['search_input']
    id = Video.objects.only('id').get(title = search_input).id
    gotvid = Video.objects.get(id = id) 
    return render(response, 'main/index.html', {'gotvid': gotvid})
            

