from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .serializers import GroupSerializer, MessageSerializer
from .models import Group, Message

class GroupViewSet(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

