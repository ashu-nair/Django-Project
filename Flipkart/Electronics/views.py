from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    prod = Product.objects.all()    
    if request.method == 'POST':
        fm = ProductForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = ProductForm()
            return redirect ('success')
    else:
        fm = ProductForm()

        
    return render(request, 'Electronics/home.html', {'prod' : prod, 'fm': fm})

def success(request):
    return render(request, 'Electronics/success.html')

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        fm = ProductForm(request.POST, instance=product)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm = ProductForm(instance=product)

    return render(request, 'Electronics/edit_product.html', {'fm': fm})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'Electronics/delete_product.html', {'product': product})