from django.shortcuts import redirect,render
from .models import *  # Assuming you have these models
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404




@login_required(login_url='a/login/')
def success(request):
    return render(request,'store/ordersuccess.html')

def index(request):
    order = Order.objects.filter(user=request.user)
    orderitems = OrderItem.objects.filter(order__in=order)
    context = {'order':order, 'orderitems':orderitems}
    return render(request,'store/order/orders.html',context)

def view(request,t_no):
    order = Order.objects.filter(trackno=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {'order':order, 'orderitems':orderitems}
    return render(request, "store/order/view.html", context)


