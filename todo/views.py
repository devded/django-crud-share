from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TodoModelV2

# Create your views here.

class BaseApiView(APIView):
    def get(self, request):
        return Response("Hello World")

class CreateTodoApiView(APIView):

    def get(self, request):
        return Response("Hello")


    def post(self, request):
        # data = request.data
        # # return Response(data)
        # # try:
        # #      res = models.TodoModel.objects.create(title=data)
        # #      return Response("Create Successfully")
        # # except Exception as e:
        # #     return Response(e)

        TodoModelV2.objects.create(title="gi")
        return Response("Create Successfully")

        