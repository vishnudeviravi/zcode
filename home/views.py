from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import  timezone


def home(request):
    product = Product.objects.all
    pro = Product.objects.raw('SELECT * FROM home_product ORDER BY upvote  DESC LIMIT 3 ')
    return render(request,'home.html',{'product':product,'pro':pro})

def search(request):
    if request.method == 'POST':
        hashtag = request.POST['search']
        product1 = Product.objects.filter(hashtags1=hashtag)
        product5 = Product.objects.filter(hashtags2=hashtag)
        product2 = Product.objects.filter(hashtags3=hashtag)
        product3 = Product.objects.filter(hashtags4=hashtag)
        product4 = Product.objects.filter(hashtags5=hashtag)
        product6 = Product.objects.filter(product_name=hashtag)
        pro = Product.objects.raw('SELECT * FROM home_product ORDER BY upvote  DESC LIMIT 3 ')
        return render(request,'home.html',{'product5':product5,'product1':product1,'product2':product2,'product3':product3,'product4':product4,'product6':product6,'pro':pro})

@login_required
def add(request):
    if request.method == 'POST':
        if request.POST['product_name'] and request.POST['hashtags1'] and request.POST['caption'] and request.FILES['icon'] and request.POST['description'] and request.POST['url'] and request.FILES['screenshot'] and request.FILES['document'] :
            product = Product()
            product.product_name = request.POST['product_name']
            product.pub_date = timezone.datetime.now()
            product.hashtags1 = request.POST['hashtags1']
            product.hashtags2 = request.POST['hashtags2']
            product.hashtags3 = request.POST['hashtags3']
            product.hashtags4 = request.POST['hashtags4']
            product.hashtags5 = request.POST['hashtags5']
            product.caption = request.POST['caption']
            product.icon = request.FILES['icon']
            product.description = request.POST['description']
            product.creator = request.user
            product.url = request.POST['url']
            product.image = request.FILES['screenshot']
            product.code = request.FILES['document']
            product.save()
            return redirect('home')
    else:
        return render(request,'add.html')

def info(request,id):
    info = get_object_or_404(Product,pk=id)
    return render(request,'info.html',{'info':info})
@login_required()
def upvote(request,id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        product.upvote += 1
        product.save()
        return redirect('/'+str(product.id))



