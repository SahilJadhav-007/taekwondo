from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("login_user",views.login_user, name="login"),
    path("admission", views.admission, name="admission"),
    path("contact", views.contact, name="contact"),
    path("store", views.store, name="store"),
    path("store/product/<int:product_id>/", views.product, name="product"),
    path("store/product/purchase/<int:product_id>/", views.purchase, name="purchase"),\
    path("confirm_purchase/<int:product_id>/", views.confirm_purchase, name="confirm_purchase"),
]
