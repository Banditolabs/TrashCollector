from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('landfill/', views.landfill, name='index'),
    path('landfill/<int:trash_id>/', views.trash_detail, name='detail'),
    # new route used to show a form and create a cat
    path('landfill/create/', views.TrashCreate.as_view(), name='trash_create'),
    path('landfill/<int:pk>/update/', views.TrashUpdate.as_view(), name='trash_update'),
    path('landfill/<int:pk>/delete/', views.TrashDelete.as_view(), name='trash_delete'),
    path('landfill/<int:trash_id>/add_feeding/', views.add_feeding, name='add_feeding'),

]   
