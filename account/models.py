from django.db import models
# from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     gender = models.CharField(max_length=50, null=True, blank=True)


#     REQUIRED_FIELDS = [
#         "first_name", "last_name", "gender", "email"
#     ]


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass