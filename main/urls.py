from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # to connect actual way
from django.contrib.staticfiles.urls import static
from .import views


urlpatterns = [
    path('', views.shop_index, name="index"),  # path to the main page
    # main pages
    path("products/", views.shop_products, name="products"),
    path("single_product/", views.shop_single, name="single_product"),
    path("about/", views.about, name="about"),
    path("contact/", views.post_contacts, name="contact"),

    # inner links of the single product page review
    path("boxes/", views.product_boxes, name="boxes"),
    path("big_box/", views.product_big_box, name="big_box"),
    path("bouquets/", views.product_bouquets, name="bouquets"),

    path("admin/", admin.site.urls),
 #   path("shop/", include('shop.urls')),  #if the link starts from 'shop/' move to shop urls
  #  path('post/<int:post_id>/', show_post, name='post'), #post the variable link to the website
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
