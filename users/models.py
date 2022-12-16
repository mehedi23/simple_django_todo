from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager  


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email')

        email = email.lower()

        user = self.model(
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email = email,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)







class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True, verbose_name="Email")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')

    USERNAME_FIELD = 'email'

    object = CustomUserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm , obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name_plural = 'User'