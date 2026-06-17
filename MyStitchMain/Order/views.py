from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm, UpperBodyForm, LowerBodyForm
from cloths.models import UpperBody, LowerBody


def orderview(request):
    orders = Order.objects.select_related('customer', 'upperBody', 'lowerBody').all()
    return render(request, 'Order/orders.html', {'orders': orders})


def oderdetailview(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'Order/orderdetails.html', {'order': order})


@login_required
def orderAdd (request):
    order_form = OrderForm()
    upper_form = UpperBodyForm(prefix='upper')
    lower_form = LowerBodyForm(prefix='lower')

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        upper_form = UpperBodyForm(request.POST, prefix='upper')
        lower_form = LowerBodyForm(request.POST, prefix='lower')

        add_upper = request.POST.get('add_upper') == 'on'
        add_lower = request.POST.get('add_lower') == 'on'

        upper_valid = upper_form.is_valid() if add_upper else True
        lower_valid = lower_form.is_valid() if add_lower else True

        if order_form.is_valid() and upper_valid and lower_valid:
            order = order_form.save(commit=False)

            if add_upper:
                upper = upper_form.save()
                order.upperBody = upper

            if add_lower:
                lower = lower_form.save()
                order.lowerBody = lower

            order.save()
            return redirect('oderDetailView', pk=order.pk)

    return render(request, 'Order/addorder.html', {
        'order_form': order_form,
        'upper_form': upper_form,
        'lower_form': lower_form,
    })


@login_required
def orderedit(request, pk):
    order = get_object_or_404(Order, pk=pk)

    upper_instance = order.upperBody
    lower_instance = order.lowerBody

    order_form = OrderForm(instance=order)
    upper_form = UpperBodyForm(instance=upper_instance, prefix='upper')
    lower_form = LowerBodyForm(instance=lower_instance, prefix='lower')

    if request.method == 'POST':
        order_form = OrderForm(request.POST, instance=order)
        upper_form = UpperBodyForm(request.POST, instance=upper_instance, prefix='upper')
        lower_form = LowerBodyForm(request.POST, instance=lower_instance, prefix='lower')

        add_upper = request.POST.get('add_upper') == 'on'
        add_lower = request.POST.get('add_lower') == 'on'

        upper_valid = upper_form.is_valid() if add_upper else True
        lower_valid = lower_form.is_valid() if add_lower else True

        if order_form.is_valid() and upper_valid and lower_valid:
            order = order_form.save(commit=False)

            if add_upper:
                upper = upper_form.save()
                order.upperBody = upper
            else:
                # If unchecked and there was an existing upper body, remove the link
                # (don't delete the object to be safe)
                order.upperBody = None

            if add_lower:
                lower = lower_form.save()
                order.lowerBody = lower
            else:
                order.lowerBody = None

            order.save()
            return redirect('oderDetailView', pk=order.pk)

    return render(request, 'Order/editorder.html', {
        'order': order,
        'order_form': order_form,
        'upper_form': upper_form,
        'lower_form': lower_form,
        'has_upper': upper_instance is not None,
        'has_lower': lower_instance is not None,
    })


@login_required
def orderdelete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orderview')
    return redirect('orderview')