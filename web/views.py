from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import DetailView, TemplateView
import stripe
from django.conf import settings
from django.views import View
from .models import (
    Course,
    # PlaylistHead,
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
    context = {"details": ProfileDetails.objects.all()}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("msg")
        form = Contact(name=name, email=email, number=number, msg=message)
        form.save()
         
    return render(request,'web/web_dev/contact.html',context)


class TopicsView(TemplateView):
    template_name="web/web_dev/topics.html"

    

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        
        context["html_courses"] = Course.object.filter(Course__category="html")
        context["css_courses"] = Course.object.filter(Course__category="css")
        context["js_courses"] = Course.object.filter(Course__category="js")
        context["bootstrap_courses"] = Course.object.filter(Course__category="bootstrap")
        context["react_courses"] = Course.object.filter(Course__category="react")
        context["python_courses"] = Course.object.filter(Course__category="python")
        context["psql_courses"] = Course.object.filter(Course__category="psql")
        context['details'] = ProfileDetails.objects.all()
        
        return context
  
  
class PlaylistView(DetailView):
    template_name = "web/web_dev/playlists/playlist.html"
    model = Playlist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["html_playlist"] = Playlist.objects.filter(category="html")
        context["watch"] = Video.objects.all()
        context["css_playlist"] = Playlist.objects.filter(category="css")
        context["js_playlist"] = Playlist.objects.filter(category="js")
        context["bootstrap_playlist"] = Playlist.objects.filter(category="bootstrap")
        return context
    

class WatchVideoView(View):
    template_name = "web/web_dev/watch_video/watch_video.html"
    model = Video
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["details"] =ProfileDetails.objects.all()
        return context
    

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
