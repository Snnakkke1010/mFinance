from django.db import models    
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _ 
from .manager import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(max_length=255, unique=True, verbose_name=_("Email Address"))
    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    second_name = models.CharField(max_length=100, verbose_name=_("Second Name"))
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ["first_name", "second_name"]
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f'User: {self.email}'
    
    @property
    def get_full_name(self):
        return f'{self.first_name} {self.second_name}'
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    
    
class OneTimePassword(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    
    def __str__(self):
        return f'{self.user.first_name}--passcode'