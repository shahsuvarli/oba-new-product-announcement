from django.shortcuts import render, redirect
from .models import *
from .forms import *



# Create your views here.

def home_view(request):
	context = {}
	return render(request, 'home.html', context)


def process_view(request):
	table = ProcessFlow.objects.all()
	context = {'table':table}
	return render(request, 'process.html', context)


def create_product_view(request):
	form = ProductForm(request.POST)
	if request.method == 'POST':
		form = ProductForm(request.POST or None)
		if form.is_valid():
			form = form.save(commit=False)
			form.created_by = request.user
			form.pending = form.created_by
			form.save()
			return redirect('product')
	context = {'form':form}
	return render(request, 'create-product.html', context)


def update_product_view(request, pk):
	product = Product.objects.get(id=pk)
	form = ProductForm(request.POST or None, instance=product)
	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			form = form.save(commit=False)
			sends_to = ProcessFlow.objects.get(display_name=request.user)._meta.get_field('sends_to_id')
			print(sends_to)
			form.pending = sends_to
			form.save()
			return redirect('product')
	context = {'form':form}
	return render(request, 'update-product.html', context)


def confirm_product_view(request, pk):
	product = Product.objects.get(id=pk)
	if request.method == 'POST':
		person_id = ProcessFlow.objects.get(display_name=product.pending).__dict__['sends_to_id_id']
		new_pending = ProcessFlow.objects.get(id=person_id).__dict__['display_name']
		product.pending = new_pending
		product.save()
		return redirect('product')
	context = {'product':product}
	return render(request, 'confirm-product.html', context)


def product_view(request):
	product = Product.objects.all()
	context = {'product':product}
	return render(request, 'product.html', context)




def blog_view(request):
	pass















