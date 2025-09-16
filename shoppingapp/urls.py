from django.urls import path
from shoppingapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('womens',views.women_section,name='women'),
    path('mens',views.men_section,name='men'),
    path('kids_xandder',views.kid_xander,name='kids_xander'),
    path('boy_section',views.kids_section_boy,name='boy'),
    path('girl_section',views.kids_section_girl,name='girl'),
    path('registration',views.registration,name='register'),
    path('forgetpassword',views.forgetpassword,name='forgetpassword'),

    #!women setion
    
    path('sarees',views.sarees,name='sarees'),
    path('salwar',views.salwar,name='salwar'),
    path('kurti',views.kurti,name='kurti'),
    path('women_inner',views.women_inner,name='women_inner'),
    path('women_jeans',views.women_jeans,name='women_jeans'),
    path('lehanaga',views.lehanga,name='lehanga'),
    path('cart',views.cart,name='cart'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('about',views.about,name='about'),

    #!men section
    path('t-shirts',views.tshirt,name='tshirt'),
    path('shirts',views.shirt,name='shirt'),
    path('kurtas',views.kurta,name='kurta'),
    path('mens-jeans',views.mens_jeans,name='mens_jeans'),
    path('mens-inner',views.mens_inner,name='mens_inner'),
    path('mens-suit',views.mens_suit,name='mens_suit'),

    #!others
    path('profile',views.profile,name='profile'),
    path('validation',views.validation,name='validation'),



]
