from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'menu/home.html', {'products': products})

#def product_detail(request, slug):
    #product = get_object_or_404(Product, slug=slug)
    #return render(request, 'menu/products/detail.html', {'product': product} )


#def category_list(request, category_slug=None):
    #category = get_object_or_404(Category, slug=category_slug)
    #products = Product.objects.filter(category=category)
    #return render(request, 'menu/products/category.html', {'category': category, 'products': products})
