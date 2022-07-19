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
    path('landfill/<int:trash_id>/assoc_uses/<int:use_id>/', views.assoc_use, name='assoc_use'),
    path('uses/', views.UseList.as_view(), name='uses_index'),
    path('uses/<int:pk>/', views.UseDetail.as_view(), name='use_detail'),
    path('uses/create/', views.UseCreate.as_view(), name='use_create'),
    path('uses/<int:pk>/update/', views.UseUpdate.as_view(), name='use_update'),
    path('uses/<int:pk>/delete/', views.UseDelete.as_view(), name='use_delete'),
]   
