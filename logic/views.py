from rest_framework import generics

from .models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # permission_classes = ['IsAuthenticated']
# class PersonAPIList(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#     permission_classes = ['IsAuthenticated']
#
#
# class PersonAPIUpdate(generics.UpdateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#     permission_classes = ['IsAdminUser']
#
#
# class PersonAPIDestroy(generics.DestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#     permission_classes = ['IsAdminUser']






