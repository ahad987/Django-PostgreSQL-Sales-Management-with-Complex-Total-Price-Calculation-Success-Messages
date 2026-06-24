# Sales Management Application

A lightweight Django web application designed to log product sales, dynamically calculate total pricing metrics on the backend, and view structured sales performance reports. This project completely bypasses standard `Django Forms` to handle pure HTML form submissions directly through backend views, implementing custom calculations and Django’s messages framework.

## 🚀 Features

- **Manual Math Engine**: Total price calculated via backend views utilizing the exact specification formula:
  $$\text{Total Price} = (\text{Unit Price} \times \text{Quantity}) - \left((\text{Unit Price} \times \text{Quantity}) \times \frac{\text{Discount \%}}{100}\right) + \left((\text{Unit Price} \times \text{Quantity}) \times \frac{\text{Tax \%}}{100}\right)$$
- **Form-Free Processing**: Handles raw HTML `<form>` requests directly via standard HTTP POST handling methods.
- **Dynamic Flash Notifications**: Built-in system messages notifying users with success or warning alerts during crucial app actions (e.g., system logins or logging new sales).
- **Comprehensive Reports**: Tabular list of entries reporting complete data context including calculated grand totals.

---

## 📂 Project Directory Structure

```text
Sales_Management_Project/
├── manage.py
├── core_project/                   # Project settings folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── sales/                          # Application folder
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── sales/
            ├── base.html           # Main boilerplate (contains flash messages block)
            ├── add_sale.html       # Raw HTML entry form
            └── sale_list.html      # Reports and management table
```
🛠️ Code Architecture
1. Database Model (sales/models.py)
Defines the structure for saving specific sales records.

```
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    
    def __str__(self):
        return self.username
    

class CategoryModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class SalesModel(models.Model):
    product_name = models.CharField(max_length=200, null=True, blank=True)
    
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name='category_info',
        null=True,
        blank=True
        )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    tax_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    sale_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name
```
2. Backend Processing (sales/views.py)
Processes database additions manually, calculates metrics without Django Forms, and triggers user messages.
```
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
```
⚡ Setup Instructions
1. Clone the Repository:
```
git clone [https://github.com/your-username/sales-management.git](https://github.com/your-username/sales-management.git)
cd sales-management
```
2. Initialize Database Tables:
```
python manage.py makemigrations
python manage.py migrate
```
3. Start the Development Server:
```
python manage.py runserver
```
Open http://127.0.0.1:8000/sales/ inside your preferred browser.

* * *
## 👤 Contact

**Abdul Ahad Chowdhury**
- GitHub: [@ahad987](https://github.com/ahad987)
- Email: [ahad987@gmail.com](mailto:ahad987@gmail.com)
- **LinkedIn:** [Your Name / Profile](https://www.linkedin.com/in/ahad1987/)
- **Facebook:** [ahadc](https://facebook.com)
- **WhatsApp:** [Message on WhatsApp](https://wa.me)
- **Phone:** [+880 1812148778](tel:+8801812148778)
- Project: [https://github.com/ahad987/Django-PostgreSQL-Sales-Management-with-Complex-Total-Price-Calculation-Success-Messages](https://github.com/ahad987/Django-PostgreSQL-Sales-Management-with-Complex-Total-Price-Calculation-Success-Messages)

---
⭐ **Feel free to star this repository if you find my learning track useful!**
