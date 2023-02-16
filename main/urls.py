from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('pagedetail/<int:id>/', views.page_detail, name="pagedetail"),
    path('faq/', views.faq_list, name="faq"),
    path('enquiry/', views.enquiry, name="enquiry"),
    path('gallery/', views.gallery, name="gallery"),
    path('gallerydetail/<int:id>/', views.gallery_detail, name="gallerydetail"),
    path('pricing/', views.pricing, name="pricing"),
    path('accounts/signup/', views.signup, name="signup"),
    path('checkout/<int:plan_id>/', views.checkout, name="checkout"),


]
