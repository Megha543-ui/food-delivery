from django.shortcuts import render
from food.models import SignupUser
from django.contrib.auth.hashers import make_password
from food.models import Payment
from food.models import Contact
from django.contrib.auth.hashers import check_password

# Create your views here.

def index(request):
    return render(request,'food/index2.html')
def login2(request):
    if request.method =="POST":
        un=request.POST.get('uname')
        pw=request.POST.get('psw1')
        user_exist = SignupUser.objects.filter(username=un).exists()
        if user_exist:
            user = SignupUser.objects.get(username=un)
            stored_psw1 =user.password
            chkpwd = check_password(pw,stored_psw1)
            if chkpwd:
                context = {'msg':'username & password Matched !'}
                return render(request,'food/index2.html',context)
            else:
                context={'msg':'wrong Username or Password'}
                return render(request,'food/login2.html',context)
        else:
            context={'msg':f'User {un} does not exist !'}
            return render(request,'food/login2.html',context)
    else:
        return render(request,'food/login2.html')
def menu2(request):
    return render(request,'food/menu2.html')
def contact2(request):
    if request.method == "POST":
        mq =request.POST.get('myQuery')
        mn =request.POST.get('myName')
        me =request.POST.get('myEmail')
        mp =request.POST.get('myPhone')
        eg=request.POST.get('eligible')    
        mg =request.POST.get('mesg')
        

        user_exist = Contact.objects.filter(myName=mn)
        if user_exist:
            context = {'msg':'user already exist !'}
            return render(request,'food/contact2.html',context)
        else:
            # print("++++>>")
            data = Contact(
                myQuery = mq,
                myName =mn,
                myEmail =me,
                myPhone=mp,
                eligible=eg,
                mesg=mg)
                
                
            data.save()
            context ={'msg':'user REGISTER Successfully !'}
            return render(request,'food/contact2.html',context)
        
    else:
        return render(request,'food/contact2.html')
def payment2(request):
    if request.method == "POST":
        fn =request.POST.get('Fullname')
        em =request.POST.get('Email')
        Ad =request.POST.get('Address')
        ct =request.POST.get('City')
        zc=request.POST.get('Zipcode')    
        cn =request.POST.get('Cardnumber')
        em =request.POST.get('Expmonth')
        cv =request.POST.get('Cvv')

        user_exist = Payment.objects.filter(Fullname=fn)
        if user_exist:
            context = {'msg':'user already exist !'}
            return render(request,'food/payment2.html',context)
        else:
            # print("++++>>")
            data = Payment(
                Fullname = fn,
                Email =em,
                Address =Ad,
                City=ct,
                Zipcode=zc,
                Cardnumber=cn,
                Expmonth=em,
                Cvv=cv)
                
            data.save()
            context ={'msg':'user REGISTER Successfully !'}
            return render(request,'food/payment2.html',context)
        
    else:
        return render(request,'food/payment2.html')
def forgotpassword2(request):
    return render(request,'food/forgotpassword2.html')
def signup2(request):
    if request.method == "POST":
        un =request.POST.get('name')
        em =request.POST.get('email')
        pn =request.POST.get('pno')
        Ad =request.POST.get('Address')
        p1 =request.POST.get('psw1')    
        p2 =request.POST.get('psw2')

        user_exist = SignupUser.objects.filter(username=un)
        if user_exist:
            context = {'msg':'user already exist'}
            return render(request,'food/signup2.html',context)
        else:
            # print("++++>>")
            data = SignupUser(
                username = un,
                email =em,
                phonenumber =pn,
                Address=Ad,
                password= make_password(p1),
                reenterpassword=make_password(p2))
            data.save()
            context ={'msg':'user REgistered Successfully'}
            return render(request,'food/signup2.html',context)
        
    else:
         return render(request,'food/signup2.html')
def about2(request):
    return render(request,'food/about2.html') 
def ourblog2(request):
    return render(request,'food/ourblog2.html')    
    
