from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from Product.models import Category,Product,Images,Comment,CommenttForm
from PremiumApp.models import Setting,ContactForm,ContactMessage
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from user.models import UserProfile
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from user.forms import signUpForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def UserP(request):
	#context={}
	return HttpResponse('okay ')




def for_login(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			current_user=request.user
			userpro=UserProfile.objects.get(user_id=current_user.id)
			request.session['userimage']=userpro.image.url
			return redirect('index')
		else:
			messages.warning(request,"Your password or username is not correct")
			return redirect('for_login')
	category=Category.objects.all()
	context={
	'category':category,
	}
	return render(request,'login.html',context)



def forlogout(request):
	logout(request)
	return redirect('index')



def forSignUp(request):
	if request.method == 'POST':
		form = signUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			current_user = request.user
			data=UserProfile()
			data.user_id=current_user.id
			data.image="images/users/user.png"
			data.save()
			messages.success(request, 'Your account has been created!')
			return redirect('index')
		else:
			messages.warning(request,"Your new and reset password is not matched")
			return redirect('forSignUp')


	form = signUpForm()
	category=Category.objects.all()
	context={
	'category':category,
	'form': form,

	}
	return render(request, 'signup.html',context)




def ForUserProfile(request):
	category=Category.objects.all()
	current_user = request.user  # Access User Session information
	profile = UserProfile.objects.get(user_id=current_user.id)
	context={
	'category':category,
	'profile':profile,
	
	}
	return render(request, 'userprofile.html',context)






@login_required(login_url='/user/login') # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('ForUserProfile')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'userupdate.html', context)



@login_required(login_url='/user/login') # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user/userprofile')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        #category = Category.objects.all()
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'userpasswordupdate.html', {'form': form,'category': category
                       })