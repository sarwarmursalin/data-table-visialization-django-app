from django.urls import path
from. import views

urlpatterns = [
    path('data/',views.data, name='data'),
    path('create/', views.create, name='create'),
    path('update/<int:stock_id>/', views.update, name='update'),
    path('delete/<int:stock_id>/', views.delete, name='delete'),
]
