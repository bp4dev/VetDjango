from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def main(request):
     
    return render(request, 'main.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone_number = request.POST['phone-number']
        email = request.POST['email']
        message = request.POST['message']

        #sending email
        send_mail(
                name,#subject
                message,#message
                email,#from
                ['test@email.com'],#to
                )

        return render(request, 'contact.html', {'name': name})

    else:
        return render(request, 'contact.html', {})

def gallery(request):
     
    return render(request, 'gallery.html', {})

def about(request): 
     
    return render(request, 'about.html', {})

