from django.db import models

class Employee(models.Model):
    fullname = models.CharField(max_length=128)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)

# create    / insert  / add - post
# retrieve  /           fetch - get
# update    /           edit - put
# delete    /           remove - delete
