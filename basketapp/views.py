from django.urls import path
import basketapp.views as controller

app_name = 'basketapp'
urlpatterns = [
    path( '' , controller.basket, name= 'view' ),
    path( 'add/<int:pk>/' , controller.basket_add, name= 'add' ),
    path( 'remove/<int:pk>)/' , controller.basket_remove, name= 'remove' ),
]