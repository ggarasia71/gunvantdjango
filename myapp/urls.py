from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('products/',views.products,name='products'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('new_password/',views.new_password,name='new_password'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('seller_index/',views.seller_index,name='seller_index'),
    path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
    path('seller_change_password/',views.seller_change_password,name='seller_change_password'),
    path('seller_view_product/',views.seller_view_product,name='seller_view_product'),
    path('seller_edit_profile/',views.seller_edit_profile,name='seller_edit_profile'),
    path('seller_product_details/<int:pk>/',views.seller_product_details,name='seller_product_details'),
    path('seller_edit_product/<int:pk>/',views.seller_edit_product,name='seller_edit_product'),
    path('seller_delete_product<int:pk>/',views.seller_delete_product,name='seller_delete_product'),
    path('seller_search_product/',views.seller_search_product,name='seller_search_product'),
    path('product_details<int:pk>/',views.product_details,name='product_details'),
    path('add_to_wishlist<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('remove_from_wishlist<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('add_to_cart<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('remove_from_cart<int:pk>/',views.remove_from_cart,name='remove_from_cart'),
    path('change_qty/',views.change_qty,name='change_qty'),
    path('success/',views.success,name='success'),
    path('payment/',views.payment,name='payment'),
]