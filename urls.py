from django.urls import path
from food import views

urlpatterns =[
    path('',views.index,name="food-index2"),
    path('login2/',views.login2,name="food-login2"),
    path('menu2/',views.menu2,name="food-menu2"),
    path('contact2/',views.contact2,name="food-contact2"),
    path('payment2/',views.payment2,name="food-payment2"),
    path('forgotpassword2/',views.forgotpassword2,name="food-forgotpassword2"),
    path('signup2/',views.signup2,name="food-signup2"),
    path('about2/',views.about2,name="food-about2"),
    path('ourblog2/',views.ourblog2,name="food-ourblog2"),


    
]