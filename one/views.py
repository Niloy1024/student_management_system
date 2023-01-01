from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import  MyUser,Test,Question,Choice
from .forms import UserForm,Testform

# # Create your views here




# def loginPage(request):
#     page = 'login'
#     if request.user.is_authenticated:
#         return redirect('teahome')

#     if request.method == 'POST':
#         email = request.POST.get('email').lower()
#         password = request.POST.get('password')
#         try:
#             user = MyUser.objects.get(email=email)
#         except:
#             messages.error(request, 'User does not exist')
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Username OR password does not exit')

#     context = {'page': page}
#     return render(request, 'base/login_register.html')


# def logoutUser(request):
#     logout(request)
#     return redirect('home')

def cleardata(re):
    y = MyUser.objects.all()
    for i in y:
        i.delete() 

    return HttpResponse('slls')

def home_teacher(request):
    form = Testform()
    print( request.user  )
    if request.method == 'POST':
        
        t = Test(user=request.user )
        t.save()

        for x in request.POST.keys():
            if x.find('question')!=-1:

                q = Question(test=t,text=request.POST[x])
                q.save()
                pass 
        
        
    return render(request,'one/test.html',{'form':form})

def home_student(p1):
    print(p1.user)
    return HttpResponse('stdhome')


def register(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save() 
            
            r = login(request, user)
            print(request.user )
            print('success ful login ')
            if request.user.is_student:
                 return redirect('home/student')
            else:
                return redirect('home/teacher')
        else:
            pass  
            # print( vars("shit problem " ) )
            # messages.error(request, 'An error occurred during registration')

    return render(request, 'one/login_register.html', {'form': form})

