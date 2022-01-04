from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        prodt=products.objects.filter(catog=c_page,available=True)

    else:
        prodt=products.objects.all().filter(available=True)

    cat=category.objects.all()
    prod=products.objects.all()
    paginator=Paginator(prod,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)


    return render(request,'index.html',{'prod':prodt,'cat':cat,'pg':pro})

def proddetail(request,c_slug,product_slug):
    try:
        prod=products.objects.get(catog__slug =c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,"item.html",{'pr':prod})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'prod':prod})

