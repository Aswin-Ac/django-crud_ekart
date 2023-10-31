from django.shortcuts import redirect, render

from customer.models import seller

# Create your views here.
def seller_home(request):
    newSeller = seller.objects.get(id = request.session['seller'])
    return render(request, 'seller/seller_home.html',{'seller_details':newSeller})

def add_product(request):
    return render(request, 'seller/add_product.html')

def add_category(request):
    return render(request, 'seller/add_category.html')

def view_category(request):
    return render(request, 'seller/view_category.html')

def view_products(request):
    return render(request, 'seller/view_product.html')

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

# def seller_logout(request):
#     del request.session['seller']
#     request.session.flush()

#     return redirect('seller:seller_home')