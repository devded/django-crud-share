from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import json


class TestMockApiView(APIView):
    def get(self, request):
        with open('staticfiles/asset/training-plan.json', 'r') as f:
            data = json.load(f)
        return Response(data)
