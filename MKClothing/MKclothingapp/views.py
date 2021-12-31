from django.shortcuts import redirect, render
from .models import Products
from .forms import ProductForm, EditProductForm , CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def defcart(request):
   if request.user.is_authenticated:
    return redirect('inventory')
   else: 
    return render(request,"htmlss/cart.html")

def defadminreg(request):
   if request.user.is_authenticated:
    return redirect('inventory')
   else: 
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
          form.save()
          messages.success(request, 'Account succesfully created')
          return redirect('/adminlogin/')
        
    context= {'form': form}
    return render(request,"htmlss/adminreg.html", context)

def defshop(request):
 if request.user.is_authenticated:
    return redirect('inventory')
 else: 
    pd = Products.objects.all()
    context = {
      'pd': pd
    }

    return render(request,"htmlss/Shop.html",context)

def defcheckout(request):
   if request.user.is_authenticated:
    return redirect('inventory')
   else: 
    return render(request,"htmlss/checkout.html")

def defadminlogin(request):
  if request.user.is_authenticated:
    return redirect('inventory')
  else:
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login (request, user)
        return redirect('inventory')
      else:
        messages.info(request, 'Username or password is incorrect. ')
    context= {}
    return render(request,"htmlss/adminlogin.html", context)

def deflogout(request):
  logout(request)
  return redirect('adminlogin')

@login_required(login_url='adminlogin')
def defadminchangepass(request):
  return render(request,"htmlss/adminchangepass.html")

@login_required(login_url='adminlogin')
def defaddingform(request):
  formp = ProductForm(request.POST or None)
  
  if request.method == 'POST':
    formp = ProductForm(request.POST, request.FILES)
    if formp.is_valid():
      formp.save()

      return redirect('/inventory/')
  
  context = {
    'formproducts': formp
  }
  return render(request,"htmlss/addingform.html", context)

@login_required(login_url='adminlogin')
def defedit(request,pd_id):
  pd_edit = Products.objects.get(id=pd_id)
  form = EditProductForm(instance=pd_edit)
  
  if request.method == 'POST':
    form = EditProductForm(request.POST,request.FILES,instance=pd_edit)
    if form.is_valid():
      form.save()
      return redirect('/inventory/')

  context = {
    'form': form
  }
  
  return render(request,"htmlss/edit.html",context)

@login_required(login_url='adminlogin')
def defhistory(request):
  return render(request,"htmlss/history.html")

@login_required(login_url='adminlogin')
def definventory(request):  
  pd = Products.objects.all()
  context = {
    'pd': pd
  }

  return render(request,"htmlss/inventory.html",context)

def defdel(request,pdd_id):
  pd_del = Products.objects.get(id=pdd_id)
  pd_del.delete()
  return redirect('/inventory/')

  
  
