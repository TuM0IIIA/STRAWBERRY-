from django.shortcuts import render,redirect
from django.views.generic.base import View
from shop.models import Product
from .forms import ContactForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template



def about(request):
    return render(request, 'about.html')  # just link to the about page
# -------------------------------------------------------------

def shop_index(request):  # for index we use shop_single on the url's page

    products = Product.objects.all()  # variable for all products
   # print(len(products))
    context = {
        # we use "product_index" as a link name on the page index.html
        "shop_index": products,
    }
    return render(request, 'index.html', context)
#-------------------------------------------------------------


def shop_single(request):  # same as the previous one

    products = Product.objects.all()
   # print(len(products))
    context = {
        "product_single": products,
    }
    return render(request, 'single_product.html', context)
#-------------------------------------------------------------

def shop_products(request):  # same as the previous one

    products = Product.objects.all()
   # print(len(products))
    context = {
        "product_val": products,
    }
    return render(request, 'products.html', context)
#----------------------------------------------------------------
def product_big_box(request):  # same as the previous one

    products = Product.objects.all()
   # print(len(products))
    context = {
        "product_big_box": products,
    }
    return render(request, 'big_box.html', context)
#----------------------------------------------------
def product_boxes(request):  # same as the previous one

    products = Product.objects.all()
   # print(len(products))
    context = {
        "product_boxes": products,
    }
    return render(request, 'boxes.html', context)
#----------------------------------------------------------
def product_bouquets(request):  # same as the previous one

    products = Product.objects.all()
   # print(len(products))
    context = {
        "product_bouquets": products,
    }
    return render(request, 'bouquets.html', context)
#--------------------------------------------------------

def post_contacts(request):
    context = {}
    if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
           send_message(form.cleaned_data['the_name'], form.cleaned_data['e_mail'], form.cleaned_data['topic'], form.cleaned_data['message'])
           context = {'well done' : 1}

    else:
       form = ContactForm(request.POST)
    context['form'] = form
    return render(request,'contact.html',context=context)

def send_message(the_name, e_mail, topic, message ):
    text = get_template('e_mail.html')
    context = {'name' :the_name, 'email': e_mail,'topic': topic, 'text': message }
    subject = 'Message from the user'
    from_who_email = 'from@example.com'
    text_content = text.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_who_email, ['someone@example.com'])
    msg.send()

