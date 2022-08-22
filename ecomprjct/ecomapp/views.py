from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'page1.html')

def signup(request):
    return render(request,'page2.html')

def loginpage(request):
    return render(request,'page3.html')        

def about(request):
    return render(request,'page4.html')    

def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists! Try Again')
                #print("Username already Taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match! Try Again')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('loginpage')
    else:
        return render(request,'signup.html')

#User login functionality view
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.info(request, f'Welcome {username}')
			return redirect('about')
		else:
			messages.info(request, 'Invalid Username or Password. Try Again.')
			return redirect('loginpage')
	else:
		#messages.info(request, 'Oops, Something went wrong.')
		return redirect('loginpage')

#User logout functionality view
def logout(request):
	auth.logout(request)
	return redirect('home')
