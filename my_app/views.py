from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import *
from django.core.mail import send_mail



# Create your views here.

class HomeView(ListView):
    model = Product
    template_name = 'index.html'
    

def about(request):
    context = {}
    return render(request, 'about.html', context)

def service(request):
    context = {}
    return render(request, 'service.html', context)


class ProductsView(ListView):
    model = Product
    template_name = 'shop.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        message_body = f'''Hey, I am {name}.My phone number is {phone}.

        {message}
        '''
        # send an email 
        send_mail(
            f'Message from {name} ',
            message_body,
            email,
            ['testerwebsite007@gmail.com'],
            fail_silently=False,
        )
        context = {'name':name}
    else:
        context = {}
    return render(request, 'contact.html', context)
