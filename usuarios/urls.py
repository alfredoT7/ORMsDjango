from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet,TeacherViewSet, UserNViewSet

router=DefaultRouter()
router.register(r'userN',UserNViewSet)
router.register(r'student',StudentViewSet)
router.register(r'teacher', TeacherViewSet)

urlpatterns=[
    path('nat-user', include(router.urls))
]