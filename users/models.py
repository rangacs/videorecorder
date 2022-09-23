from django.db import models  
class VideoLib(models.Model):  
    mobile = models.CharField(max_length=100)  
    name = models.EmailField()  
    file = models.FileField()
    file_b  = models.CharField(max_length=100, null=True)  
    user = models.IntegerField(default=0, null=True)
    status = models.CharField(max_length=10, null=True)  
    file_status = models.CharField(max_length=10, null=True)  
    file_b_status = models.CharField(max_length=10, null=True)  
    file_upload_time = models.DateTimeField(auto_now_add=True, null=True)
    file_b_upload_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:  
        db_table = "video_lib"