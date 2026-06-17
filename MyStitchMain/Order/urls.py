from .models import Order
from . import views
from django.urls import path

urlpatterns = [
    path("", views.orderview, name='orderview'),
    path("<int:pk>/", views.oderdetailview, name='oderDetailView'),
    path("add/",views.orderAdd, name='orderAdd'),
    path("edit/<int:pk>/",views.orderedit, name='orderedit'),
    path("delete/<int:pk>/",views.orderdelete, name='orderdelete'),
    # path("add/gender/", views.getgender, name='getgender'),
    # path("add/<str:clothtype>/", views.measurementsview, name='measurementsview'),

]
