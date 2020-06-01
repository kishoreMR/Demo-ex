from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'members',views.MembersViewset)
router.register(r'memberactivity',views.ActivityViewset)
#router.register(r'memact',views.MembersActViewset)

urlpatterns=[
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]
