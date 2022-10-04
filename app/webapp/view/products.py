from django.shortcuts import get_object_or_404, render, redirect

from webapp.forms import ProductForm
from webapp.models import Product


def errors_test(form):
    errors = {}
    if not form.data['title']:
        errors['title'] = 'Title should not be empty!'
    if not form.data['balance']:
        errors['balance'] = 'Balance should not be empty!'
    if not form.data['price']:
        errors['price'] = 'Price should not be empty!'
    if int(form.data['balance']) < 1:
        errors['balance'] = 'Balance must be greater than 1!'
    return errors


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.category = product.get_category_display()
    return render(request, 'product.html', context={'product': product})


def create_view(request):
    form = ProductForm()
    if request.method == "GET":
        return render(request, 'create.html', context={'choices': Product.CHOICES, 'form': form})
    form = ProductForm(request.POST)
    errors = errors_test(form)
    if errors:
        product = {
            'title': form.data['title'],
            'description': form.data['description'],
            'photo': form.data['photo'],
            'category': form.data['category'],
            'balance': form.data['balance'],
            'price': form.data['price']
        }
        return render(request, 'create.html', context={'product': product, 'errors': errors, 'choices': Product.CHOICES})
    if not form.is_valid():
        return render(request, 'create.html', context={'choices': Product.CHOICES, 'form': form})
    product = Product.objects.create(**form.cleaned_data)
    return redirect('product', pk=product.pk)


def edit_view(request, pk):
    form = ProductForm()
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST)
        errors = errors_test(form)
        if errors:
            product = {
                'pk': product.pk,
                'title': form.data['title'],
                'description': form.data['description'],
                'photo': form.data['photo'],
                'category': form.data['category'],
                'balance': form.data['balance'],
                'price': form.data['price']
            }
            return render(request, 'edit.html',
                          context={'product': product, 'errors': errors, 'choices': Product.CHOICES})
        if form.is_valid():
            product.title = form.cleaned_data['title']
            product.description = form.cleaned_data['description']
            product.photo = form.cleaned_data['photo']
            product.category = form.cleaned_data['category']
            product.balance = form.cleaned_data['balance']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('index')
    return render(request, 'edit.html', context={'product': product, 'form': form, 'choices': Product.CHOICES})


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "confirm_delete.html", context={'product': product})


def confirm_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect("index")

