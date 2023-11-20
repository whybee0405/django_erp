from django.urls import path
from . import views

app_name="erp_system"

urlpatterns = [
    path('', views.login_page, name='login'), # Login page view
    path('index/', views.index, name='index'), # Home page view
    path('view_inventories/', views.view_inventories, name='view_inventories'), # Inventory records view
    path('<int:inventory_id>/edit_inventory/', views.edit_inventory, name='edit_inventory'), # Edit Inventory records view
    path('<int:inventory_id>/update_inventory/', views.update_inventory, name='update_inventory'), # Function to update Inventory records
    path('<int:inventory_id>/delete_inventory/', views.delete_inventory, name='delete_inventory'), # Function to delete Inventory records
    path('add_inventory/', views.add_inventory, name='add_inventory'), # Add/Insert new Inventory view
    path('view_users/', views.view_users, name='view_users'), # System user list view
    path('add_user/', views.add_user, name='add_user'), # Create new system user view
    path('<int:user_id>/edit_user/', views.edit_user, name='edit_user'), #TODO give front-end access to edit users. going to require access layers
    path('<int:user_id>/delete_user', views.delete_user, name='delete_user'), #TODO give front-end access to delete users. going to require access layers
    path('reg_user', views.reg_user, name='reg_user'), # Function to create a new system user
    path('auth_user', views.auth_user, name='auth_user'), # Function to authenticate user into the system
    path('reg_inventory', views.reg_inventory, name='reg_inventory') # Function to insert Inventory records

] 