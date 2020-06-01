from demo_app.models import Members,Activity
from rest_framework.serializers import ModelSerializer

class MembersSerializers(ModelSerializer):
    class Meta:
        model = Members
        fields =('id','real_name','tz')

class ActivitySerializers(ModelSerializer):
    name=MembersSerializers()
    class Meta:
        model = Activity
        fields =('name','starttime','endtime')
