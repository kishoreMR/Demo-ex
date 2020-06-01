from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MembersSerializers,ActivitySerializers
from demo_app.models import Members,Activity
from drf_multiple_model.views import ObjectMultipleModelAPIView

# Create your views here.
#def index(request):
    #return render(request,'index.html')


class MembersViewset(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class=MembersSerializers

class ActivityViewset(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class=ActivitySerializers
