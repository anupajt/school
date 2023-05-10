from django.db import models



from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    address = models.TextField()
    department = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    materials = models.TextField()

    def __str__(self):
        return self.name
