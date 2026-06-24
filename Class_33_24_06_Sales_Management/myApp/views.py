from django.shortcuts import render, redirect
from myApp.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.utils.html import escape
from django.utils.safestring import mark_safe

def home_view(request):
    
    return render(request, 'home.html')

def sign_up_view(request):
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password == password:
            UserModel.objects.create_user(
                username = username,
                first_name = first_name,
                password = password
            )
            messages.success(request, "Your Account successfully created!...")
            return redirect('sign_in')
        
    
    return render(request, 'sign_up.html')

def signin_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user:
            login(request, user)
            messages.success(request, "You successfully Logd in... ... ... ")
            return redirect('home')
        
        else:
            print('Login ERROR')
    
    return render(request, 'sign_in.html')

@login_required
def logout_page(request):
    logout(request)

    return redirect('sign_in')

@login_required
def add_sale_page(request):
    
    data = CategoryModel.objects.all()
    
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        quantity = int(request.POST.get('quantity'))
        unit_price = float(request.POST.get('unit_price'))
        discount_percent = float(request.POST.get('discount_percent'))
        tax_percent = float(request.POST.get('tax_percent'))
        
        cat_info = CategoryModel.objects.get(id = category)
        
        cal_total_price = (unit_price * quantity) - ((unit_price * quantity) * (discount_percent/100)) + ((unit_price * quantity) * (tax_percent/100))
        
        SalesModel.objects.create(
            product_name = product_name,
            category = cat_info,
            quantity = quantity,
            unit_price = unit_price,
            discount_percent = discount_percent,
            tax_percent = tax_percent,
            total_price = cal_total_price
        )
        # unsafe_string = f"Successfully <b>{product_name}</b> product for new sale! "
        # messages.success(request, escape(unsafe_string))
        messages.success(request,mark_safe(f"Successfully <b>{product_name}</b> product for new sale! "))
        return redirect('sale_list')
        
        #print(product_name, category, quantity, unit_price, discount_percent, tax_percent)

    return render(request, 'add_sale.html', {'data':data})

@login_required
def sale_list_page(request):    
    
    data = SalesModel.objects.all()

    return render(request, 'sale_list.html', {'data': data})