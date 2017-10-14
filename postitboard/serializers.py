from rest_framework import serializers
from .models import Group, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = '__all__'
