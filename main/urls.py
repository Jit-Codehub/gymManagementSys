from django.urls import path
from .import views
urlpatterns = [
    path('', views.home),
    path('pagedetail/<int:id>/', views.page_detail, name="pagedetail"),
    path('faq/', views.faq_list, name="faq"),
    path('enquiry/', views.enquiry, name="enquiry"),
    path('gallery/', views.gallery, name="gallery"),
    path('gallerydetail/<int:id>/', views.gallery_detail, name="gallerydetail"),
]
