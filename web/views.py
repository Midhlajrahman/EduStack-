from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import DetailView, TemplateView

import stripe
from django.conf import settings
from django.views import View

from .models import (
    BootstrapCourse,
    BootstrapPlaylist,
    BootstrapWatchVideo,
    ContactForm,
    CssCourse,
    CssPlaylist,
    CssWatchVideo,
    HtmlCourse,
    HtmlPlaylist,
    JsCourse,
    JsPlaylist,
    JsWatchVideo,
    PlaylistHead,
    ProfileDetails,
    PsqlCourse,
    PsqlPlaylist,
    PsqlWatchVideo,
    PythonCourse,
    PythonPlaylist,
    PythonWatchVideo,
    ReactCourse,
    ReactPlaylist,
    ReactWatchVideo,
    SelectboxCourse,
    TeacherProfile,
    WatchVideo,
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
        msg = request.POST.get("msg")
        form = ContactForm(name=name, email=email, number=number, msg=msg)
        form.save()
         
    return render(request,'web/web_dev/contact.html',context)


class topics(TemplateView):
    template_name="web/web_dev/topics.html"
    model=ProfileDetails
    

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["coursu"] = HtmlCourse.objects.all()
        context["coursu_2"] = CssCourse.objects.all()
        context["coursu_3"] = JsCourse.objects.all()
        context["coursu_4"] = BootstrapCourse.objects.all()
        context["coursu_5"] = ReactCourse.objects.all()
        context["coursu_6"] = PythonCourse.objects.all()
        context["coursu_7"] = PsqlCourse.objects.all()
        context["play"] = HtmlPlaylist.objects.all()
        context["play_2"] = CssPlaylist.objects.all()
        context["play_3"] = JsPlaylist.objects.all()
        context['details'] = ProfileDetails.objects.all()
        
        
        
        return context

 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coursu"] = HtmlCourse.objects.all()
        context["coursu_2"] = CssCourse.objects.all()
        context["coursu_3"] = JsCourse.objects.all()
        context["coursu_4"] = BootstrapCourse.objects.all()
        context["coursu_5"] = ReactCourse.objects.all()
        context["coursu_6"] = PythonCourse.objects.all()
        context["coursu_7"] = PsqlCourse.objects.all()
        context["play"] = HtmlPlaylist.objects.all()
        context["play_2"] = CssPlaylist.objects.all()
        context["play_3"] = JsPlaylist.objects.all()
        context["details"] = ProfileDetails.objects.all()
        return context

    

class PlaylistView(DetailView):
    template_name = "web/web_dev/playlists/playlist.html"
    model = HtmlPlaylist
    model = BootstrapPlaylist
    model = PlaylistHead
    model = ProfileDetails
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["play"] = HtmlPlaylist.objects.all()
        context["watch"] = WatchVideo.objects.all()
        context["list"] = CssPlaylist.objects.all()
        context["js_list"] = JsPlaylist.objects.all()
        context["bootstrap_list"] = BootstrapPlaylist.objects.all()
        return context


class CssPlaylistView(DetailView):
    template_name = "web/web_dev/playlists/css_playlist.html"
    model = CssPlaylist
    model = PlaylistHead
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watch"] =WatchVideo.objects.all()
        context["list"] = CssPlaylist.objects.all()
        context["details"] = ProfileDetails.objects.all()
        return context


class JsPlaylistView(DetailView):
    template_name = "web/web_dev/playlists/js_playlist.html"
    model = JsPlaylist
    model = PlaylistHead
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watch"] = WatchVideo.objects.all()
        context["js_list"] = JsPlaylist.objects.all()
        context["details"] = ProfileDetails.objects.all()
        return context


class BootstrapPlaylistView(DetailView):
    template_name = "web/web_dev/playlists/bootstrap_playlist.html"
    model = BootstrapPlaylist
    model = PlaylistHead
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watch"] = WatchVideo.objects.all()
        context["bootstrap_list"] = BootstrapPlaylist.objects.all()
        context["details"] = ProfileDetails.objects.all()
        return context


class ReactPlaylistView(DetailView):
    template_name = "web/web_dev/playlists/react_playlist.html"
    model = ReactPlaylist
    model = PlaylistHead
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watch"] = WatchVideo.objects.all()
        context["react_list"] = ReactPlaylist.objects.all()
        context["details"] = ProfileDetails.objects.all()
        return context


class PythonPlaylistView(DetailView):
    template_name = "web/web_dev/playlists/react_playlist.html"
    model = PythonPlaylist
    model = PlaylistHead
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watch"] = WatchVideo.objects.all()
        context["python_list"] = PythonPlaylist.objects.all()
        context["details"] = ProfileDetails.objects.all()
        return context

   


class PsqlPlaylistView(DetailView):
    template_name = "web/web_dev/playlists/psql_playlist.html"
    model = PsqlPlaylist
    model = PlaylistHead
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watch"] = WatchVideo.objects.all()
        context["psql_list"] = PsqlPlaylist.objects.all()
        context["details"] = ProfileDetails.objects.all()
        return context
    

class WatchVideoView(DetailView):
    template_name = "web/web_dev/watch_video/watch_video.html"
    model = WatchVideo
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["details"] =ProfileDetails.objects.all()
        return context


class CssWatchVideoView(DetailView):
    template_name = "web/web_dev/watch_video/css_watch_video.html"
    model = CssWatchVideo
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["details"] = ProfileDetails.objects.all()
        return context


class JsWatchVideoView(DetailView):
    template_name = "web/web_dev/watch_video/js_watch_video.html"
    model = JsWatchVideo
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["details"] = ProfileDetails.objects.all()
        return context
    

class BootstrapWatchVideoView(DetailView):
    template_name = "web/web_dev/watch_video/bootstrap_watch_video.html"
    model = BootstrapWatchVideo
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["details"] = ProfileDetails.objects.all()
        return context


class ReactWatchVideoView(DetailView): 
    template_name = "web/web_dev/watch_video/react_watch_video.html"
    model = ReactWatchVideo
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["details"] =ProfileDetails.objects.all()
        return context
    

class PythonWatchVideoView(DetailView):
    template_name = "web/web_dev/watch_video/python_watch_video.html"
    model = PythonWatchVideo
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["details"] = ProfileDetails.objects.all()
        return context
    

class PsqlWatchVideoView(DetailView):
    template_name = "web/web_dev/watch_video/psql_watch_video.html"
    model = PsqlWatchVideo
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["details"] = ProfileDetails.objects.all()
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


def watch_video_1(request):
    context = {"details": ProfileDetails.objects.all()}
    return render(request, "web/web_dev/watch_video/watch_video_1.html", context)


def watch_video_2(request):
    context = {"details": ProfileDetails.objects.all()}
    return render(request, "web/web_dev/watch_video/watch_video_2.html", context)


def watch_video_3(request):
    context = {"details": ProfileDetails.objects.all()}
    return render(request, "web/web_dev/watch_video/watch_video_3.html", context)


def watch_video_4(request):
    context = {"details": ProfileDetails.objects.all()}
    return render(request, "web/web_dev/watch_video/watch_video_4.html", context)


def watch_video_5(request):
    context = {"details": ProfileDetails.objects.all()}
    return render(request, "web/web_dev/watch_video/watch_video_5.html", context)


def watch_video_6(request):
    context = {"details": ProfileDetails.objects.all()}
    return render(request, "web/web_dev/watch_video/watch_video_6.html", context)


def success(request):
    return render(request, "web/web_dev/payment_animation/success.html")


def cancel(request):
    return render(request, "web/web_dev/payment_animation/cancel.html")


def student_signin(request):
    context = {
        "selectbox": SelectboxCourse.objects.all(),
        "details": ProfileDetails.objects.all(),
    }

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
    return render(request, "web/signin/student_signin.html", context)


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
