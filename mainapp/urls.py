from django.urls import path

import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    path('', controller.products, name='index'),  # {% url 'products:index' %}
    path('category/<int:pk>/', controller.products, name='category'),  # products:category id=1
    # path('details/<int:id>/', controller.product_detail, name='details'),  # products:details id=1
]