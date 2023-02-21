from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.SayHelloView.as_view())
]
