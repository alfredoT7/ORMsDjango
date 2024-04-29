from rest_framework import serializers
from .models import Student,Teacher,UserN
from decimal import Decimal

class StudentSerializer(serializers.Serializer):
    class Meta:
        model= Student
        fields='__all__'

class TeacherSerializer(serializers.Serializer):
    class Meta:
        model=Teacher
        fields='__all__'

class UserNSerializer(serializers.Serializer):
    class Meta:
        model= UserN
        fields='__all__'


