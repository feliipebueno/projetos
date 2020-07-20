from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'shop/shop.html')

def handler500(request, exception):
    return render(request, '500.html')