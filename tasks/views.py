# from django.shortcuts import render
# from rest_framework import viewsets
# from.models import Task
# from.serializers import TaskSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly


# class TaskViewSet(viewsets.ModelViewSet):
#     queryset=Task.objects.all()
#     serializer_class=TaskSerializer
#     permission_classes=[IsAuthenticatedOrReadOnly]

from rest_framework.response import Response
from rest_framework.views import APIView
from tasks.models import Task
from tasks.serializers import TaskSerializer
class vc1(APIView):
    def get(self, request):
        x = Task.objects.all()
        serializer = TaskSerializer(x, many=True)
        return Response(serializer.data)
class vc2(APIView):
    def get(self, request,id):
        x= Task.objects.get(id=id)
        serializer = TaskSerializer(x, many=False)
        return Response(serializer.data)
class vc3(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class vc4(APIView):
    def post(self, request,id):
        x=Task.objects.get(id=id)
        serializer = TaskSerializer(instance=x,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class vc5(APIView):
    def delete(self, request,id):
        x=Task.objects.get(id=id)
        x.delete()
        return Response('successfully delete')