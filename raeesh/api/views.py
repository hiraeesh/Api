
from .models import Student
# Create your views here.
from .serializers import  StudentSerializer

from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class Born_To_Be_A_Programmer(viewsets.ModelViewSet):
   
    queryset = Student.objects.all()
    serializer_class =StudentSerializer
  
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
  