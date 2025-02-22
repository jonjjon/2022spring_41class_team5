from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serializers import *


class userapi(APIView):
    def get(self, request):
        queryset = user.objects.all()
        serializer = userSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
        """
        if request.method == 'GET':
            queryset = user.objects.all()
            serializer = userSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = userSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
            
        elif request.method == 'PUT':
            serializer = userSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """
        
class progressapi(APIView):
    def get(self, request):
        queryset = progress.objects.all()
        print(queryset)
        serializer = progressSerializer(queryset, many=True)
        return Response(serializer.data)

class submitapi(APIView):
    def get(self, request):
        queryset = submit.objects.all()
        print(queryset)
        serializer = submitSerializer(queryset, many=True)
        return Response(serializer.data)
    
class problemapi(APIView):
    def get(self, request):
        queryset = problem.objects.all()
        print(queryset)
        serializer = problemSerializer(queryset, many=True)
        return Response(serializer.data)
    
class contentapi(APIView):
    def get(self, request):
        queryset = content.objects.all()
        print(queryset)
        serializer = contentSerializer(queryset, many=True)
        return Response(serializer.data)
# Create your views here.
