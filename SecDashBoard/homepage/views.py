import socket
import requests
import sched, time
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from .models import ServerInfoModel,PromServerModel
from .forms import PromServerModelForms

@login_required(login_url='/login')
def HomePage(request):
    servModel = PromServerModel

    return render(request,"homepage/homepage.html",
        {
            "PromServerModels" : servModel.objects.all,
        }
    )
    
##NEED TO BE REVIEWED
@login_required(login_url='/login')
def ServerFormView(request):
    if request.method == "POST":
        form = PromServerModelForms(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if ItemExist(instance.hostname):
                return render(request,'homepage/AddServerForm.html',{'form':form})
            else:
                try:
                    socket.gethostbyname(instance.hostname)
                    
                except socket.gaierror:
                    return render(request,'homepage/AddServerForm.html',{
                            'form' : form,
                        })
                else:
                    instance.ipAddress = socket.gethostbyname(instance.hostname)
                    GET_REQUEST_PromCollect(instance.hostname,instance)
                instance.save()
                PromServerModel = form.save()
                return redirect("homepage")
    else:
        form = PromServerModelForms()
    return render(request,'homepage/AddServerForm.html',{
        'form' : form,
    })


def ItemExist(hostname):
    for obj in PromServerModel.objects.all():
        if obj.hostname ==  hostname:
            return True
    return False

def GET_REQUEST_PromCollect(hostname,instance):
        try:
            r = requests.get(f"http://{socket.gethostbyname(hostname)}:9090/api/v1/targets")
            
        except requests.ConnectionError:
            return redirect('homepage')

        else:
            for elem in r.json()['data']['activeTargets']:
                instance.activeTargets.append("".join(elem['discoveredLabels']['__address__'].split(':')[0]))
            
            for elem in r.json()['data']['droppedTargets']:
                if elem:
                    instance.droppedTargets.append("".join(elem['discoveredLabels']['__address__'].split(':')[0]))
            #     (state=True if elem['health']=='up' else False,scrape_duration=elem['discoveredLabels']['__scrape_interval__'])
            # servinf.save()



    
    


@login_required(login_url='/login')
def loginout(request):
    logout(request)
    return redirect('loginpage')