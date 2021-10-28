from django.shortcuts import render

def defsignup(request):
  return render(request,"htmlss/signup.html")

def defproductpage(request):
  return render(request,"htmlss/productpage.html")

def deflogin(request):
  return render(request,"htmlss/login.html")

def defindex(request):
  return render(request,"htmlss/index.html")

def defforhim(request):
  return render(request,"htmlss/forhim.html")

def defAllproducts(request):
  return render(request,"htmlss/Allproducts.html")  
