from rest_framework import viewsets

# Create your views here.

from .models import Student
from .serializer import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer
