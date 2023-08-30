from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import make_order,createUserForm,comments_form
from .models import product,post,choice,chat_post,chat_comment
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import F

def register(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid:
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Your account has been successfully created')
    context = {'form':form}
    
    return render(request,'register.html',context)

def login_view(request):
   if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or password does not exist')
            form = AuthenticationForm()
   context = {}
   return render(request,'login.html',context)    
    
def logoutuser(request):
    logout(request)
    return redirect('login')   


def index(request):
    obj = product.objects.all()[:3]
    return render(request,'index.html',{'obj':obj})
    

@login_required(login_url='login')
def product_add(request):
    form = make_order
    if request.method == 'POST':
        form = make_order(request.POST)
        if form.is_valid():
          form.save()
          return redirect('product_add')
    else:
        form = make_order    
    return render(request,'product_add.html',{'form':form})

@login_required(login_url='login')
def blog_home(request):
    post_list = post.objects.order_by('-date_published')[:3]
    context = {'post_list':post_list}
    return render(request,'blog_home.html',context)

def blog_vote(request,pk):
    blog_post = get_object_or_404(post,pk= pk)
    try:
        selected_choice = blog_post.choice_set.get(pk = request.POST['choice'])

    except(KeyError,choice.DoesNotExist):
        return render(request,'blog_detail.html',{'blog_post':blog_post,"error_message":"You did not select a choice"})
    else:
        selected_choice.vote = F('vote') +  1
        selected_choice.save()
    return HttpResponseRedirect(reverse('blog_result',args=(selected_choice.id,)))

def blog_result(request,pk):
    blog_post = get_object_or_404(post,pk=pk)
    return render(request,'blog_result.html',{'blog_post': blog_post})

def blog_detail(request,pk):
    blog_post = get_object_or_404(post,pk=pk)
    context = {'blog_post':blog_post,}
    return render(request,'blog_detail.html',context)

def chats(request):
    chat_posts = chat_post.objects.all()

    return render(request,'chat_post.html',{'chat_posts':chat_posts})        


def chat_post_detail(request,pk):
    chat_posts = get_object_or_404(chat_post,pk=pk)
    comments = chat_posts.comments.all()

    if request.method == 'POST':
        comments = comments_form(request.POST or None)
        if comments.is_valid():
            new_comment = comments.save(commit = False)
            new_comment.chat_post = chat_posts
            new_comment.comment = chat_posts
            new_comment.save()
        else:
            return redirect('chat_post_detail' ,pk=pk)
            comments  = comments_form()
    return render(request,'chat_post_detail.html',{'chat_posts':chat_posts,'comments':comments,'comments_form':comments_form})        


       

