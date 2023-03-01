from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators  import login_required
from .models import product,order
from .forms import product_form,order_form
from django.contrib import messages

@login_required()
def home(request):
    users=User.objects.all()
    u_count=users.count()
    orders=order.objects.all()
    o_count=orders.count()
    products=product.objects.all()
    p_count=products.count()
    if request.method=='POST':
        form=order_form(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('Home')
    else:
        form=order_form()
    context={
        'u_count':u_count,
        'o_count':o_count,
        'p_count':p_count,
        'form':form,
        'orders':orders,
        'products':products,
    }
    return render(request,'dashboard/index.html',context)

@login_required()
def staff(request):
    items=User.objects.all()
    u_count=items.count()
    prod=product.objects.all()
    p_count=prod.count()
    ordr=order.objects.all()
    o_count=ordr.count()
    context={
        'items':items,
        'u_count':u_count,
        'o_count':o_count,
        'p_count':p_count,
    }
    return render(request,'dashboard/staff.html',context)

@login_required()
def Product(request):
    if request.method=='POST':
        form_data=product_form(request.POST)
        if form_data.is_valid():
            form_data.save()
            name=form_data.cleaned_data.get('name')
            messages.success(request,f'{name} is added') 
            return redirect('dash-product')
    else:
        item=product.objects.all()
        p_count=item.count()
        ordr=order.objects.all()
        o_count=ordr.count()
        stf=User.objects.all()
        u_count=stf.count()
        form=product_form()
        context={
            'items':item,
            'form':form,
            'u_count':u_count,
            'o_count':o_count,
            'p_count':p_count,
        }
        return render(request,'dashboard/product.html',context)

@login_required()
def Order(request):
    item=order.objects.all()
    o_count=item.count()
    stf=User.objects.all()
    u_count=stf.count()
    prod=product.objects.all()
    p_count=prod.count()
    context={
        'items':item,
        'u_count':u_count,
        'o_count':o_count,
        'p_count':p_count,
    }
    return render(request,'dashboard/order.html',context)
# Create your views here.
