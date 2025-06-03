from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Product, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'rating']

def product_list(request):
    products = Product.objects.all()
    return render(request, 'reviews/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ReviewForm()

    return render(request, 'reviews/product_detail.html', {
        'product': product,
        'form': form,
        'reviews': reviews
    })
