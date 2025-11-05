from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import *
# Create your views here.

def home(request):
    category= Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, 'store/index.html',context)


def collections(request):
    category= Category.objects.filter(status=0)
    context = {'category':category}
    return render(request,"store/collections.html",context)


def collectview(request, slug):
    # Fetch category by slug and ensure it's active
    category = Category.objects.filter(slug=slug, status=0).first()
    print(category)
    if category:
        # Fetch all products related to the found category
        products = Product.objects.filter(category=category, status=0)
        
        # Debugging step
        if not products.exists():
            messages.warning(request, "No product found for this category.")
        
        context = {'products': products, 'category': category}
        print(f"Category found: {category}")
        print(f"Products found: {products}")
        return render(request, 'store/product/products.html', context)
    else:
        messages.warning(request, "No such category found.")
        return redirect('collections')


    
def productview(request, cate_slug, prod_slug):
    category = Category.objects.filter(slug=cate_slug, status=0).first()
    if category:
        product = Product.objects.filter(category=category, slug=prod_slug, status=0).first()
        if product:
            context = {'product': product}
            return render(request, "store/product/view.html", context)
        else:
            messages.error(request, "No such product found")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')


def productlist(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productsList = list(products)

    return JsonResponse(productsList,safe=False)


def searchproduct(request):
    if request.method == 'POST':
        searchitemi = request.POST.get('searchitemi', '').strip()
        if not searchitemi:
            return redirect(request.META.get('HTTP_REFERER', '/'))

        # Search by name or meta_keyword
        product = Product.objects.filter(
            models.Q(name__icontains=searchitemi) | models.Q(meta_keywords__icontains=searchitemi)
        ).first()
        
        if product:
            # Use absolute URL for the redirection
            return redirect(f'/collections/{product.category.slug}')
        else:
            messages.info(request, "No product matched your search")
            return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect(request.META.get('HTTP_REFERER', '/'))

