from django.db import models


# Create your models here.
class html_course(models.Model):
    authername=models.CharField(max_length=50)
    auther_image=models.ImageField(upload_to='media')   
    date=models.CharField(max_length=50)     
    howmany_videos=models.CharField(max_length=50) 
    video_title=models.CharField(max_length=50) 
    thumbnail=models.ImageField(upload_to='media')

class html_playlist(models.Model):
   
    video_thumbnail=models.ImageField(upload_to='media')
    video_title=models.CharField(max_length=50)

class css_course(models.Model):
    authername=models.CharField(max_length=50)
    auther_image=models.ImageField(upload_to='media')   
    date=models.CharField(max_length=50)     
    howmany_videos=models.CharField(max_length=50) 
    video_title=models.CharField(max_length=50) 
    thumbnail=models.ImageField(upload_to='media')

class css_playlist(models.Model):
   
    video_thumbnail=models.ImageField(upload_to='media')
    video_title=models.CharField(max_length=50) 

class js_course(models.Model):
    authername=models.CharField(max_length=50)
    auther_image=models.ImageField(upload_to='media')   
    date=models.CharField(max_length=50)     
    howmany_videos=models.CharField(max_length=50) 
    video_title=models.CharField(max_length=50) 
    thumbnail=models.ImageField(upload_to='media')

class js_playlist(models.Model):
   
    video_thumbnail=models.ImageField(upload_to='media')
    video_title=models.CharField(max_length=50) 


class bootstrap_course(models.Model):
    authername=models.CharField(max_length=50)
    auther_image=models.ImageField(upload_to='media')   
    date=models.CharField(max_length=50)     
    howmany_videos=models.CharField(max_length=50) 
    video_title=models.CharField(max_length=50) 
    thumbnail=models.ImageField(upload_to='media')

class bootstrap_playlist(models.Model):
   
    video_thumbnail=models.FileField(upload_to='media')
    video_title=models.CharField(max_length=50) 

class react_course(models.Model):
    authername=models.CharField(max_length=50)
    auther_image=models.ImageField(upload_to='media')   
    date=models.CharField(max_length=50)     
    howmany_videos=models.CharField(max_length=50) 
    video_title=models.CharField(max_length=50) 
    thumbnail=models.ImageField(upload_to='media')

class react_playlist(models.Model):
   
    video_thumbnail=models.FileField(upload_to='media')
    video_title=models.CharField(max_length=50) 


class python_course(models.Model):
    authername=models.CharField(max_length=50)
    auther_image=models.ImageField(upload_to='media')   
    date=models.CharField(max_length=50)     
    howmany_videos=models.CharField(max_length=50) 
    video_title=models.CharField(max_length=50) 
    thumbnail=models.ImageField(upload_to='media')

class python_playlist(models.Model):
   
    video_thumbnail=models.FileField(upload_to='media')
    video_title=models.CharField(max_length=50) 

class psql_playlist(models.Model):
   
    video_thumbnail=models.FileField(upload_to='media')
    video_title=models.CharField(max_length=50) 

class psql_course(models.Model):
    authername=models.CharField(max_length=50)
    auther_image=models.ImageField(upload_to='media')   
    date=models.CharField(max_length=50)     
    howmany_videos=models.CharField(max_length=50) 
    video_title=models.CharField(max_length=50) 
    thumbnail=models.ImageField(upload_to='media')



    

class flutter_course(models.Model):
    authername=models.CharField(max_length=50)
    auther_image=models.ImageField(upload_to='media')   
    date=models.CharField(max_length=50)     
    howmany_video=models.CharField(max_length=50) 
    video_title=models.CharField(max_length=50) 
    thumbnail=models.ImageField(upload_to='media')
class contact_form(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    number=models.IntegerField()
    msg=models.TextField()

class selectbox_course(models.Model):
    course_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.course_name
    
class teacher_profile(models.Model):
    teacher_image=models.ImageField(upload_to='media')
    teacher_name=models.CharField(max_length=50)
    teacher_position=models.CharField(max_length=50)
    insta_url=models.CharField( max_length=50)
    wp_url=models.CharField( max_length=50)
    linkedin_url=models.CharField( max_length=50)


class playlist_head(models.Model):
    topic_thumb=models.ImageField(upload_to='media')
    how_many_videos=models.CharField(max_length=50)
    tutor_image=models.ImageField(upload_to='media')
    tutor_name=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    topic_title=models.CharField(max_length=100)
    topic_description=models.CharField(max_length=100)
    # playlist_number=models.CharField( max_length=50)
    # def __str__(self):
    #     return self.playlist_number


   

class watch_video(models.Model):
    video=models.FileField(upload_to='media')
    video_thumb=models.FileField(upload_to='media')
    title=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    tutor_image=models.ImageField( upload_to='media' )
    tutor_name=models.CharField(max_length=50)
    tutor_position=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    # def __str__(self):
    #     return self.title

class css_watch_video(models.Model):
    video=models.FileField(upload_to='media')
    video_thumb=models.ImageField(upload_to='media')
    title=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    tutor_image=models.ImageField( upload_to='media' )
    tutor_name=models.CharField(max_length=50)
    tutor_position=models.CharField(max_length=50)
    description=models.CharField(max_length=100)

class js_watch_video(models.Model):
    video=models.FileField(upload_to='media')
    video_thumb=models.ImageField(upload_to='media')
    title=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    tutor_image=models.ImageField( upload_to='media' )
    tutor_name=models.CharField(max_length=50)
    tutor_position=models.CharField(max_length=50)
    description=models.CharField(max_length=100)

class bootstrap_watch_video(models.Model):
    video=models.FileField(upload_to='media')
    video_thumb=models.FileField(upload_to='media')
    title=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    tutor_image=models.ImageField( upload_to='media' )
    tutor_name=models.CharField(max_length=50)
    tutor_position=models.CharField(max_length=50)
    description=models.CharField(max_length=100)


class react_watch_video(models.Model):
    video=models.FileField(upload_to='media')
    video_thumb=models.FileField(upload_to='media')
    title=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    tutor_image=models.ImageField( upload_to='media' )
    tutor_name=models.CharField(max_length=50)
    tutor_position=models.CharField(max_length=50)
    description=models.CharField(max_length=100)

class python_watch_video(models.Model):
    video=models.FileField(upload_to='media')
    video_thumb=models.FileField(upload_to='media')
    title=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    tutor_image=models.ImageField( upload_to='media' )
    tutor_name=models.CharField(max_length=50)
    tutor_position=models.CharField(max_length=50)
    description=models.CharField(max_length=100)

class psql_watch_video(models.Model):
    video=models.FileField(upload_to='media')
    video_thumb=models.FileField(upload_to='media')
    title=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    tutor_image=models.ImageField( upload_to='media' )
    tutor_name=models.CharField(max_length=50)
    tutor_position=models.CharField(max_length=50)
    description=models.CharField(max_length=100)

class profile_details(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    image=models.FileField(blank=True,null=True,upload_to='images')

# class signup_form(models.Model):
#     username=models.CharField(max_length=50)
#     first_name=models.CharField(max_length=50)
#     second_name=models.CharField(max_length=50)
#     email=models.EmailField()
#     phone_number=models.BigIntegerField()
#     course=models.CharField(max_length=60)
#     student_id=models.CharField(max_length=30)