
from django.db import models

class cdetails(models.Model):
    cpics = models.ImageField(upload_to='images/')
    cname = models.CharField( max_length=50)
    cdet = models.CharField(max_length=500)

    def __str__(self):
        return str(self.id)+ "    " +self.cname
        #return self.cname +"--"+ self.cdet
    # def __str__(self):
    #     return self.cname
    # def __str__(self):
    #     return self.cdet
    
# class cdetails1(models.Model):
#     cpic = models.ImageField(height_field=4000, width_field=3000, max_length=10000)
#     cname = models.CharField(max_length=50)
#     cdetails = models.CharField(max_length=500)
    # def __str__(self):
    #     return self.cname
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now

class ldetails(models.Model):
    lpic = models.ImageField( max_length=100)
    lname = models.CharField(max_length=50)

    ldetails = models.CharField(max_length=500)
    def __str__(self):
        return self.lname+"--"+ self.ldetails
    
   