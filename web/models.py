from django.db import models


# Create your models here.
class HtmlCourse(models.Model):
    authername = models.CharField(max_length=50)
    auther_image = models.ImageField(upload_to="media")
    date = models.CharField(max_length=50)
    howmany_videos = models.CharField(max_length=50)
    video_title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="media")


class HtmlPlaylist(models.Model):
    video_thumbnail = models.ImageField(upload_to="media")
    video_title = models.CharField(max_length=50)


class CssCourse(models.Model):
    authername = models.CharField(max_length=50)
    auther_image = models.ImageField(upload_to="media")
    date = models.CharField(max_length=50)
    howmany_videos = models.CharField(max_length=50)
    video_title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="media")


class CssPlaylist(models.Model):
    video_thumbnail = models.ImageField(upload_to="media")
    video_title = models.CharField(max_length=50)


class JsCourse(models.Model):
    authername = models.CharField(max_length=50)
    auther_image = models.ImageField(upload_to="media")
    date = models.CharField(max_length=50)
    howmany_videos = models.CharField(max_length=50)
    video_title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="media")


class JsPlaylist(models.Model):
    video_thumbnail = models.ImageField(upload_to="media")
    video_title = models.CharField(max_length=50)


class BootstrapCourse(models.Model):
    authername = models.CharField(max_length=50)
    auther_image = models.ImageField(upload_to="media")
    date = models.CharField(max_length=50)
    howmany_videos = models.CharField(max_length=50)
    video_title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="media")


class BootstrapPlaylist(models.Model):
    video_thumbnail = models.FileField(upload_to="media")
    video_title = models.CharField(max_length=50)


class ReactCourse(models.Model):
    authername = models.CharField(max_length=50)
    auther_image = models.ImageField(upload_to="media")
    date = models.CharField(max_length=50)
    howmany_videos = models.CharField(max_length=50)
    video_title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="media")


class ReactPlaylist(models.Model):
    video_thumbnail = models.FileField(upload_to="media")
    video_title = models.CharField(max_length=50)


class PythonCourse(models.Model):
    authername = models.CharField(max_length=50)
    auther_image = models.ImageField(upload_to="media")
    date = models.CharField(max_length=50)
    howmany_videos = models.CharField(max_length=50)
    video_title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="media")


class PythonPlaylist(models.Model):
    video_thumbnail = models.FileField(upload_to="media")
    video_title = models.CharField(max_length=50)


class PsqlPlaylist(models.Model):
    video_thumbnail = models.FileField(upload_to="media")
    video_title = models.CharField(max_length=50)


class PsqlCourse(models.Model):
    authername = models.CharField(max_length=50)
    auther_image = models.ImageField(upload_to="media")
    date = models.CharField(max_length=50)
    howmany_videos = models.CharField(max_length=50)
    video_title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="media")


class FlutterCourse(models.Model):
    authername = models.CharField(max_length=50)
    auther_image = models.ImageField(upload_to="media")
    date = models.CharField(max_length=50)
    howmany_video = models.CharField(max_length=50)
    video_title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="media")


class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    number = models.IntegerField()
    msg = models.TextField()


class SelectboxCourse(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name


class TeacherProfile(models.Model):
    teacher_image = models.ImageField(upload_to="media")
    teacher_name = models.CharField(max_length=50)
    teacher_position = models.CharField(max_length=50)
    insta_url = models.CharField(max_length=50)
    wp_url = models.CharField(max_length=50)
    linkedin_url = models.CharField(max_length=50)


class PlaylistHead(models.Model):
    topic_thumb = models.ImageField(upload_to="media")
    how_many_videos = models.CharField(max_length=50)
    tutor_image = models.ImageField(upload_to="media")
    tutor_name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    topic_title = models.CharField(max_length=100)
    topic_description = models.CharField(max_length=100)


class WatchVideo(models.Model):
    video = models.FileField(upload_to="media")
    video_thumb = models.FileField(upload_to="media")
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    tutor_image = models.ImageField(upload_to="media")
    tutor_name = models.CharField(max_length=50)
    tutor_position = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class CssWatchVideo(models.Model):
    video = models.FileField(upload_to="media")
    video_thumb = models.ImageField(upload_to="media")
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    tutor_image = models.ImageField(upload_to="media")
    tutor_name = models.CharField(max_length=50)
    tutor_position = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class JsWatchVideo(models.Model):
    video = models.FileField(upload_to="media")
    video_thumb = models.ImageField(upload_to="media")
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    tutor_image = models.ImageField(upload_to="media")
    tutor_name = models.CharField(max_length=50)
    tutor_position = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class BootstrapWatchVideo(models.Model):
    video = models.FileField(upload_to="media")
    video_thumb = models.FileField(upload_to="media")
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    tutor_image = models.ImageField(upload_to="media")
    tutor_name = models.CharField(max_length=50)
    tutor_position = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class ReactWatchVideo(models.Model):
    video = models.FileField(upload_to="media")
    video_thumb = models.FileField(upload_to="media")
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    tutor_image = models.ImageField(upload_to="media")
    tutor_name = models.CharField(max_length=50)
    tutor_position = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class PythonWatchVideo(models.Model):
    video = models.FileField(upload_to="media")
    video_thumb = models.FileField(upload_to="media")
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    tutor_image = models.ImageField(upload_to="media")
    tutor_name = models.CharField(max_length=50)
    tutor_position = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class PsqlWatchVideo(models.Model):
    video = models.FileField(upload_to="media")
    video_thumb = models.FileField(upload_to="media")
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    tutor_image = models.ImageField(upload_to="media")
    tutor_name = models.CharField(max_length=50)
    tutor_position = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class ProfileDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.FileField(blank=True, null=True, upload_to="images")
