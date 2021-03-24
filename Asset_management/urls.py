import Asset_management.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', Asset_management.views.get_index_page),
    path('submit/', Asset_management.views.submit),
    path('update/', Asset_management.views.update),
]
