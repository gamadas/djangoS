from django.shortcuts import render
from django.http import HttpResponse
from erma_app.models import AccessRecord, Topic, Webpage
# for forms     -- . means current directory
# from . import forms
from erma_app.forms import UserForm, UserProfileForm

# for login built-in feature
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# for Class Based View
from django.views.generic import View, TemplateView

# Class Based View Sample
class IndexView(TemplateView):
    template_name = 'erma_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['insert_key'] = 'HOGEHOGE INSERTED'
        return context

# Create your views here.

def index(request):
    return render(request,'erma_app/index.html',)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def special(request):
    return HttpResponse("You are logged in, cheers")


# def index(request):
    # map_dic = {'insert_key': "YMGM  replaced it!!"}
    # return render(request,'erma_app/index.html',context=map_dic)

# def index(request): # DBからリストを取りテンプレートにマッピング
#     cur_list = AccessRecord.objects.order_by('date')
#     map_dic = {'acc_record':cur_list}
#     return render(request,'erma_app/index.html',context=map_dic)


def form_name_view(request):
    form = forms.MyForm()
    return render(request,'erma_app/form.html',{'form':form})

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Validation
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'erma_app/registration.html',
                        {'user_form':user_form,
                         'profile_form':profile_form,
                         'registered':registered})

def user_login(request):   # login は django package とかぶるので使わない

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("INVALID LOGIN")
    else:
        return render(request,'erma_app/login.html')
