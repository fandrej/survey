from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, authentication, permissions
from rest_framework.permissions import IsAuthenticated

class Test(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response('HELLO WORLD!')
