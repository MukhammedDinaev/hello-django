from django.urls import path
from hello_django.calc import views


urlpatterns = [
    path('', views.CalcPage.as_view()),
    path('<int:a>/<int:b>/', views.index),
]
