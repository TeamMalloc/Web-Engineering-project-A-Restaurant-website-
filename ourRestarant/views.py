from django.shortcuts import render,HttpResponse,redirect
from django.template.response import TemplateResponse
from ourRestarant.models import ThaiFood,IndianFood,DumplingsFood,ContinentalFood,Book_A_Table,qualification
from django.core.files import File

from django.contrib import messages

# for email
from email.message import EmailMessage
import ssl
import smtplib

# Create your views here.
def index(request):
    user_name = "admin123"
    pass_word = "admin1981"
    if request.method == "POST":
        if request.POST.get("form_type") == 'formOne':
            na = request.POST.get("name")
            email = request.POST.get("email")
            ph = request.POST.get("phone")
            da = request.POST.get("date")
            ti = request.POST.get("time")
            peop = request.POST.get("people")
            messss = request.POST.get("message")

            BookATable = Book_A_Table(name=na,email=email,phone=ph,date=da,time=ti,people=peop,messagess=messss)
            BookATable.save()

            # send confirmation mail for reservation table
            email_sender = 'sa3518548@gmail.com'
            email_password = 'pziggqxkwggxtopt'

            email_receiver = email
            subject = "hello "+na+"! check your Reservation status."
            body = "Hi "+ na+ "! your reservation is booked.\nthanking you team malloc to visit our BiyeBari website.\nwe are waiting for you util "+ti+" "+da+"."

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
                smtp.login(email_sender,email_password)
                smtp.sendmail(email_sender,email_receiver,em.as_string())
            
            messages.success(request,"Your reservation is booked, we send a mail on your mail address. Please check it out and Thank you!")
        
        if request.POST.get("form_type") == 'formTwo':
            nam = request.POST.get("name")
            qua = request.POST.get("qualification")
            ra = request.POST.get("rate")
            me = request.POST.get("message")

            qualifi = qualification(Name=nam,qualification=qua,rate=ra,messagesss=me)
            qualifi.save()
        
        else:
            uname = request.POST.get("Username")
            pas = request.POST.get("password")
            if (user_name == uname) and (pass_word == pas):
                return TemplateResponse(request, 'Yummy/adminP.html',{"pos":Book_A_Table.objects.all()})
            else:
                messages.error(request,"Username or Password incorrect! Please try again.")
                return redirect('home')


    test = qualification.objects.all()
    return render(request,'Yummy/index.html',{"test":test})
    #return HttpResponse("this is home page r")

def thai(request):
    TypeFood1 = "Appetizers"
    TypesFood = "Salads"
    TypesFood2 = "Soups"
    TypesFood3 = "Chicken"
    TypesFood4 = "Beef"
    TypesFood5 = "Fish"
    objThaiFood = ThaiFood.objects.all()
    return render(request,'Yummy/thai.html',{"tf":objThaiFood,"sa":TypesFood,"ap":TypeFood1,"so":TypesFood2,"chi":TypesFood3,"bef":TypesFood4,"fi":TypesFood5})

def indian(request):
    food1 = "Tandoor Delights"
    food2 = "Breads"
    food3 = "Rice"

    objindianfood = IndianFood.objects.all()

    return render(request,'Yummy/indian.html',{"inf":objindianfood,"td":food1,"br":food2,"ri":food3})

def dumplings(request):
    return render(request,'Yummy/dumplings.html')

def continental(request):
    return render(request,'Yummy/continental.html')

def adminP(request,name):
    if request.method == "post":
        pi = Book_A_Table.objects.get(name)
        pi.delete()
        return redirect('home')
    return render(request,'Yummy/adminP.html')

