from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def category(request):
    return render(request, 'index.html', {})


def product_detail(request, id):
    return render(request, 'index.html', {})


def product_list(request, id):
    return render(request, 'index.html', {})


def product(request, id):
    return render(request, 'index.html', {})



