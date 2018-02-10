from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Group, Message

# Create your tests here.
class ModelTestCase(TestCase):

    def setUp(self):
        self.groupname = "Random Man"
        self.description = "Just a random something"
        user = User.objects.create(username="user1")
        self.group = Group(groupname=self.groupname, description=self.description, group_creator=user)
    
    def test_model_can_create_a_group(self):
        old_count = Group.objects.count()
        self.group.save()
        new_count = Group.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="user2")
        self.client = APIClient()
        self.group_data = {'groupname': 'Random 1', 'users': user}
        self.response = self.client.post(
            reverse('group'),
            self.group_data,
            format="json"
        )
    
    def test_api_can_create_a_group(self):
        """Test the api has group creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_api_can_get_a_group(self):
        group = Group.objects.get()
        response = self.client.get(
            reverse('group'),
            kwargs={'pk': group.id},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, group)
    
    def test_api_can_update_group(self):
        self.groupname = "Random Man 2"
        self.description = "Just a random something"
        group = Group(groupname=self.groupname, description=self.description)
        group.save()
        change_new_group = {'groupname': 'Something new', 'description': 'Just a random something', 'users': [1]}
        res = self.client.put(
            reverse('details', kwargs={'pk': 1}),
            change_new_group, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)