from django.contrib import admin
from django.urls import path
from task1.views import index, index_reg, index_game, index_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('reg/', index_reg),
    path('games/', index_game),
    path('cart/', index_cart)

]
