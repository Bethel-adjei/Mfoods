from django.urls import path
from .views import HomePage,About,Contact,AllShop,Checkout,SingleProduct,Cart,News,SingleNews,Testimonial
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage, name="homepage"),
    path('about-us', About, name="about"),
    path('contact', Contact, name="contact"),
    path('shop', AllShop, name="shop"),
    path('check-out', Checkout, name="checkout"),
    path('single-product/<int:id>/', SingleProduct, name="single-product"),
    path('cart', Cart, name="cart"),
    path('news', News, name="news"),
    path('single-news', SingleNews, name="single-news"),
    path('testimonial', Testimonial, name="testimonial"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)