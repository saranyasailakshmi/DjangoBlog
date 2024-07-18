from django.shortcuts import render,HttpResponseRedirect
from blog.forms import UserSignupForm,UserLoginForm,NewPostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from blog.models import Post
from django.contrib.auth.models import Group
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# class PostDetailView(DetailView,LoginRequiredMixin):
#     model = Post
#     context_object_name ='posts'
#     template_name ='blog/post.html'
#     login_url ='blog/login'

def bloghome(request):
    posts = Post.objects.all()
    context = {'msg':'Pystack Blog Development','posts':posts}
    return render(request,'blog/home.html',context)

def post(request,id):
    post = Post.objects.get(pk=id)
    viewed_posts = request.session.get('viewed_posts',[])
    print(viewed_posts)
    if id not in viewed_posts:
        post.views = post.views + 1
        post.save()
        viewed_posts.append(id)
        print(viewed_posts)
        request.session['viewed_posts'] = viewed_posts
    context = {'msg':'This is User Post Page','post':post}
    return render(request,'blog/post.html',context)

def post_likes(request,id):
    post = Post.objects.get(pk=id)
    liked_posts = request.session.get('liked_posts',[])
    if id not in liked_posts:
        post.likes = post.likes + 1
        post.save()
        liked_posts.append(id)
        request.session['liked_posts'] = liked_posts
    context = {'msg':'This is User Post Page','post':post}
    return render(request,'blog/post.html',context)

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user)
        user = request.user
        fullname = user.get_full_name()
        groups = Group.objects.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'fullname':fullname,'groups':groups})
    else:
        return HttpResponseRedirect('/blog/user_login')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserLoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user = authenticate(username=uname,password=pwd)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Done Successfully!!')
                    return HttpResponseRedirect('/blog/dashboard')
        else:
            form = UserLoginForm()
        context = {'form':form}
        return render(request,'blog/login.html',context)
    else:
        return HttpResponseRedirect('/blog/dashboard')

def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request,'Singup Done as Author Suucessfully!!')
    else:
        form = UserSignupForm()
    context = {'form':form}
    return render(request,'blog/signup.html',context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/blog/user_login')

def newpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NewPostForm(request.POST,request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post_image = form.cleaned_data['post_image']
                author = request.user
                post1 = Post(title=title,desc=desc,author=author,post_image=post_image)
                post1.save()
                form = NewPostForm()
        else:
            form = NewPostForm()
        return render(request,'blog/newpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/blog/user_login')
    
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post.objects.get(pk=id)
            form = NewPostForm(request.POST,instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,'Post Updated')
                return HttpResponseRedirect('/blog/dashboard')
        else:
            post = Post.objects.get(pk=id)
            form = NewPostForm(instance=post)
        context = {'form':form}
        return render(request,'blog/updatepost.html',context)
    else:
        return HttpResponseRedirect('/blog/user_login')
    
def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post.objects.get(pk=id)
            post.delete()
            return HttpResponseRedirect('/blog/dashboard')
    else:
        return HttpResponseRedirect('/blog/user_login')
    

def setsess(request):
    request.session['sid'] = 1005
    request.session['sname'] = 'Gopi'
    request.session['course'] = 'python'
    request.session.setdefault('fee',12000)
    request.session.set_expiry(60)
    return render(request,'blog/sess.html')

def getsess(request):
    sid = request.session.get('sid')
    sname = request.session.get('sname')
    # keys = request.session.keys()
    # values = request.session.values()
    # items = request.session.items()
    return render(request,'blog/sess.html',{'sid':sid,'sname':sname})

def delsess(request):
    # if 'sid' in request.session:
    #     del request.session['sid']
    request.session.flush()
    request.session.clear_expired()
    return render(request,'blog/sess.html')
