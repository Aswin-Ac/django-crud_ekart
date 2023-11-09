from django.shortcuts import redirect, render

from customer.models import seller
from eKart_admin.models import Category
from seller.models import Product

# Create your views here.
def seller_home(request):
    newSeller = seller.objects.get(id = request.session['seller'])
    return render(request, 'seller/seller_home.html',{'seller_details':newSeller})

def add_product(request):
    category_list = Category.objects.all()
    message = ''

    if request.method == 'POST':
        product_no = request.POST['product_no']
        product_name = request.POST['product_name']
        description = request.POST['description']
        stock = request.POST['stock']
        price = request.POST['price']
        image = request.FILES['image']
        category = request.POST['category']
        seller1 = request.session['seller']

        # product_exist = Product.objects.filter(product_no = )
        product,created = Product.objects.get_or_create(product_no = product_no, seller = seller1, defaults = {
            'product_no':product_no,
            'product_name':product_name,
            'description':description,
            'stock':stock,
            'price':price,
            'image':image,
            'product_category':Category.objects.get(id =int(category) ),
            'seller':seller.objects.get(id = seller1),
        })
        if created:
            message = 'Product added'
        else:
            message = 'Product already exist'
    context = {'category':category_list,
                   'message':message}
    return render(request, 'seller/add_product.html',context)

def add_category(request):
    return render(request, 'seller/add_category.html')

def view_category(request):
    return render(request, 'seller/view_category.html')

def view_products(request):
    products = Product.objects.filter(seller_id = request.session['seller'])
    return render(request, 'seller/view_product.html',{'products':products})

def profile(request):
    return render(request,'seller/profile.html')

def view_orders(request):
    return render(request,'seller/view_orders.html')

def update_stock(request):
    return render(request,'seller/update_stock.html')

def order_history(request):
    return render(request,'seller/order_history.html')

def change_password(request):
    pwd_status = ''
    if request.method == "POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        try:
            if len(new_password) > 8 :
                if new_password == confirm_password :
                    new_Seller = seller.objects.get(id = request.session['seller'])
                    if new_Seller.password == old_password:
                        new_Seller.password = new_password
                        new_Seller.save()
                        pwd_status = 'Password changed'
                    else:
                        pwd_status = 'incorrect password !'
                else:
                    pwd_status = 'Password does not match'
            else:
                pwd_status = 'Password should have minimum 8 characters'
        except:
            pwd_status = 'invalid password'
        
    return render(request,'seller/change_password.html',{'msg':pwd_status})

def seller_logout(request):
    del request.session['seller']
    request.session.flush()
    return redirect('customer:seller_login')