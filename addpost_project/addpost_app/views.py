from django.contrib.auth.decorators import login_required

from .forms import ModelForm
from django.shortcuts import render, redirect
from .models import  *

import requests
from django.shortcuts import render
# Create your views here.

def home(request):
    product=shop.objects.all()

    return render(request,"index.html",{"products":product})
@login_required(login_url='login')
def detail(request,shop_id):
    product1=shop.objects.get(id=shop_id)

    return render(request,"product_view.html",{"product":product1})

@login_required(login_url='login')
def add_product(request):
    if request.method=='POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        rating = request.POST.get('rating')
        s=shop(name=name,desc=desc,rating=rating,img=img)
        s.save()
        print("product added")

    return render(request,"add_post.html")

@login_required(login_url='login')
def update(request,id):
    obj=shop.objects.get(id=id)
    form=ModelForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{"form1":form,'obj1':obj})

@login_required(login_url='login')
def delete(request,id):
    if request.method == 'POST':
        obj=shop.objects.get(id=id)
        obj.delete()
        return redirect('/')

    return render(request, 'delete.html')



API_KEY = "802b578e"   # 🔑 replace this

def movie_search(request):
    query = request.GET.get('q')  # get search input
    movies = []

    if query:
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={query}"
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            movies = data.get("Search", [])
        else:
            movies = []

    return render(request, "movies.html", {"movies": movies})

