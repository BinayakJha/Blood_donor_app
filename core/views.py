import email
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from numpy import logical_not
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from requests import request
from .forms import *
from django.core.mail import EmailMessage, send_mail
# Create your views here.
class Tabs:
    def index(self):
        blood_request_list = Blood_form.objects.all()
        context = {'blood_request_list': blood_request_list}
        return render(self, 'blood_requests.html', context)
    def blood_requests(self):
        return render(self, 'blood_requests.html')
    def profile(self):
        return render(self, 'profile.html')
    def login(self):
        return render(self, 'login.html')
    def register(self):
        return render(self, 'register.html')
    def blood_request_form(self):
        form  =  Blood_Donor_Form()
        context = {'form': form}
        return render(self, 'blood_request_form.html', context)

class Authentication:
    #---------------------------------------------------------------------------------
    # signup function
    #---------------------------------------------------------------------------------
    def signup(self):
        if self.method != 'POST':
            return redirect('register')
        username = self.POST['email']
        email = self.POST['username']
        password = self.POST['password']
        confirm_password = self.POST['confirm_password']
        first_name = self.POST['fname']
        last_name = self.POST['lname']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(self, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(self, 'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(self, 'User created')
                return redirect('login')
        else:
            messages.info(self, 'Password not matching')
            return redirect('register')
    # ------------------------------------------------------------------------------------
    # login function
    # ------------------------------------------------------------------------------------
    def login(self):
        if self.method != 'POST':
            return redirect('login')
        email = self.POST['email']
        password = self.POST['password']
        user = authenticate(self, username=email, password=password)
        if user is not None:
            login(self, user)
            return redirect('/')
        else:
            messages.info(self, 'Invalid credentials')
            return redirect('/login')
    # ------------------------------------------------------------------------------------
    # logout function
    # ------------------------------------------------------------------------------------
    def logout(self):
        logout(self)
        return redirect('/')
    
class BloodRequests:
    def form_function(request):
        if request.method == "POST":
            form = Blood_Donor_Form(request.POST, request.FILES)
            if form.is_valid():
                print("valid")
                form.save()
                # send email to the user that the request has been received and we will contact you if someone contacts you
                email_send = EmailMessage(
                    'Blood Request',
                    'Your blood request has been received. We have already sent the request to all the active donors. We will contact if someone accepts your request.',
                    settings.EMAIL_HOST_USER,
                    [request.POST['email']],
                    headers = {'Reply-To': settings.EMAIL_HOST_USER}
                )
                email_send.send()
                # now to all the donors
                email_list = User.objects.all()
            # get the email addresses from the database
                for em in email_list:
                    try:
                        print(em.username)
                        email_send_2 = EmailMessage(
                        'Blood Request',
                        'New Blood Request ! Please go to http://localhost:2500 to see the request.',
                        settings.EMAIL_HOST_USER,
                        [em.email],
                        reply_to=[settings.EMAIL_HOST_USER],
                        headers = {'Message-ID': 'foo'},
                        )
                        email_send_2.sub_type = 'html'
                        email_send_2.send()
                    except:
                        print("error")
                        
                return JsonResponse({'status': 'success'})
            else:
                print("Error")
        else:
            print("Error")
            return HttpResponseRedirect('/')

    def send_info_email(request):
        # get the logged in user info
        user = request.POST['use']
        user = int(user)
        user_info = User.objects.get(id=user)

        # print(use)
        email2 = Blood_form.objects.get( id = request.POST['requester_id'])
        # this email will be send to the requester email
        email_send = EmailMessage(
                'Blood Request Accepted',
                'Your blood request has been accepted. The contact info of the donor is : \n Name: ' + user_info.email + '\n Email: ' + user_info.username + ' ' ,
                settings.EMAIL_HOST_USER,
                [email2.email],
                reply_to=[settings.EMAIL_HOST_USER],
                headers = {'Message-ID': 'foo'},
        ).send()
        # also the requester info will go to the donor
        email_send = EmailMessage(
                'Blood Requester Info',
                'The info of the requester of the blood request you accepted is : \nName: ' + str(email2.first_name) + ' ' + str(email2.last_name)  + '\nEmail: ' +str( email2.email) +'\nHospital Address: '+ str(email2.address) + '\nAge: ' + str(email2.Age) + '\nBlood Group of the patient: ' + str(email2.blood_group) + '\nReason for the request: ' + str(email2.reason) + ' ' ,
                settings.EMAIL_HOST_USER,
                [user_info.username],
                reply_to=[settings.EMAIL_HOST_USER],
                headers = {'Message-ID': 'foo'},
        ).send()
        Blood_form.objects.get(id=email2.id).delete()
        return JsonResponse({'status': 'success'})

        # delete the request from the database after it has been accepted
    def delete_request(request):
        # get the accepted request post 
        request_id = request.POST['requester_id']
        request_id = int(request_id)
        # delete the request from the database
        Blood_form.objects.get(id=request_id).delete()
        return JsonResponse({'status': 'success'})


                

            