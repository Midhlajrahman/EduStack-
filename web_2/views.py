from typing import Any
from django.shortcuts import render
from . models import contact_form
from . models import profile_form
from django.views.generic import TemplateView,DetailView
from  django.core.files import File
from django.shortcuts import redirect

# course section 
from . models import course_1
from . models import course_2
from . models import course_3

# side bar section 
from . models import d_teacher_profile

# playlist section 
from . models import playlist_1
from . models import playlist_2
from . models import playlist_3
from . models import d_playlist_head

# watch video section 
from . models import d_watch_video
from . models import d_watch_video_2
from . models import d_watch_video_3
# from . models import css_course
# from . models import js_course
# Create your views here.
def d_home(request):
    context={
        'updates':profile_form.objects.all()
    }
    # course=get_object_or_404(web_course, pk=id, slug=slug) 
    return render(request,'web/digital_marketing/d_home.html',context)
def d_about(request):
    context={
        'updates':profile_form.objects.all()
    }
    return render(request,'web/digital_marketing/d_about.html',context)
def d_contact(request):
   context={
        'updates':profile_form.objects.all()
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
       

   return render(request,'web/digital_marketing/d_contact.html ',context)

def d_profile(request):
    context={
        'updates':profile_form.objects.all()
    }
      
    return render(request,'web/digital_marketing/d_profile.html',context)
def d_teachers(request):
    context = { 
        't_profu' : d_teacher_profile.objects.all(),
        'updates':profile_form.objects.all()
    }
    return render(request,'web/digital_marketing/d_teachers.html',context)



# class d_topics_view(TemplateView):
    
#     template_name="web/digital_marketing/d_topics.html"

#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context["courz"] = course_1.objects.all()
       
#         return context
       

def d_topics_view(request):
    context = {
        'courzu' : course_1.objects.all() ,
        'courzu_2' : course_2.objects.all() ,
        'updates':profile_form.objects.all()
       

    }
    return render(request,'web/digital_marketing/d_topics.html',context)
class d_topics_view(TemplateView):
    template_name="web/digital_marketing/d_topics.html"

    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context["courzu"] = course_1.objects.all() 
        context["courzu_2"] = course_2.objects.all() 
        context["courzu_3"] = course_3.objects.all() 
        context['updates'] = profile_form.objects.all()
      

        return context
       

    


def d_update(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        image=request.FILES["image"]

        form = profile_form (
            name=name,
            email=email,
            image=image,
        )
        form.save()

    context={
        'updates':profile_form.objects.all()
    }   
    return render(request,'web/digital_marketing/d_update.html',context)
    

# class d_update_view(TemplateView):
    
#     def get_context_data(self, **kwargs):

#         if request.method=="POST":
#             name=request.POST.get("name")
#             email=request.POST.get("email")
#             pic=request.POST.get("pic")

#             form = profile_form (
#                 name=name,
#                 email=email,
#                 pic=pic
#         )
#         form.save()
#         context = super().get_context_data(**kwargs)  
#         return context
#     template_name="web/digital_marketing/d_update.html"
#     model=profile_form   



class playlist_1_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['d_play'] = playlist_1.objects.all()
        context['updates'] = profile_form.objects.all()
        return context
    template_name="web/digital_marketing/playlist/playlist_1.html"

    model=playlist_1
    # model=d_playlist_head

class playlist_2_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['d_play_2'] = playlist_2.objects.all()
        context['updates'] = profile_form.objects.all()

        return context
    template_name="web/digital_marketing/playlist/playlist_2.html"

    model=playlist_2
    # model=d_playlist_head

class playlist_3_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['d_play_3'] = playlist_3.objects.all()
        context['updates'] = profile_form.objects.all()

        return context
    template_name="web/digital_marketing/playlist/playlist_3.html"

    model=playlist_3
    # model=d_playlist_head

def playlist_4(request):
    return render(request,'web/digital_marketing/playlist/playlist_4.html')
def playlist_5(request):
    return render(request,'web/digital_marketing/playlist/playlist_5.html')
def playlist_6(request):
    return render(request,'web/digital_marketing/playlist/playlist_6.html')
def playlist_7(request):
    return render(request,'web/digital_marketing/playlist/playlist_7.html')

class d_watch_video_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)

        context['updates'] = profile_form.objects.all()

        return context
    model=d_watch_video
    template_name="web/digital_marketing/watch_video/d_watch_video.html"
class d_watch_video_2_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
     
        context['updates'] = profile_form.objects.all()

        return context
    model=d_watch_video_2
    template_name="web/digital_marketing/watch_video/d_watch_video_2.html"

class d_watch_video_3_view(DetailView):
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
     
        context['updates'] = profile_form.objects.all()

        return context
    model=d_watch_video_3
    template_name="web/digital_marketing/watch_video/d_watch_video_2.html"


import stripe
from django.conf import settings
from django.views import View


stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateStripeCheckoutSessionView1(View):
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
                            "name": 'Digital Marketing',
                          
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