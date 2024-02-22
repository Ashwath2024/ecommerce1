from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),  # Corrected function name
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]