from django.contrib.auth.decorators import login_required

from .forms import ModelForm
from django.shortcuts import render, redirect
from .models import  *
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
        price = request.POST.get('price')
        s=shop(name=name,desc=desc,price=price,img=img)
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


