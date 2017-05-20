from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from .models import Task
from .serilizers import TaskSErilizer


 # api/getAllTaks/

class TaskList(APIView):

     def get(self,request):
         try:
            id = request.GET['id']
         except:
             tasks = Task.objects.all()
             serilizer = TaskSErilizer(tasks, many=True)
             return Response({'data': serilizer.data, 'error': '', 'message': "Sucessfully"})
         else:
             tasks = Task.objects.all().filter(id=id)
             serilizer = TaskSErilizer(tasks, many=True)
             return Response({'data': serilizer.data, 'error': '', 'message': "Sucessfully"})


     def post(self,request):
         serializer = TaskSErilizer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response( {'data':serializer.data,'message':"Sucessfully",'error':''})
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



     def delete(self,id):
         try:
             data = int(id.data['id'])
         except :
             return Response({'data':'', 'error': 'Invalid Parameter', 'message': 'Failed'})
         else:
             value = Task.objects.all().filter(id=data)
             if value:
                 value.delete()
                 return Response({'data': '', 'error': '', 'message': 'Taks with id = ' + str(data) + ' Sucessfully Deleted'})
             else:
                 return Response({'data': '', 'error': 'Task with id '+str(data)+' Not Found', 'message': ''})

     def put(self,object):
         try:
             id = int(object.data['id'])
         except:
             return Response({'data':'', 'error': 'Invalid Parameter', 'message': 'Failed'})
         else:
             task = Task.objects.all().filter(id=id)
             serializer = TaskSErilizer(data=task,many=False)
             if serializer.is_valid():
                 serializer.name = object.data['name']
                 serializer.date = object.data['date']
                 serializer.save()
                 return Response({'data': serializer.data, 'message': "Sucessfully", 'error': ''})
             else:
                 return Response({'data': '', 'error': 'Task with id ' + str(id) + ' Not Found', 'message': ''})



