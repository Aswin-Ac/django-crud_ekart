from django.shortcuts import render,redirect
from random import randint
from django.conf import settings
from django.core.mail import send_mail

from customer.models import Customer,seller
# from .models import Customer
# Create your views here.


def customer_home(request):
    customer = Customer.objects.get(id = request.session['customer'])
    return render(request, 'customer/customer_home.html',{'customer_details':customer})


def store(request):
    return render(request, 'customer/store.html')


def product_detail(request):
    return render(request, 'customer/product_detail.html')


def cart(request):
    return render(request, 'customer/cart.html')


def place_order(request):
    return render(request, 'customer/place_order.html')


def order_complete(request):
    return render(request, 'customer/order_complete.html')


def dashboard(request):
    return render(request, 'customer/dashboard.html')


def seller_register(request):
    status = False
    msg = ''
    if request.method == "POST":
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        company_name = request.POST['cname']
        bank_name = request.POST['bname']
        branch_name = request.POST['bbranch']
        account_number = request.POST['accnum']
        ifsc = request.POST['ifsccode']
        seller_image = request.FILES['picture']

        seller_exist = seller.objects.filter(email = email)
        if not seller_exist : 
            new_seller = seller(
                first_name = f_name,
                last_name = l_name,
                email = email,
                gender = gender,
                city = city,
                country = country,
                company_name = company_name,
                bank_name = bank_name,
                bank_branch = branch_name,
                account_number = account_number,
                ifsc = ifsc,
                seller_picture = seller_image, 
            )

            new_seller.save()
            msg = 'Account created successfully'
            status = True
        else :
            msg = 'Account already exist'

    return render(request, 'customer/seller_register.html',{'message' : msg})

def seller_login(request):
    msg = ''
    if request.method == 'POST':
        s_username = request.POST['sellerid']
        s_password = request.POST['password']

        newSeller = seller.objects.filter(login_id = s_username, password = s_password)

        if newSeller.exists():
            request.session['seller'] = newSeller[0].id
            request.session['seller_name']=newSeller[0].first_name+''+newSeller[0].last_name
            return redirect('Seller:seller_home')
        else:
            msg = 'Incorrect Password or Username'
    return render(request, 'customer/seller_login.html',{'message':msg})


def customer_signup(request):
    msg = ""
    status = False
    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lastname'] 
        email = request.POST['email'] 
        gender = request.POST['gender'] 
        city = request.POST['city'] 
        country = request.POST['country']
        password = request.POST['password']

        customer_exist = Customer.objects.filter(email = email).exists()

        if not customer_exist:
            customer = Customer(
                first_name = f_name,
                last_name = l_name,
                email = email,
                gender = gender,
                city = city,
                country = country,
                password = password
                )
        
            customer.save()
            msg = 'Registration successfull'
            status = True
        else:
            msg = 'Already registered'
    return render(request, 'customer/customer_signup.html',{'message':msg,'status':status})


def customer_login(request):
    msg = ''
    if request.method == 'POST':
        c_mail = request.POST['email']
        c_password = request.POST['password']

        customer = Customer.objects.filter(email = c_mail, password = c_password)

        if customer.exists():
            request.session['customer'] = customer[0].id
            return redirect('customer:customer_home')
        else:
            msg = 'Incorrect Password or Username'
    return render(request, 'customer/customer_login.html',{'message':msg})


def forgot_password_customer(request):
    return render(request, 'customer/forgot_password_customer.html')


def forgot_password_seller(request):
    return render(request, 'customer/forgot_password_seller.html')