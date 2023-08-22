from django.db import models


class NewUser(models.Model):
    uid = models.IntegerField()
    uname = models.CharField(max_length=255)
    uemail = models.EmailField()
    urole = models.CharField(max_length=255)

    class Meta:
        db_table = "users"
