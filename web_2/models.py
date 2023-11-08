from django.db import models

# Create your models here.
#  teachers profile 
class d_teacher_profile(models.Model):
    teacher_image=models.ImageField(upload_to='media')
    teacher_name=models.CharField(max_length=50)
    teacher_position=models.CharField(max_length=50)
    insta_url=models.CharField( max_length=50)
    wp_url=models.CharField( max_length=50)
    linkedin_url=models.CharField( max_length=50)

# contact form 

class contact_form(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    number=models.IntegerField()
    msg=models.TextField()

class profile_form (models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    image=models.FileField(blank=True, null=True, upload_to='images')


class d_playlist_head(models.Model):
    d_topic_thumb=models.ImageField(upload_to='media')
    d_how_many_videos=models.CharField(max_length=50)
    d_tutor_image=models.ImageField(upload_to='media')
    d_tutor_name=models.CharField(max_length=50)
    d_date=models.CharField(max_length=50)
    d_topic_title=models.CharField(max_length=100)
    d_topic_description=models.CharField(max_length=100)

class playlist_1(models.Model):
    video_thumbnail=models.FileField(upload_to='media')
    video_title=models.CharField(max_length=50)

class playlist_2(models.Model):
    video_thumbnail=models.FileField(upload_to='media')
    video_title=models.CharField(max_length=50)

class playlist_3(models.Model):
    video_thumbnail=models.FileField(upload_to='media')
    video_title=models.CharField(max_length=50)
#  course models 
class course_1(models.Model):
    authername=models.CharField(max_length=50)
    auther_image=models.ImageField(upload_to='media')   
    date=models.CharField(max_length=50)     
    howmany_videos=models.CharField(max_length=50) 
    video_title=models.CharField(max_length=50) 
    thumbnail=models.ImageField(upload_to='media')

class course_2(models.Model):
    authername=models.CharField(max_length=50)
    auther_image=models.ImageField(upload_to='media')   
    date=models.CharField(max_length=50)     
    howmany_videos=models.CharField(max_length=50) 
    video_title=models.CharField(max_length=50) 
    thumbnail=models.ImageField(upload_to='media')

class course_3(models.Model):
    authername=models.CharField(max_length=50)
    auther_image=models.ImageField(upload_to='media')   
    date=models.CharField(max_length=50)     
    howmany_videos=models.CharField(max_length=50) 
    video_title=models.CharField(max_length=50) 
    thumbnail=models.ImageField(upload_to='media')



# watch video section 

class d_watch_video(models.Model):
    video=models.FileField(upload_to="media")
    video_thumb=models.FileField(upload_to='media')
    title=models.CharField(max_length=100)
    tutor_name=models.CharField(max_length=50)
    tutor_image=models.FileField(upload_to="media")
    tutor_position=models.CharField(max_length=50)
    description=models.CharField(max_length=150)

class d_watch_video_2(models.Model):
    video=models.FileField(upload_to="media")
    video_thumb=models.FileField(upload_to='media')
    title=models.CharField(max_length=100)
    tutor_name=models.CharField(max_length=50)
    tutor_image=models.FileField(upload_to="media")
    tutor_position=models.CharField(max_length=50)
    description=models.CharField(max_length=150)

class d_watch_video_3(models.Model):
    video=models.FileField(upload_to="media")
    video_thumb=models.FileField(upload_to='media')
    title=models.CharField(max_length=100)
    tutor_name=models.CharField(max_length=50)
    tutor_image=models.FileField(upload_to="media")
    tutor_position=models.CharField(max_length=50)
    description=models.CharField(max_length=150)


# class test_details(models.Model):

#     image=models.FileField(upload_to='media')
#     name=models.CharField(max_length=100)


# class html_course(models.Model):
#     authername=models.CharField(max_length=50)
#     auther_image=models.ImageField(upload_to='media')   
#     date=models.CharField(max_length=50)     
#     howmany_videos=models.CharField(max_length=50) 
#     video_title=models.CharField(max_length=50) 
#     thumbnail=models.ImageField(upload_to='media')

# class html_playlist(models.Model):
   
#     video_thumbnail=models.ImageField(upload_to='media')
#     video_title=models.CharField(max_length=50)

# class css_course(models.Model):
#     authername=models.CharField(max_length=50)
#     auther_image=models.ImageField(upload_to='media')   
#     date=models.CharField(max_length=50)     
#     howmany_videos=models.CharField(max_length=50) 
#     video_title=models.CharField(max_length=50) 
#     thumbnail=models.ImageField(upload_to='media')
# /
# class css_playlist(models.Model):
   
#     video_thumbnail=models.ImageField(upload_to='media')
#     video_title=models.CharField(max_length=50) 

# class js_course(models.Model):
#     authername=models.CharField(max_length=50)
#     auther_image=models.ImageField(upload_to='media')   
#     date=models.CharField(max_length=50)     
#     howmany_videos=models.CharField(max_length=50) 
#     video_title=models.CharField(max_length=50) 
#     thumbnail=models.ImageField(upload_to='media')

# class js_playlist(models.Model):
   
#     video_thumbnail=models.ImageField(upload_to='media')
#     video_title=models.CharField(max_length=50) 
