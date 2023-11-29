from django.contrib import messages
import urllib.parse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import DetailView, TemplateView
import stripe
from django.conf import settings
from django.views import View
from .forms import ContactForm
from .models import (
    Course,
    PlaylistHead,
    Playlist,
    Video,
    Contact,
    ProfileDetails,
    TeacherProfile,
    
)

def home(request):
    context = {
        "details": ProfileDetails.objects.all(),
    }
    return render(request, "web/web_dev/home.html", context)


def about(request):
    context = {"details": ProfileDetails.objects.all()}
    return render(request, "web/web_dev/about.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            message = (
                f'Name: {form.cleaned_data["name"]} \n'
                f'number: {form.cleaned_data["number"]}\n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Message: {form.cleaned_data["message"]}\n'
            )
            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "9037126305"
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = (
                f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"
            )
            return redirect(whatsapp_url)
        print(form.errors)
    
    context = {
            "is_contact": True,
            "form": form,
        }
         
    return render(request,'web/web_dev/contact.html',context)


class TopicsView(TemplateView):
    template_name = "web/web_dev/topics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["courses"] = Course.objects.all()
        context['details'] = ProfileDetails.objects.all()

        return context


  
  
class PlaylistView(DetailView):
    template_name = "web/web_dev/playlists/playlist.html"
    model = Playlist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch the playlist
        playlist = self.object
        course = playlist.course

        # Fetch the associated playlist head
        playlist_head = playlist.playlist_head

        # Add the playlist and playlist_head to the context
        context["playlist"] = playlist
        context["playlist_head"] = playlist_head

        # Filter playlists based on the category of the associated course
        context["html_playlist"] = Playlist.objects.filter(course=course, category="html")
        context["watch"] = Video.objects.all()
        context["css_playlist"] = Playlist.objects.filter(course=course, category="css")
        context["js_playlist"] = Playlist.objects.filter(course=course, category="js")
        context["bootstrap_playlist"] = Playlist.objects.filter(course=course, category="bootstrap")

        return context




class WatchVideoView(View):
    template_name = "web/web_dev/watch_video/watch_video.html"

    def get(self, request, *args, **kwargs):
        video_id = kwargs.get('pk')  # Assuming your URL includes the video ID
        video = get_object_or_404(Video, pk=video_id)

        context = {
            'object': video,
            'details': ProfileDetails.objects.all(),
        }

        return render(request, self.template_name, context)

def profile(request):
    context = {"details": ProfileDetails.objects.all()}
    return render(request, "web/web_dev/profile.html", context)


def teachers(request):
    context = {
        "t_profu": TeacherProfile.objects.all(),
        "details": ProfileDetails.objects.all(),
    }
    return render(request, "web/web_dev/teachers.html", context)


def update(request):
    if request.method == "POST":
        name = request.POST.get("student_name")
        email = request.POST.get("student_email")
        image = request.FILES["student_image"]

        form = ProfileDetails(
            name=name,
            email=email,
            image=image,
        )
        form.save()

    context = {"details": ProfileDetails.objects.all()}
    return render(request, "web/web_dev/update.html", context)


def success(request):
    return render(request, "web/web_dev/payment_animation/success.html")


def cancel(request):
    return render(request, "web/web_dev/payment_animation/cancel.html")


def student_signin(request):

    if request.method == "POST":
        email = request.POST.get("email")
        student_id = request.POST.get("student_id")
        user = authenticate(
            username=student_id, email=email, password="web_development"
        )
        user_2 = authenticate(
            username=student_id, email=email, password="digital_marketing"
        )
        if user is not None:
            login(request, user)
            return redirect("web:home")
        elif user_2 is not None:
            login(request, user_2)
            return redirect("web_2:d_home")
        else:
            return redirect("web:student_signin")
    return render(request, "web/signin/student_signin.html")


def signup(request):
    if request.method == "POST":
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        course = request.POST.get("course")
        student_id = request.POST.get("student_id")
        if student_id != student_id:
            messages.warning(request, "invalid student id")
        else:
            customer = User.objects.create_user(student_id, email, course)
            customer.f_name = f_name
            customer.l_name = l_name
            customer.phone = phone

            customer.save()
            return redirect("web:student_signin")
    return render(request, "web/signin/signup.html")

# stripe api integration
stripe.api_key = settings.STRIPE_SECRET_KEY
class CreateStripeCheckoutSessionView(View):
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
                            "name": "web development",
                            # "images": [
                            #     f"{settings.BACKEND_DOMAIN}/{price.product.thumbnail}"
                            # ],
                        },
                    },
                    "quantity": 1,
                }
            ],
            # metadata={"product_id": price.product.id},
            mode="payment",
            success_url="http://localhost:8000/success",
            cancel_url="http://localhost:8000/cancel",
        )
        return redirect(checkout_session.url)
