from django.shortcuts import redirect, render
from django.views.generic import DetailView

import stripe
from django.conf import settings
from django.views import View

from .models import (
    ContactForm,
    Course1,

    DTeacherProfile,
    DWatchVideo,
    Playlist1,
    ProfileForm,
)


def d_home(request):
    context = {"updates": ProfileForm.objects.all()}
    return render(request, "web/digital_marketing/d_home.html", context)


def d_about(request):
    context = {"updates": ProfileForm.objects.all()}
    return render(request, "web/digital_marketing/d_about.html", context)


def d_contact(request):
    context = {"updates": ProfileForm.objects.all()}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        msg = request.POST.get("msg")
        form = ContactForm(name=name, email=email, number=number, msg=msg)
        form.save()
    return render(request,'web/digital_marketing/d_contact.html',context)


def d_profile(request):
    context = {"updates": ProfileForm.objects.all()}
    return render(request, "web/digital_marketing/d_profile.html", context)


def d_teachers(request):
    context = {
        "t_profu": DTeacherProfile.objects.all(),
        "updates": ProfileForm.objects.all(),
    }
    return render(request, "web/digital_marketing/d_teachers.html", context)


def d_topics_view(request):
    context = {
        "courzu": Course1.objects.all(),
        "courzu_2": Course2.objects.all(),
        "updates": ProfileForm.objects.all(),
    }
    return render(request, "web/digital_marketing/d_topics.html", context)


def d_update(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        image = request.FILES["image"]

        form = ProfileForm(
            name=name,
            email=email,
            image=image,
        )
        form.save()

    context = {"updates": ProfileForm.objects.all()}
    return render(request, "web/digital_marketing/d_update.html", context)


class Playlist1View(DetailView):
    template_name = "web/digital_marketing/playlist/playlist_1.html"
    model = Playlist1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["d_play"] = Playlist1.objects.all()
        context["updates"] = ProfileForm.objects.all()
        return context


class DVideoView(DetailView):
    template_name = "web/digital_marketing/watch_video/d_watch_video.html"
    model = DWatchVideo
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["updates"] = ProfileForm.objects.all()
        return context
    
    
stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateStripeCheckoutSessionView1(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        price = 5000

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "inr",
                        "unit_amount": int(price) * 100,
                        "product_data": {
                            "name": "Digital Marketing",
                        },
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url="http://localhost:8000/success",
            cancel_url="http://localhost:8000/cancel",
        )
        return redirect(checkout_session.url)
