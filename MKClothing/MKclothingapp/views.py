from django.forms import NullBooleanField
from django.shortcuts import redirect, render
from pymysql import NULL
from .models import History, Products, orderc
from .forms import ProductForm, EditProductForm , CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def check():
  check = orderc.objects.values_list('cancel', flat = True)
  var = len(check)

  if var == 0: 
    s = orderc(id = 1, cancel = 0, success = 0)
    s.save()
  else:
    return 

def complete_order(request,i_id):
  chisto = History.objects.get(id=i_id)
  cprod = Products.objects.get(itemname=chisto.pname)
  var1 = orderc.objects.get(id=1)

  plus = var1.success + 1
  var1.success = plus
  var1.save()

  if chisto.quan > cprod.stocks:
      messages.success(request, 'Not enough stocks.')
      return redirect('history')
  else:
  
      var = 'Hi ' + chisto.name + "! \n \nThis is to inform you that your that your order has been confirmed and is on it's way. Please prepare exact amount of PHP " + str(chisto.total) + '. \n \n Order Details:  \n   Product name: ' + chisto.pname +  ' \n   Quantity: ' + str(chisto.quan) + ' \n   Address: ' + chisto.address +  '\n \n Thank you! \n Meikai'

      subject = 'ORDER CONFIRMATION'
      message = var
      recipient_list = [chisto.email, ]
      send_mail( subject, message, 'mkclothing.elective02@gmail.com', recipient_list,fail_silently=False, )
      
      chisto.delete()
    
      return redirect('history')


def cancel_order(request,i_id):
  chisto = History.objects.get(id=i_id)
  cprod = Products.objects.get(itemname=chisto.pname)
  var = orderc.objects.get(id=1)

  plus = var.cancel + 1
  var.cancel = plus
  var.save()

  updatedstock = cprod.stocks + chisto.quan
  cprod.stocks = updatedstock  
  cprod.save()
 
  chisto.delete()


  return redirect('history')

  
@login_required(login_url='adminlogin') 
def defadminreg(request):
    form = CreateUserForm()
    if request.method == 'POST':
         form = CreateUserForm(request.POST)
         if form.is_valid():
          form.instance.is_superuser = True
          form.save()
          messages.success(request, 'Account succesfully created')
          return redirect('/adminreg/')
        
    context= {'form': form}
    return render(request,"htmlss/adminreg.html", context)

def defshop(request):
    check()
    pd = Products.objects.all()
    context = {
      'pd': pd
    }

    return render(request,"htmlss/Shop.html",context)

def defcheckout(request,data_id):
  yes = Products.objects.get(id=data_id)
  quan11 = request.POST.get('quantity')
  name1 = request.POST.get('name')
  email1 = request.POST.get('contact')
  add = request.POST.get('address')
  
  if request.method == 'POST':
    if quan11 == '' or name1 == '' or email1 == '' or add == '':
       messages.info(request, 'Please complete all information.')
    else:
      quan1 = int(quan11)
      if quan1 > yes.stocks:
        messages.info(request, "Sorry, we don't have enough stock for your order.")
      else:
        updatedstock = yes.stocks - quan1
        yes.stocks = updatedstock
        tots = yes.price * quan1
        s = History(name=name1, pname=yes.itemname, quan=quan1, total=tots, email=email1, address=add )
        s.save()
        yes.save()

        var = "Hi " + name1 + "! \n \n"  "This is to inform you that we have received your order. Kindly wait for our confirmation via e-mail before completing your payment. \n \n Order Details: \n Product name: " + yes.itemname + "\n Quantity: " + str(quan1) +  "\n Item Price: PHP " + str(yes.price) + "\n \n Thank you! \n Meikai"

        subject = 'ORDER PENDING'
        message = var
        recipient_list = [email1, ]
        send_mail( subject, message, 'mkclothing.elective02@gmail.com', recipient_list,fail_silently=False, )

        return redirect('shop')

        
  
  data = {'weee': yes}

  return render(request,"htmlss/checkout.html", data)

def defadminlogin(request):
    if request.user.is_authenticated:
     return redirect('inventory')
    else: 
      if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
          login (request, user)
          return redirect('inventory')
        else:
          messages.info(request, 'Invalid credentials. ')
      context= {}
      return render(request,"htmlss/adminlogin.html", context)

def deflogout(request):
  logout(request)
  return redirect('shop')

@login_required(login_url='adminlogin')
def defaddingform(request):
   if request.user.is_authenticated and not request.user.is_superuser:
      return redirect('shop')
   else:
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
   if request.user.is_authenticated and not request.user.is_superuser:
      return redirect('shop')
   else:
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
  histo = History.objects.all()
  var = orderc.objects.get(id=1)

  totalprocessed = var.success + var.cancel

  data = {
    'histo': histo,'var' : var, 'totalprocessed' : totalprocessed
  }
  return render(request,"htmlss/history.html", data)

@login_required(login_url='adminlogin')
def definventory(request):  
   if request.user.is_authenticated and not request.user.is_superuser:
      return redirect('shop')
   else:
    pd = Products.objects.all()
    context = {
      'pd': pd
    }
    return render(request,"htmlss/inventory.html",context)

def defdel(request,pdd_id):
  pd_del = Products.objects.get(id=pdd_id)
  pd_del.delete()
  return redirect('/inventory/')

  