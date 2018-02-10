from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Group model containing groupname and description
class Group(models.Model):
    groupname = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    group_creator = models.ForeignKey('auth.User',
    related_name='group_creator',
    on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Group: {}".format(self.groupname)

# Message model
class Message(models.Model):
    message_priority = (
        ('N', 'Normal'),
        ('U', 'Urgent'),
        ('C', 'Critical')
    )
    content = models.TextField()
    priority = models.CharField(max_length=1, choices=message_priority)
    readcheck = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return "Message: {}".format(self.content)