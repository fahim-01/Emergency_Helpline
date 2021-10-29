#from django.http import HttpResponse
from django.shortcuts  import render,HttpResponse,redirect
from .models import Contact
# Create your views here.
def index(request):
    return  render(request, 'homepage/home.html')


def service(request):
    return  render(request, 'homepage/service.html')
def contact(request):
    thank =False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'homepage/contact.html', {'thank': thank})



def about(request):
    return  render(request, 'homepage/about.html')
def post(request):
    return  render(request, 'homepage/post.html')

def signup(request):
    return  render(request, 'homepage/signup.html')