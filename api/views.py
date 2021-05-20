from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny , IsAdminUser
from django.contrib.auth.models import User

# Create your views here.
class UserCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class StudentViewSet(viewsets.ViewSet):
    authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]


    def List(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)


    def retrieve(self,request,pk=None):
        if pk is not None:
            stu = Student.objects.get(id = pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)


    def create(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    def update(self,request,pk=None):
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complate data update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self,request,pk):
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data update'})
        return Response(serializer.errors)


    def destroy(self,request,pk):
        stu = Student.objects.get(id = pk)
        stu.delete()
        return Response({'msg':'data delete successfully'})


# check costom function ---------------------------------

    @action(detail = True,methods=['GET'])
    def change(self,request,pk=None):
        if pk is not None:
            stu = Student.objects.get(id = pk)
            stu.city = 'yyy'
            stu.save()
            serializer = StudentSerializer(stu)
            return Response({'msg':'success'},status=status.HTTP_200_OK)


    @action(detail=True, methods=['GET'])
    def change_again(self, request, pk=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)
            stu.city = 'zzz'
            stu.save()
            serializer = StudentSerializer(stu)
            return Response({'msg': 'success'}, status=status.HTTP_200_OK)




#--------------------------------- Model View Set------------------------------
#
# class Studentapi(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # authentication_classes = [BaseAuthentication]
#     # permission_classes = [AllowAny]
#
#     @action(detail = True, methods=['GET'])
#     def change_again(self, request, pk=None):
#         if pk is not None:
#             stu = Student.objects.get(id=pk)
#             stu.city = 'zzz'
#             stu.save()
#             serializer = StudentSerializer(stu)
#             return Response({'msg': 'success'}, status=status.HTTP_200_OK)
#




#-------------------------- GENERIC VIEW ------------------------------------------

from rest_framework.generics import GenericAPIView

from rest_framework.mixins import ListModelMixin , CreateModelMixin  , RetrieveModelMixin , UpdateModelMixin


class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)



class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentReriave(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    @action(detail=True, methods=['GET'])
    def change_again(self, request, pk=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)
            stu.city = 'zzz'
            stu.save()
            serializer = StudentSerializer(stu)
            return Response({'msg': 'success'}, status=status.HTTP_200_OK)










