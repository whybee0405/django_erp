from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Inventory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def login_page(request):
    return render(request, 'auth/login.html')

def index(request):
    latest_inventory_list = Inventory.objects.order_by('id')
    context = {'latest_inventory_list':latest_inventory_list}
    return render(request, 'index.html', context)

def view_inventories(request): #Renders a list of inventories in View Inventories view
    latest_inventory_list = Inventory.objects.order_by('id')
    context = {'latest_inventory_list':latest_inventory_list}
    return render(request, 'inventories/view_inventories.html', context)

def edit_inventory(request, inventory_id): #Renders Edit Inventory form view
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    return render(request, 'inventories/edit_inventory.html', {'inventory':inventory})

def update_inventory(request, inventory_id): #Function to update inventory depending on the request on the front end form. Redirect back to inventories view
    # TODO : Proper error handling needs to be done
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    inventory.sku = request.POST['sku']
    inventory.category_1 = request.POST['category_1']
    inventory.category_2 = request.POST['category_2']
    inventory.category_3 = request.POST['category_3']
    inventory.attribute_1 = request.POST['attribute_1']
    inventory.attribute_2 = request.POST['attribute_2']
    inventory.attribute_3 = request.POST['attribute_3']
    inventory.description = request.POST['description']
    inventory.retail_price = request.POST['retail_price']
    inventory.supplier_name = request.POST['supplier_name']
    inventory.backorder_qty = request.POST['backorder_qty']
    inventory.stock_available = request.POST['stock_available']
    inventory.save()
    return HttpResponseRedirect(
            reverse('erp_system:view_inventories')
        )
    
def delete_inventory(request, inventory_id): #Function to delete a selected inventory item
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    inventory.delete()
    return HttpResponseRedirect(
            reverse('erp_system:view_inventories')
        )
    
def add_inventory(request): #Function to insert a new inventory record
    return render(request, 'inventories/add_inventory.html')

def reg_inventory(request):
    inventory = Inventory(
    sku = request.POST['sku'],
    category_1 = request.POST['category_1'],
    category_2 = request.POST['category_2'],
    category_3 = request.POST['category_3'],
    attribute_1 = request.POST['attribute_1'],
    attribute_2 = request.POST['attribute_2'],
    attribute_3 = request.POST['attribute_3'],
    description = request.POST['description'],
    retail_price = request.POST['retail_price'],
    supplier_name = request.POST['supplier_name'],
    backorder_qty = request.POST['backorder_qty'],
    stock_available = request.POST['stock_available'],
    )
    inventory.save()
    return HttpResponseRedirect(
        reverse('erp_system:view_inventories')
    )

def auth_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('erp_system:login_page')
        )
    else:
        login(request,user)
        return HttpResponseRedirect(
            reverse('erp_system:index')
        )

def view_users(request):
    latest_users_list = User.objects.order_by('id')
    context = {'latest_users_list':latest_users_list}
    return render(request, 'config/users.html', context)

def add_user(request):
    return render(request, 'config/user_add.html')

def reg_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username=username, password=password)
    user.save()
    return HttpResponseRedirect(
        reverse('erp_system:view_users')
    )

def edit_user(request):
    pass

def delete_user(request):
    pass
