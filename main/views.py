from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from main.models import *
from .form import OrderForm
from .filters import OrderFilter


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
               'total_customers':total_customers, 'delivered':delivered,
               'total_orders':total_orders, 'pending':pending}

    return render(request, 'home.html', context)


def products(request):
    products = Product.objects.all()

    context = {'products' : products}
    return render(request, 'products.html', context)


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs


    context = {'customer' : customer, 'orders' : orders,
               'order_count':order_count, 'myFilter':myFilter}
    return render(request, 'customer.html', context)


def status(request):
    return render(request, 'status.html')


def createOrder(request, pk):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'order_form.html', context)


def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'delete.html', context)
