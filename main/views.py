from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    banners = Banners.objects.all()
    services = Service.objects.all()[:3]
    gimgs = GalleryImage.objects.all().order_by('-id')[:9]
    return render(request, "main/home.html",{"banners":banners,"services":services,"gimgs":gimgs})

def page_detail(request,id):
    page = Pages.objects.get(id=id)
    return render(request,"main/page.html",{"page":page})

def faq_list(request):
    faqs = Faq.objects.all()
    return render(request,"main/faq.html",{"faqs":faqs})

def enquiry(request):
    msg = ""
    form = EnquiryForm()
    if request.method=="POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Data has been saved successfully"
    return render(request,"main/enquiry.html",{"form":form,"msg":msg})


def gallery(request):
    gallery = Gallery.objects.all().order_by('-id')
    return render(request,"main/gallery.html",{"gallerys":gallery})

def gallery_detail(request,id):
    gallery = Gallery.objects.get(id=id)
    gallery_imgs=GalleryImage.objects.filter(gallery=gallery).order_by('-id')
    return render(request,"main/gallery_imgs.html",{"gallery_imgs":gallery_imgs,"gallery":gallery})

def pricing(request):
    pricing = SubPlan.objects.all().order_by('price')
    dfeatures = SubPlanFeature.objects.all()
    return render(request,"main/pricing.html",{"plans":pricing,"dfeatures":dfeatures})


def signup(request):
    msg=""
    form = SignupForm()
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Thanks for registration"
    return render(request,"registration/signup.html",{"form":form,"msg":msg})



def checkout(request,plan_id):
    planDetail = SubPlan.objects.get(pk=plan_id)
    return render(request,"main/checkout.html",{"plan":planDetail})

def user_dashboard(request):
    return render(request,"user/dashboard.html")

def update_profile(request):
    msg = ""
    if request.method == "POST":
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            msg = "Profile has been updated"
    form = ProfileForm(instance=request.user)
    return render(request,"user/update_profile.html",{"form":form,"msg":msg})



def trainerlogin(request):
    msg = ""
    form = TrainerForm()
    if request.method=="POST":
        username = request.POST['username']
        pwd = request.POST['pwd']
        trainer = Trainer.objects.filter(username=username, pwd=pwd).count()
        if trainer > 0:
            request.session['trainerLogin']=True
            return redirect('/trainer_dashboard')
        else:
            msg='Invalid Credentials!!'
        
    return render(request,"trainer/login.html",{"form":form,"msg":msg})


def trainerlogout(request):
    del request.session['trainerLogin']
    return redirect('/trainerlogin')

        

        

