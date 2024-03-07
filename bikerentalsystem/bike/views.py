from django.shortcuts import render

from.models import login
from.models import customerregistration
from.models import bikedetails
from.models import bookingdetails

def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')
def help(request):
    return render(request,'help.html')
def customerprofile(request):
    u = request.POST['username']
    data = customerregistration.objects.filter(username=u)
    return render(request,'cprofile.html' ,{'r':data})
def cregister(request):
    return render(request,'cregistration.html')
def log(request):
    return render(request,'login.html')
def mycontact(request):
    return render(request,'mycontact.html')
def adregister(request):
    return render(request,'adminregister.html')
def adboard(request):
    return render(request,'admindashboard.html')
def bike(request):
    data = bikedetails.objects.all()
    return render(request, 'bike.html', {'r': data})


#admindashboard
def cdetails(request):
    return render(request,'customerdetails.html')
def bdetails(request):
    data = bikedetails.objects.all()
    return render(request,'bikedetails.html',{'r':data})
def bookdetails(request):
    return render(request,'bookingdetails.html')
def addbike(request):
    return render(request,'addbikes.html')
def changepassword(request):
    return render(request,'changepassword.html')


def login1(request):
    m = login.objects.get(username = request.POST['username'],password=request.POST['password'])
    if m.status =='1' :
        request.session['admin_id'] = m.username

        return render(request,'admindashboard.html')
    elif m.status =='2' :
        a = request.POST['username']
        request.session['customer_id'] = m.username
        data = customerregistration.objects.filter(cusername=a)
        return render(request,'cprofile.html',{'r':data})
    else:
        return render(request,'login.html')

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return render(request,'login.html')
def cregistration(request):
    a = request.POST['cname']
    b = request.POST['cage']
    c = request.POST['caddress']
    d = request.POST['cid']
    e = request.POST['cemail']
    f = request.POST['cphnumber']
    g = request.POST['username']
    h = request.POST['password']
    data = customerregistration(cname=a, cage=b, caddress=c, cid=d, cemail=e, cphnumber=f, cusername=g)
    data.save()
    data1 = login(username=g, password=h, status=2)
    data1.save()
    return render(request,'cprofile.html')
def addingbike(request):
    a = request.FILES['bimage']
    b = request.POST['bnumber']
    c = request.POST['bname']
    d = request.POST['bcompany']
    e = request.POST['charge']
    f = request.POST['bdiscription']
    g = request.POST['bold']
    data = bikedetails(bimage=a,bnumber=b,bname=c,bcompany=d,charge=e,bdiscription=f,bold=g)
    data.save()
    print(data)
    return render(request,'admindashboard.html')
def edit(request):


    return render(request,'addbike.html')

def delete1(request):
    return render(request,'delete.html')

def delete(request):
    a = request.POST['bnumber']
    data = bikedetails.objects.get(bnumber=a)
    data.delete()
    return render(request,'bikedetails.html')



