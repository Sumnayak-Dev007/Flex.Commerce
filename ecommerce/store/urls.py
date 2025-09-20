from django.urls import path,include
from . import views,cart,wishlist,checkout,orders

urlpatterns=[
    path('',views.home,name="home"),
    path('collections/',views.collections,name="collections"),
    path('collections/<str:slug>',views.collectview,name="collectview"),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),
    
    path('product-list/',views.productlist,),
    path('searchproduct/',views.searchproduct,name="searchproduct"),

    path('add-to-cart/',cart.addtocart,name='addtocart'),
    path('cart',cart.viewcart,name='cart'),
    path('update-cart/',cart.updatecart,name='updatecart'),
    path('delete-cart-item/',cart.deletecartview,name='deletecartview'),
    path('wishlist/',wishlist.view,name='wishlist'),
    path('add-to-wishlist/',wishlist.addtowishlist,name='addtowishlist'),
    path('del-wish/',wishlist.delwish,name='delwish'),
    path('update-cart-quantity/',cart.update_cart_quantity, name='update_cart_quantity'),
    path('checkout/',checkout.index,name="checkout"),
    path('placeorder/',checkout.placeorder,name="placeorder"),
    path('proceed-to-pay/',checkout.paywithRzrpay,name="proceed-to-pay"),
    path('my-orders/',orders.success,name="myorders"),
    path('orders/',orders.index,name="orders"),
    path('view-orders/<str:t_no>',orders.view,name="orderview"),
    
    
]

