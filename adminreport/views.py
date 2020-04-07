from django.shortcuts import render, get_object_or_404, redirect,reverse
from django.contrib.auth.models import User
from webpage.models import Reviewmovie
from webboard.models import boardpost
from django.contrib import messages
# Create your views here.
def Report(request):
    movie = Reviewmovie.objects.all().order_by('-review_date')
    member = User.objects.all().order_by('-is_superuser')
    webboard = boardpost.objects.all()
    return render(request,'report.html',{'member':member,'movie':movie,'webboard':webboard})

def MemberDelete(request, id):
    member = get_object_or_404(User, id = id)
    if request.method == "POST":
        member.delete()
        reverse('report:report')
        messages.success(request,'ลบข้อมูลสำเร็จ')
        return redirect('report:report')
    else:
        return render(request,'report.html')

def UserInformation(request,id):
    userinformation = User.objects.all().filter(id=id)
    context={
        'userinformation':userinformation
    }
    return render(request,'userinformation.html',context)
