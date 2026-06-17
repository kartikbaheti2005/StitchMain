from django.shortcuts import redirect, render, get_object_or_404
from .models import Order
from .forms import OrderForm

# Create your views here.
def orderview(request):
    orders = Order.objects.all()
    print("Order count:", orders.count())  # ← add this
    print("Orders:", orders)   
    context = {
        "orders" : orders
    }
    return render(request, 'Order/orders.html', context=context)

def oderdetailview(request, pk):
    order = get_object_or_404(Order, pk=pk)
    context = {
        "order" : order 
    }
    return render(request, 'Order/orderdetails.html', context = context)

def orderAdd(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orderview')
        else:
            print(form.errors)
    else:
        form = OrderForm()

    context = {
        'form' : form
    }

    return render(request, 'Order/addorder.html', context=context)


def orderedit(request, pk):

    return render(request, 'Order/editorder.html')

def orderdelete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('orderview')