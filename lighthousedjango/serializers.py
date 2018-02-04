from rest_framework import serializers
from lighthousedjango.models import Event, User

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('start', 'end', 'title', 'description', 'calendar_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'hashed_password', 'blocked_websites', 'totals')

