from django.http import JsonResponse
from django.shortcuts import redirect,render
from .models import *
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User  # Assuming you have these models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import random


@login_required(login_url='a/login/')
def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.Product.quantity:
            item.delete()
    
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.Product.selling_price * item.product_qty

    profile = Profile.objects.filter(user=request.user).first()
    context = {
        'cart':cart,
        'total':total_price,
        'profile':profile
    }
    return render(request,'store/checkout.html',context)




@login_required(login_url='a/login/')
def placeorder(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            profile  = Profile()
            profile.user = request.user
            profile.phone = request.POST.get('phone')
            profile.address = request.POST.get('address')
            profile.city = request.POST.get('city')
            profile.state = request.POST.get('state')
            profile.country = request.POST.get('country')
            profile.pincode = request.POST.get('pincode')
            profile.save()


        neworder = Order()
        neworder.user=request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.pincode = request.POST.get('pincode')

        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')

        cart = Cart.objects.filter(user=request.user)
        cart_total = 0
        for item in cart:
            cart_total = cart_total + item.Product.selling_price * item.product_qty

        neworder.total_price = cart_total
        track = 'order'+str(random.randint(1111111,9999999))
        while Order.objects.filter(trackno=track) is None:
            track = 'order'+str(random.randint(1111111,9999999))
        neworder.trackno = track
        neworder.save()
        print(neworder.country)
        print(neworder.payment_mode)

        cartems = Cart.objects.filter(user=request.user)
        for item in cartems:
            OrderItem.objects.create(
                order = neworder,
                product = item.Product,
                price = item.Product.selling_price,
                qty = item.product_qty
            )

            #To decrease product quantity from stock
            orderproduct = Product.objects.filter(id=item.Product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()

        #To clear User's cart
        Cart.objects.filter(user=request.user).delete()
        messages.success(request,"Your Order has been Placed Successfully")

        payMode = request.POST.get('payment_mode')
        if (payMode == "Paid by Razorpay" or payMode == "Paid by Paypal" or payMode == "COD"):
            return JsonResponse({'status':"Your order has been placed successfully"})
    return redirect('/')


@login_required(login_url='a/login/')
def paywithRzrpay(request):
    cart = Cart.objects.filter(user=request.user)
    cart_total = 0
    for item in cart:
        cart_total = cart_total + item.Product.selling_price * item.product_qty

    return JsonResponse({'cart_total':cart_total})





