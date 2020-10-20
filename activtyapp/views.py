from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from .models import Status,Members,ActivityPeriod
# ,CustomUser
from django.contrib.auth.models import User
from .serializers import StatusSerializers,MembersSerializers,ActivityPeriodSerializers,UserSerializers
from rest_framework import viewsets

class ActivityPeriodAPI(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class =ActivityPeriodSerializers
    paginate_by = None

class MembersAPI(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class =MembersSerializers
    paginate_by = None

class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =UserSerializers
    paginate_by = None

class StatusAPI(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class =StatusSerializers
    paginate_by = None


# class ActivityList(APIView):
#     """
#     get:
#     Return the given match.

#     post:
#     Create a new match instance.
#     """
#     def get(self,request):
#         queryset=ActivityPeriod.objects.all()
#         serializer=ActivityListsSerializers(queryset,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer=ActivityListsSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
