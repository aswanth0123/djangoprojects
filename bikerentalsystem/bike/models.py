from django.db import models

class login(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    status = models.CharField(max_length=40)


class customerregistration(models.Model):
    cname = models.CharField(max_length=40)
    cage = models.CharField(max_length=40)
    caddress = models.CharField(max_length=40)
    cid = models.CharField(max_length=40)
    cemail = models.CharField(max_length=40)
    cphnumber = models.CharField(max_length=40)
    cusername = models.CharField(max_length=40)


class bikedetails(models.Model):
    bimage = models.FileField()
    bnumber = models.CharField(max_length=40)
    bname = models.CharField(max_length=40)
    bcompany = models.CharField(max_length=40)
    charge = models.CharField(max_length=40)
    bdiscription = models.CharField(max_length=40)
    bold = models.CharField(max_length=40)


class bookingdetails(models.Model):
    bookingdate = models.CharField(max_length=40)
    bikenumber = models.CharField(max_length=40)
    bookingname = models.CharField(max_length=40)
    bookingaddress = models.CharField(max_length=40)
    phnumber = models.CharField(max_length=40)
    pickupaddress = models.CharField(max_length=40)
    dropaddress = models.CharField(max_length=40)




