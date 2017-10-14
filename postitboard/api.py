from rest_framework.viewsets import ModelViewSet

from .serializers import GroupSerializer, MessageSerializer
from .models import Group, Message

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(group = self.request.query_params.get('group'))
