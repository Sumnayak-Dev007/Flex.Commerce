from django.http import JsonResponse
from django.shortcuts import redirect,render
from .models import *  # Assuming you have these models
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if Cart.objects.filter(user=request.user, Product=prod_id).exists():
                    return JsonResponse({'status': 'Product Already In Cart'})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty :
                        Cart.objects.create(user=request.user, Product=product_check, product_qty=prod_qty)
                        return JsonResponse({'status':"Product added successfully"})
                    else:
                        return JsonResponse({'status':"Only "+ str(product_check.quantity) +" quantity available"})
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status': "Login to Continue"})
    return redirect('/')



@login_required(login_url='a/login/')
def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    cart_quantities = 0

    for item in cart:
        # Access the product's quantity in stock
        cart_quantities = item.Product.quantity

    context = {'cart':cart,'cart_quantities': cart_quantities}
    return render(request,'store/cart.html',context)


def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, Product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(Product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':"Updated Successfully"})
    return redirect('/')

def deletecartview(request):
    if request.method == "POST":
        prod_id = request.POST.get('product_id')
        print(f"Received Product ID: {prod_id}")  # Debugging
        if prod_id:
            prod_id = int(prod_id)
            if Cart.objects.filter(user=request.user, Product_id=prod_id).exists():
                cart = Cart.objects.get(Product_id=prod_id, user=request.user)
                cart.delete()
                return JsonResponse({'status': "Deleted Successfully"})
    return JsonResponse({'status': "Invalid product data"})

def update_cart_quantity(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        new_quantity = int(request.POST.get('new_quantity'))

        product = get_object_or_404(Product, id=product_id)
        cart_item = get_object_or_404(Cart, user=request.user, product=product)

        # Check if the quantity is within stock limits
        if new_quantity <= product.quantity:
            cart_item.product_qty = new_quantity
            cart_item.save()
            return JsonResponse({'success': True, 'new_quantity': new_quantity})
        else:
            return JsonResponse({'success': False, 'message': 'Insufficient stock.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})