from rest_framework import serializers
from .models import Status,Members,ActivityPeriod
# ,CustomUser
from django.contrib.auth.models import User
class ActivityPeriodSerializers(serializers.ModelSerializer):
    class Meta:
        model=ActivityPeriod
        fields='__all__'


class UserSerializers(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    # username = serializers.Field(source='user.username')
    # user = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['username',]

        
class MembersSerializers(serializers.ModelSerializer):
    # tz=serializers.SerializerMethodField()
    
    # tz = serializers.CharField(source='get_tz_display')
    # tz = serializers.ChoiceField(choices=Members.TIMEZONES)
    real_name = serializers.CharField(source='real_name.username', read_only=True)
    # tz = serializers.CharField(source='tz', read_only=True)
    activityperiod=ActivityPeriodSerializers(many=True,read_only=True)
    user=UserSerializers(many=True,read_only=True)
    
    class Meta:
        model=Members
        fields='__all__'
        # depth=2
    # def get_tz(self,obj):
    #     return obj.get_tz_display()


        
class StatusSerializers(serializers.ModelSerializer):
    members=MembersSerializers(many=True,read_only=True)
    activityperiod=ActivityPeriodSerializers(many=True,read_only=True)
    user=UserSerializers(many=True,read_only=True)
    class Meta:
        model=Status
        fields='__all__'
        # depth=4