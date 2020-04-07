from django.shortcuts import render,redirect , get_object_or_404,reverse,HttpResponseRedirect
from .models import Userprofile
from webpage.models import Reviewmovie
from webboard.models import boardpost
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def Register(request):
    if request.method == 'POST':
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        c_password = request.POST["confirmpassword"]
        if not firstname or not lastname or not username or not email:
            messages.error(request,'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('account:register')
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username ถูกใช้งานแล้ว')
                return redirect('account:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email ถูกใช้งานแล้ว')
                return redirect('account:register')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                user.save()
                profile = Userprofile.objects.create(user=user)
                profile.save()
                messages.success(request,'สมัครเสร็จสิ้น')
                return redirect("account:login")
        else:
            messages.error(request, 'Password และ Confirm Password ไม่ตรงกัน')
            return redirect('register')
    else:
     return render(request,'register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Your username or password is incorrect')
            return redirect('account:login')
    else:
     return render(request,'login.html')

def Logout(request):
    auth.logout(request)
    return redirect('/')

def Edit(request,id):
    if request.method == 'POST':
        user = get_object_or_404(User,id=id)
        userimage = get_object_or_404(Userprofile,user=id)
        user.email = request.POST['email']
        user.first_name= request.POST['firstname']
        user.last_name=request.POST['lastname']
        userimage.user_image = request.FILES.get('image', userimage.user_image)
        user.save()
    userimage.save()
    messages.success(request,'บันทึกสำเร็จ')
    print('สำเร็จ')
    return redirect('movie:profile',id)




