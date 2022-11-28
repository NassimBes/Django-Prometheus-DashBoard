import socket
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from .models import ServerInfoModel,ServerModel
from .forms import ServerModelForms

@login_required(login_url='/login')
def HomePage(request):
    servModel = ServerModel

    return render(request,"homepage/homepage.html",
        {
            "serverModels" : servModel.objects.all,
        }
    )
    

@login_required(login_url='/login')
def ServerFormView(request):
    if request.method == "POST":
        form = ServerModelForms(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if ItemExist(instance.hostname):
                return render(request,'homepage/AddServerForm.html',{'form':form})
            else:
                try:
                    socket.gethostbyname(instance.hostname)
                except:
                    return render(request,'homepage/AddServerForm.html',{
                            'form' : form,
                        })
                instance.ipAddress = socket.gethostbyname(instance.hostname)
                instance.save()
                ServerModel = form.save()
                return redirect("homepage")
    else:
        form = ServerModelForms()
    return render(request,'homepage/AddServerForm.html',{
        'form' : form,
    })


def ItemExist(hostname):
    for obj in ServerModel.objects.all():
        if obj.hostname ==  hostname:
            return True
    return False

@login_required(login_url='/login')
def loginout(request):
    logout(request)
    return redirect('loginpage')