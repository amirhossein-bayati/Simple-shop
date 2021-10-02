from django.contrib import messages
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import *
from .forms import *
from .filters import *

from .decorators import unauthenticated_user, allowed_users

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group


@allowed_users(allowed_roles=['admin', 'customer'])
def home(request):
	customers = Customer.objects.all()
	orders = Order.objects.all()
	total_orders = orders.count()
	total_orders_delivered = orders.filter(status="delivered").count()
	total_orders_pending = orders.filter(status="pending").count()


	context = {
		'customers': customers,
		'oerders': orders,
		'total_orders': total_orders,
		'total_orders_delivered': total_orders_delivered,
		'total_orders_pending': total_orders_pending,
	}
	return render(request, 'accounts/dashboard.html', context)


def products(request):
	products = Product.objects.all()
	context = {
		'products': products,
	}
	return render(request, 'accounts/products.html', context)


def customer(request, user_id):
	customer = Customer.objects.get(id=user_id)
	customer_total_orders = customer.order_set.count()
	customer_order = customer.order_set.all()

	filters = OrderFilter(request.GET, queryset=customer_order)
	customer_order = filters.qs

	context = {
		"customer": customer,
		'customer_total_orders': customer_total_orders,
		'customer_order': customer_order,
		'filters': filters,
	}
	return render(request, 'accounts/customer.html', context)


def userPage(request):
	orders = request.user.customer.order_set.all()
	total_orders = orders.count()
	total_orders_delivered = orders.filter(status="delivered").count()
	total_orders_pending = orders.filter(status="pending").count()

	context = {
		'oerders': orders,
		'total_orders': total_orders,
		'total_orders_delivered': total_orders_delivered,
		'total_orders_pending': total_orders_pending,
	}
	return render(request, 'accounts/user.html', context)


def createOrder(request):
	# customer = Customer.objects.get(id=user_id)
	form = OrderForm()
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
	context = {
		'form': form
	}
	return render(request, 'accounts/order_form.html', context)


def updateOrder(request, order_id):
	order = Order.objects.get(id=order_id)
	form = OrderForm(instance=order)

	if request.method == "POST":
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect("/")
	context = {
		'form': form,
	}
	return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, order_id):
	order = Order.objects.get(id=order_id)
	order.delete()
	return redirect("/")


@unauthenticated_user
def register(request):
	form = CreateUserForm()

	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name='customer')
			user.groups.add(group)

			Customer.objects.create(
				user=user,
				name=user.username
			)
			return redirect('login')
	context = {
		'form': form,
	}
	return render(request, "accounts/register.html", context)


@unauthenticated_user
def loginPage(request):
	if request.method == "POST":
		# print(request.POST)
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('customer', args=[str(user.id)]))
			else:
				messages.error(request, "User is not active")
		else:
			messages.error(request, "Username Or password is Incorrect")
	context = {
	}
	return render(request, 'accounts/login.html', context)


def logoutPage(request):
	logout(request)
	return redirect('login')

def accountSetting(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == "POST":
		form = CustomerForm(request.POST, request.FILES, instance=customer)

		if form.is_valid():
			form.save()
			return redirect("/")
	context = {
		'form': form,
	}
	return render(request, 'accounts/account_setting.html', context)