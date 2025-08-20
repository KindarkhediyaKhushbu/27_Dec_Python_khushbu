from django.http import JsonResponse
from django.shortcuts import render,HttpResponseRedirect,redirect
from datetime import datetime
from django.db.models import Count
from app.models import Cart, Contact,Customer
from app.models import Product
from django.contrib import messages
from django.views import View
from .forms import CustomerRegistrationForm,CustomerProfileFrom
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return  render (request,'app/index.html')
def about(request):
    return  render (request,'app/about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent')
    return  render (request,'app/contact.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,"app/customerregistration.html",{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulation! User Register Successfully")
        else:
            messages.warning(request,"Invlaid Input Data")
        return render(request,"app/customerregistration.html",{'form':form})
   
def user_login(request):
    if request.method=="GET":
        fm=AuthenticationForm(request=request,data=request.GET)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
    else:
        fm=AuthenticationForm()
    return render(request,'app/login.html',{'form':fm})   

def user_logout(request):
    logout(request)
    return redirect("login")
    
# def user_profile(request):
#     return render(request,'app/profile.html')
class ProfileView(View):
    def get(self,request):
       form=CustomerProfileFrom()
       return render(request,'app/profile.html',locals())
    def post(self,request):
       form=CustomerProfileFrom(request.POST)
       if form.is_valid():
           user=request.user
           name=form.cleaned_data['name']
           locality=form.cleaned_data['locality']
           city=form.cleaned_data['city']
           mobile=form.cleaned_data['mobile']
           state=form.cleaned_data['state']
           zipcode=form.cleaned_data['zipcode']
           
           reg=Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
           reg.save()
           messages.success(request,"Congratulations! Profile save Successfully")
       else:
           messages.warning(request,"Invalid Input Data")
       return render(request,'app/profile.html',locals())
   
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',locals())



class CategoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return  render (request,'app/product.html',locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values('title')
        return  render (request,'app/product.html',locals())


class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"app/productdetails.html",locals())
    
class updateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileFrom(instance=add)
        return render(request,"app/updateAddress.html",locals())
    def post(self,request,pk):
        form=CustomerProfileFrom(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.mobile=form.cleaned_data['mobile']
            add.state=form.cleaned_data['state']
            add.zipcode=form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulations! Profile save Successfully")
        else:
           messages.warning(request,"Invalid Input Data")
        return redirect("address")
    
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    products=Product.objects.get(id=product_id)
    Cart(user=user,products=products).save()
    return redirect('/cart')

def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user) 
    amount=0
    for p in cart:
        value=p.quantity*p.products.discounted_price
        amount=amount+value
    totalamount=amount+40
    return render(request,'app/addtocart.html',locals())

def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        print(prod_id)
        data={
            
        }
        return JsonResponse(data)