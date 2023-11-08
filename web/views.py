from typing import Any
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from . models import html_course
from . models import css_course
from . models import js_course
from . models import bootstrap_course
from . models import react_course
from . models import python_course
from . models import psql_course
from . models import flutter_course
from . models import contact_form
from . models import selectbox_course
from . models import teacher_profile
from . models import html_playlist
from . models import css_playlist
from . models import bootstrap_playlist
from . models import react_playlist
from . models import python_playlist
from . models import psql_playlist
from . models import js_playlist
from . models import playlist_head
from . models import watch_video
from . models import css_watch_video
from . models import js_watch_video
from . models import bootstrap_watch_video
from . models import react_watch_video
from . models import python_watch_video
from . models import psql_watch_video
from django.views.generic import TemplateView,DetailView
from . models import profile_details
# from . models import signup_form
from django.contrib import messages


app_name='web_2'
# from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    context={
        'details':profile_details.objects.all(),
        
    }
    # course=get_object_or_404(web_course, pk=id, slug=slug) 
    return render(request,'web/web_dev/home.html',context)
def about(request):
    context = {
        'details' : profile_details.objects.all()
    }
    return render(request,'web/web_dev/about.html',context)
def contact(request):
   context={
        'details':profile_details.objects.all()
    }
   if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("number")
        msg=request.POST.get("msg")

        form= contact_form (
            name=name,
            email=email,
            number=number,
            msg=msg
        )
        form.save()
       

   return render(request,'web/web_dev/contact.html ',context)
# def topics(request):
#     context = {
#         'coursu' : web_course.objects.all()
#     }
#     return render(request,'web/web_dev/topics.html',context)



# def html_playlist(request):
#     return render(request,'web/web_dev/playlists/html_playlist.html')

# def css_playlist(request):
#     return render(request,'web/web_dev/playlists/css_playlist.html')

# def bootstrap_playlist(request):
#     return render(request,'web/web_dev/playlists/bootstrap_playlist.html')

# def react_playlist(request):
#     return render(request,'web/web_dev/playlists/react_playlist.html')
# def js_playlist(request):
#     return render(request,'web/web_dev/playlists/js_playlist.html')
# def git_playlist(request):
#     return render(request,'web/web_dev/playlists/git_playlist.html')
# def python_playlist(request):
#     return render(request,'web/web_dev/playlists/python_playlist.html')

class topics(TemplateView):
    
    

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["coursu"] = html_course.objects.all()
        context["coursu_2"] = css_course.objects.all()
        context["coursu_3"] = js_course.objects.all()
        context["coursu_4"] = bootstrap_course.objects.all()
        context["coursu_5"] = react_course.objects.all()
        context["coursu_6"] = python_course.objects.all()
        context["coursu_7"] = psql_course.objects.all()
        context["play"] = html_playlist.objects.all()
        context["play_2"] = css_playlist.objects.all()
        context["play_3"] = js_playlist.objects.all()
        context['details'] = profile_details.objects.all()
        
        
        
        return context
    template_name="web/web_dev/topics.html"
    model=profile_details
        
    # def get_context_data(self, **kwargs) :
    #     context = super().get_context_data(**kwargs)
       
    #     return context 

class playlist_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['play'] = html_playlist.objects.all()
        context['watch'] = watch_video.objects.all()
        context['list'] = css_playlist.objects.all()
        context['js_list'] = js_playlist.objects.all()
        context['bootstrap_list'] = bootstrap_playlist.objects.all()
        # context['details'] = profile_details.objects.all()
        


        return context
    template_name="web/web_dev/playlists/playlist.html"
    # model=playlist
    model=html_playlist
    # model=css_playlist
    # model=js_playlist
    model=bootstrap_playlist
    model=playlist_head
    model=profile_details

class css_playlist_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['watch'] = watch_video.objects.all()
        context['list'] = css_playlist.objects.all()
        context['details'] = profile_details.objects.all()

        return context
    template_name="web/web_dev/playlists/css_playlist.html"
    # model=playlist

    model=css_playlist
    model=playlist_head


class js_playlist_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['watch'] = watch_video.objects.all()
        context['js_list'] = js_playlist.objects.all()
        context['details'] = profile_details.objects.all()

        return context
    template_name="web/web_dev/playlists/js_playlist.html"
    # model=playlist

    model=js_playlist
    model=playlist_head

class bootstrap_playlist_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['watch'] = watch_video.objects.all()
        context['bootstrap_list'] = bootstrap_playlist.objects.all()
        context['details']=profile_details.objects.all()

        return context
    template_name="web/web_dev/playlists/bootstrap_playlist.html"
    # model=playlist

    model=bootstrap_playlist
    model=playlist_head

class react_playlist_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['watch'] = watch_video.objects.all()
        context['react_list'] = react_playlist.objects.all()
        context['details']=profile_details.objects.all()

        return context
    template_name="web/web_dev/playlists/react_playlist.html"
    # model=playlist

    model=react_playlist
    model=playlist_head


class python_playlist_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['watch'] = watch_video.objects.all()
        context['python_list'] = python_playlist.objects.all()
        context['details']=profile_details.objects.all()

        return context
    template_name="web/web_dev/playlists/react_playlist.html"
    # model=playlist

    model=python_playlist
    model=playlist_head


class psql_playlist_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['watch'] = watch_video.objects.all()
        context['psql_list'] = psql_playlist.objects.all()
        context['details']=profile_details.objects.all()

        return context
    template_name="web/web_dev/playlists/psql_playlist.html"
    # model=playlist

    model=psql_playlist
    model=playlist_head


