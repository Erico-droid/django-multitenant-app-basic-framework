from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from clients.models import Client
from clients.serializer import ClientSerializer


class ClientViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ClientSerializer

    def create(self, request):
        client = request.data or {}
        tenant_name = client.get('tenant_name')
        if tenant_name is None:
            raise ValidationError('A tenant name is mandatory.')
        tenant = Client.objects.get(tenant_name=tenant_name)
        serializer = self.serializer_class(tenant, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

def basepage(request):
    return render(request, "index.html")
