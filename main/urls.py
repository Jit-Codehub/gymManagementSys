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
    path('user-dashboard/', views.user_dashboard, name="user_dashboard"),
    #user-dashboard section part
    path('update-profile/', views.update_profile, name="update_profile"),
    #trainer login-logout
    path('trainerlogin/', views.trainerlogin, name="trainerlogin"),
    path('trainerlogout/', views.trainerlogout, name="trainerlogout"),
    #notification
    path('notifs/', views.notifs, name="notifs"),
    path('get_notifs/', views.get_notifs, name="get_notifs"),



]