class watch_video_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
       
        context['details']=profile_details.objects.all()

        return context
    
    model=watch_video
    template_name='web/web_dev/watch_video/watch_video.html'

class css_watch_video_view(DetailView):

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        
        context['details']=profile_details.objects.all()

        return context
    model=css_watch_video
    template_name='web/web_dev/watch_video/css_watch_video.html'

class js_watch_video_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        
        context['details']=profile_details.objects.all()

        return context
    model=js_watch_video
    template_name='web/web_dev/watch_video/js_watch_video.html'

class bootstrap_watch_video_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
      
        context['details']=profile_details.objects.all()

        return context
    model=bootstrap_watch_video
    template_name='web/web_dev/watch_video/bootstrap_watch_video.html'


class react_watch_video_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
   
        context['details']=profile_details.objects.all()

        return context
    model=react_watch_video
    template_name='web/web_dev/watch_video/react_watch_video.html'

class python_watch_video_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
       
        context['details']=profile_details.objects.all()

        return context
    model=python_watch_video
    template_name='web/web_dev/watch_video/python_watch_video.html'

class psql_watch_video_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
       
        context['details']=profile_details.objects.all()

        return context
    model=psql_watch_video
    template_name='web/web_dev/watch_video/psql_watch_video.html'



def profile(request):
    context = {
        'details' : profile_details.objects.all()
        }
    return render(request,'web/web_dev/profile.html',context)
# def teacher_profile(request):

def teachers(request):
    context = {
        't_profu' : teacher_profile.objects.all(),
         'details' : profile_details.objects.all()
    }
    return render(request,'web/web_dev/teachers.html',context)
def update(request):
    if request.method=="POST":
        name=request.POST.get("student_name")
        email=request.POST.get("student_email")
        image=request.FILES["student_image"]

        form = profile_details (
            name=name,
            email=email,
            image=image,
        )
        form.save()

    context = {
        'details' : profile_details.objects.all()
    }
    return render(request,'web/web_dev/update.html',context)

def watch_video_1(request):
    context = {
        'details' : profile_details.objects.all()
        }
    return render(request,'web/web_dev/watch_video/watch_video_1.html',context)
def watch_video_2(request):
    context = {
        'details' : profile_details.objects.all()
        }
    return render(request,'web/web_dev/watch_video/watch_video_2.html',context)
def watch_video_3(request):
    context = {
        'details' : profile_details.objects.all()
        }
    return render(request,'web/web_dev/watch_video/watch_video_3.html',context)
def watch_video_4(request):
    context = {
        'details' : profile_details.objects.all()
        }
    return render(request,'web/web_dev/watch_video/watch_video_4.html',context)
def watch_video_5(request):
    context = {
        'details' : profile_details.objects.all()
        }
    return render(request,'web/web_dev/watch_video/watch_video_5.html',context)
def watch_video_6(request):
    context = {
        'details' : profile_details.objects.all()
        }
    return render(request,'web/web_dev/watch_video/watch_video_6.html',context)

def success(request):
    return render (request,'web/web_dev/payment_animation/success.html')
def cancel(request):
    return render (request,'web/web_dev/payment_animation/cancel.html')


def student_signin(request):
      
    context = {
        'selectbox' : selectbox_course.objects.all(),
        'details' : profile_details.objects.all()
    }


    if request.method=="POST":
        email=request.POST.get("email")
      

        # web_dev=request.POST.get("web_dev")
        student_id=request.POST.get("student_id")
       
        user=authenticate(username=student_id,email=email,password="web_development")
        user_2=authenticate(username=student_id,email=email,password="digital_marketing")
            
        if user is not None :
            login (request,user)
            return redirect('web:home')
        elif user_2 is not None :
            login (request,user_2)
            return redirect('web_2:d_home')
        else:
            return redirect('web:student_signin')
        # else:
        #     user_2=authenticate(username=course_2,password=student_id)
            
        #     if user_2 is not None :
        #         login (request,user_2)
        #         return redirect('web:home')
                
             
            
        #     else:
        #         return redirect('web:student_signin')

    return render(request,'web/signin/student_signin.html',context)
  


def signup(request):
    if request.method=="POST":
        # username=request.POST.get("username")
        f_name=request.POST.get("f_name")
        l_name=request.POST.get("l_name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        course=request.POST.get("course")
        student_id=request.POST.get("student_id")

        if student_id!=student_id :
            messages.warning(request,'invalid student id')
        else:
            customer = User.objects.create_user(student_id,email,course)
            customer.f_name=f_name
            customer.l_name=l_name
            customer.phone=phone

            customer.save()
            return redirect('web:student_signin')



        # log_form = signup_form (
        #     username=username,
        #     first_name=f_name,
        #     second_name=l_name,
        #     email=email,
        #     phone_number=phone,
        #     course=course,
        #     student_id=student_id,

        # )

        # log_form.save()

    return render(request,'web/signin/signup.html')


# stripe api integration 


import stripe
from django.conf import settings
from django.views import View


stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
     
        price=5000

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "inr",
                        "unit_amount": int(price) * 100,
                        "product_data": {
                            "name": 'web development',
                          
                            # "images": [
                            #     f"{settings.BACKEND_DOMAIN}/{price.product.thumbnail}"
                            # ],
                        },
                    },
                    "quantity":1,
                }
            ],
            # metadata={"product_id": price.product.id},
            mode="payment",
            success_url="http://localhost:8000/success",
            cancel_url="http://localhost:8000/cancel",
        )
        return redirect(checkout_session.url)
