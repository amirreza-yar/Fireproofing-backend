from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.hashers import make_password

import datetime as dt

class UserProfileManager(BaseUserManager):
    """
        Custom user manager, operates with email only
    """
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    A custom user model to work with email only, FUCK EMAIL!
    """

    # username = None
    username = models.CharField(max_length=255, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(_("email address"), blank=True)
    phone_number = models.IntegerField(blank=False)
    address = models.CharField(max_length=2000, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(blank=True,null=True)
    field = models.CharField(max_length=60,blank=True, null=True)
    education = models.CharField(max_length=200,blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    image_profile = models.ImageField(upload_to='profileImage/',blank=True,null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone_number"]

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserProfileManager()

    def __str__(self):
        """ Return string representation of our user """
        return self.username

    # def clean(self):
    #     super().clean()
    #     self.email = self.__class__.objects.normalize_email(self.email)

    def get_name(self):
        return self.name

    def get_profile(self):
        return f"media/{self.image_profile}"

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

class ResetPassword(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    secret = models.CharField(max_length=32, unique=True)
    # created_time = models.TimeField(default=dt.datetime.now())
    expiration_time = models.TimeField(default=dt.datetime.now() + dt.timedelta(minutes=2))

    def is_expired(self):
        if dt.datetime.now() > self.expiration_time:
            return True
        else:
            return False