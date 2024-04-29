from django.shortcuts import render
from .models import UserN, Teacher, Student
from .serializers import StudentSerializer,TeacherSerializer, UserNSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status



class TeacherViewSet(viewsets.ViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer

class StudentViewSet(viewsets.ViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class UserNViewSet(viewsets.ViewSet):
    queryset=UserN.objects.all()
    serializer_class=UserNSerializer

    