# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job_advert, Job_application
from .serializers import Job_advertSerializer
from .serializers import Job_applicationSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.authentication import JWTAuthentication
from account.permissions import IsAdminOrReadOnly



class Job_advertView(APIView):
    """
    Retrive all or create new job advert instances
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get(self, request, format=None):
        """ Use this method to get all job advert instances"""

        objs = Job_advert.objects.all() #get data
        serializers = Job_advertSerializer(objs, many=True)

        data = {
            "message" : "success",
            "data_count" : objs.count(),
            "data" : serializers.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method= "post", request_body=Job_advertSerializer())
    @action(methods=["POST"], detail=True)
    
    def post(self, request, format=None):

            serializer = Job_advertSerializer(data=request.data)
            #get the data and deserialization

            if serializer.is_valid():
                serializer.save()

                data = {
                    "message" :"success"
                    }               
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                data = {
                    "message" :"failed",
                    "error" : serializer.error
                }

                return Response(data, status=status.HTTP_400_BAD_REQUEST)


class Job_advertDetailView(APIView):
    """
    Retrive, update or delete a job advert instance..
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get_object(self, job_advert_id):
        """"Get a single instance using the provided job_advert_id""" 

        try:
            return Job_advert.objects.get(id=job_advert_id)
        except Job_advert.DoesNotExist:
            raise NotFound(detail = {"message", "job advert not found"})
        
    def get(self, request, job_advert_id, format=None):
        obj = self.get_object(job_advert_id)
        serializer = Job_advertSerializer(obj)

        data = {
            "message" :"success",
            "data" : serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(method="put", request_body=Job_advertSerializer())
    @action(methods=["PUT"], detail=True)
    def put(self, request, job_advert_id, format=None):
        obj = self.get_object(job_advert_id)
        serializer = Job_advertSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message" :"success"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "message" :"failed",
                "errors":serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(method="delete")
    @action(methods=["DELETE"], detail=True)
    def delete(self, request, job_advert, formart=None):
        obj = self.get_object(job_advert)
        if obj.products.count() == 0:

            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        raise PermissionDenied(detail={"message": "cannot delete this category because it contains live job applications."})









class Job_applicationView(APIView):
    """
    Retrive all or create new job applications instances
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get(self, request, format=None):
        """ Use this method to get all job application instances"""

        objs = Job_application.objects.all() #get data
        serializers = Job_applicationSerializer(objs, many=True)

        data = {
            "message" : "success",
            "data_count" : objs.count(),
            "data" : serializers.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method= "post", request_body=Job_applicationSerializer())
    @action(methods=["POST"], detail=True)
    
    def post(self, request, format=None):

            serializer = Job_applicationSerializer(data=request.data)
            #get the data and deserialization

            if serializer.is_valid():
                serializer.save()

                data = {
                    "message" :"success"
                    }               
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                data = {
                    "message" :"failed",
                    "error" : serializer.error
                }

                return Response(data, status=status.HTTP_400_BAD_REQUEST)




class Job_applicationDetailView(APIView):
    """
    Retrive, update or delete a job application instance..
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get_object(self, job_application_id):
        """"Get a single instance using the provided job_application_id""" 

        try:
            return Job_application.objects.get(id=job_application_id)
        except Job_application.DoesNotExist:
            raise NotFound(detail = {"message", "Job application not found"})
        
    def get(self, request, job_application_id, format=None):
        obj = self.get_object(job_application_id)
        serializer = Job_applicationSerializer(obj)

        data = {
            "message" :"success",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(method="put", request_body=Job_applicationSerializer())
    @action(methods=["PUT"], detail=True)
    def put(self, request, job_application_id, format=None):
        obj = self.get_object(job_application_id)
        serializer = Job_applicationSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message" :"success"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "message" :"failed",
                "errors":serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(method="delete")
    @action(methods=["DELETE"], detail=True)
    def delete(self, request, job_application, formart=None):
        obj = self.get_object(job_application)
        if obj.products.count() == 0:

            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        raise PermissionDenied(detail={"message": "cannot delete this category because it contains live job applications."})


