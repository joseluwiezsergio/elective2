from django.shortcuts import redirect, render
from .models import Products
from .forms import ProductForm, EditProductForm

def defsignup(request):
  return render(request,"htmlss/signup.html")

def defcart(request):
  return render(request,"htmlss/cart.html")

def defadminreg(request):
  return render(request,"htmlss/adminreg.html")

def defshop(request):

  pd = Products.objects.all()
  context = {
    'pd': pd
  }

  return render(request,"htmlss/Shop.html",context)

def defcheckout(request):
  return render(request,"htmlss/checkout.html")

def defadminlogin(request):
  return render(request,"htmlss/adminlogin.html")

def defadminchangepass(request):
  return render(request,"htmlss/adminchangepass.html")

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

def defhistory(request):
  return render(request,"htmlss/history.html")

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

  
  
