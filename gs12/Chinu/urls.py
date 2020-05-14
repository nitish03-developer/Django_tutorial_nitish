from django.urls import path
from . import views
urlpatterns = [
    path('chinudj/', views.chinu_dj),
    path('chinupy/', views.chinu_py),
]