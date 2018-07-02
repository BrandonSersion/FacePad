import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


# TODO create seperate UserProfile model to hide
# sensitive information from standard users.
@python_2_unicode_compatible
class User(AbstractUser):
    """
    User account information. Primary key UUIDField.
    Email address, username, and password required.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # override AbstractUser email to blank=False
    email = models.EmailField(_('email address'), blank=False)
    date_of_birth = models.DateField(null=True)
    friends = models.ManyToManyField(
        'self',
        through='Friend',
        symmetrical=False,
        related_name='related_to',
        blank=True,
    )

    def __str__(self):
        return self.username


class Content(models.Model):
    """
    Content items users posted on their profile.
    All fields required.
    """
    id = models.AutoField(primary_key=True)
    file_upload = models.FileField(upload_to='files/')
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Rate(models.Model):
    """
    Ratings users gave to their friends' content items.
    One rating per user per content item.
    All fields requireed.
    """
    RATE_CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),)
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    value = models.IntegerField(choices=RATE_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} rated "{self.content}" {self.value}'


class Comment(models.Model):
    """
    Comments users posted to their friends' content items.
    All fields required.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comment by {self.user} on {self.content}'


class Friend(models.Model):
    """
    Users who the user friended. One way relationship,
    you can friend someone without them friending you back.
    All fields required.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user'
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='to_user'
    )

    def __str__(self):
        return f'{self.user} friended {self.recipient}'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Login token authorization.
    """
    if created:
        Token.objects.create(user=instance)
