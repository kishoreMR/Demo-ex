from django.db import models


class Members(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    real_name = models.CharField(max_length=264)
    tz = models.CharField(max_length=264)



class Activity(models.Model):
    name = models.ForeignKey(Members,on_delete=models.CASCADE)
    starttime = models.DateField()
    endtime = models.DateField()
