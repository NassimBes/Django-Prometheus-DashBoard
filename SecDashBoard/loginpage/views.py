from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.



def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect ('homepage')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None and user.is_active:
                form = login(request,user)
                messages.success(request,f' welcome {username} !!')
                return redirect('homepage')
            else:
                messages.info(request,f'account done not exit plz sign in')
        form = AuthenticationForm()
        return render(request, 'user/login.html', {'form':form, 'title':'log in'})