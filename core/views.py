from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from numpy import logical_not
# Create your views here.
class Tabs:
    def index(self):
        return render(self, 'blood_requests.html')
    def blood_requests(self):
        return render(self, 'blood_requests.html')
    def profile(self):
        return render(self, 'profile.html')
    def login(self):
        return render(self, 'login.html')
    def register(self):
        return render(self, 'register.html')
    def blood_request_form(self):
        return render(self, 'blood_request_form.html')

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
        
