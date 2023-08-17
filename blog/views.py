from django.shortcuts import render , redirect
from blog.models import Post
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
     posts = Post.objects.all()
     return render(request, 'blog/home.html', {'posts': posts})



def contact(request):
     return render(request, 'blog/contact.html')



def about(request):
     return render(request, 'blog/about.html')

@login_required(login_url='signin')
def create(request):
     return render(request, 'blog/create.html')



def create_process(request):
     a = request.POST['title']
     b = request.POST['text']

     post = Post.objects.create(title=a, text=b)
     post.save()

     return HttpResponseRedirect('/')

@login_required(login_url='signin')
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return HttpResponseRedirect('/')


def signup(request):

     if request.method == 'POST':

        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']

        myuser = User.objects.create_user(username=username, password=pass1, email=email)

        myuser.save()
        return redirect('signin')
        message.success(request, " account is created")



     return render(request, "blog/signup.html")








def signin(request):

    if request.method=='POST':
          username = request.POST['username']
          pass1 = request.POST['pass1']

          user = authenticate(username= username, password= pass1 )

          if user is not None:
              login(request, user)
              fname = user.first_name

              #return render(request, "blog/home.html", {"fname": fname})
              #messages.success(request, "Logged In Sucessfully!!")
              return redirect('home')
          else:
              messages.error(request, "bad credentials")
              return redirect('signin')

    return render(request, "blog/signin.html")






def signout(request):
    logout(request)
    return redirect('home')