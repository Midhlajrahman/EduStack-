from django.db import models


class Course(models.Model):
    COURSE_CHOICES = (
        ("html" , "html"),
        ("css" , "css"),
        ("js" , "js"),
        ("bootstrap" , "bootstrap"),
        ("react" , "react"),
        ("python" , "python"),
        ("psql" , "psql"),

    )
    authername = models.CharField(max_length=50, null=True, blank=True)
    auther_image = models.ImageField(upload_to="media")
    date = models.CharField(max_length=50)
    howmany_videos = models.CharField(max_length=50)
    video_title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="media")
    
    def __str__(self):
        return str(self.video_title)
    
    
class PlaylistHead(models.Model):
    
    PLAYLISTHEAD_CHOICES = (
        ("html", "html"),
        ("css", "css"),
        ("js", "js"),
        ("bootstrap", "bootstrap"),
        ("react", "react"),
        ("python", "python"),
        ("psql", "psql"),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic_thumb = models.ImageField(upload_to="media")
    how_many_videos = models.CharField(max_length=50)
    tutor_image = models.ImageField(upload_to="media")
    tutor_name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    topic_title = models.CharField(max_length=100)
    topic_description = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=PLAYLISTHEAD_CHOICES)

    def __str__(self):
        return str(self.topic_title)


class Playlist(models.Model):

    PLAYLIST_CHOICES = (
        ("html", "html"),
        ("css", "css"),
        ("js", "js"),
        ("bootstrap", "bootstrap"),
        ("react", "react"),
        ("python", "python"),
        ("psql", "psql"),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    playlist_head = models.ForeignKey(PlaylistHead, on_delete=models.CASCADE)
    video_thumbnail = models.ImageField(upload_to="media")
    video_title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=PLAYLIST_CHOICES)

    def __str__(self):
        return str(self.video_title)

    
class Video(models.Model):
    WATCH_CHOICES = (
        ("html" , "html"),
        ("css" , "css"),
        ("js" , "js"),
        ("bootstrap" , "bootstrap"),
        ("react" , "react"),
        ("python" , "python"),
        ("psql" , "psql"),

    )
     
    Playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)
    video = models.URLField()
    video_thumb = models.FileField(upload_to="media")
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    tutor_image = models.ImageField(upload_to="media")
    tutor_name = models.CharField(max_length=50)
    tutor_position = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=WATCH_CHOICES)  # Add this line
    
    def __str__(self):
        return str(self.title)
    
       
class TeacherProfile(models.Model):
    teacher_image = models.ImageField(upload_to="media")
    teacher_name = models.CharField(max_length=50)
    teacher_position = models.CharField(max_length=50)
    insta_url = models.URLField(null=True ,  blank=True)
    linkedin_url = models.URLField()
    
    def __str__(self):
        return str(self.teacher_name)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    number = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return str(self.name)
    
    
class ProfileDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.ImageField(blank=True, null=True, upload_to="images")  # Change this line

    
