from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from stock import views

#versiona de ip
router = routers.DefaultRouter()
router.register(r'stock', views.StockViews, 'stock')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title= "stock API"))
    
]
