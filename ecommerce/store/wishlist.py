from django.http import JsonResponse
from django.shortcuts import redirect,render
from .models import *  # Assuming you have these models
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def view(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,'wishlist.html',context)



def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if Wishlist.objects.filter(user=request.user, product_id=prod_id).exists():
                    return JsonResponse({'status': 'Product Already In Wishlist'})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':"Product added to Wishlist"})
            else:
                return JsonResponse({'status':'No such Product Found'})
        else:
            return JsonResponse({'status':'Login to continue'})
    else:
        return redirect('/')

def delwish(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = request.POST.get('product_id')
            if prod_id is None:
                return JsonResponse({'status': "Product ID is missing"})
            try:
                prod_id = int(prod_id)
            except ValueError:
                return JsonResponse({'status': "Invalid product ID format"})
            
            if Wishlist.objects.filter(user=request.user, product_id=prod_id).exists():
                wishlist = Wishlist.objects.get(user=request.user, product_id=prod_id)
                wishlist.delete()
                return JsonResponse({'status': 'Product Removed'})
            else:
                return JsonResponse({'status': 'Product Not Found in Wishlist'})
    return JsonResponse({'status': "Invalid request"})