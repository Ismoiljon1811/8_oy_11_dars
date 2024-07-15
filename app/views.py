from django.shortcuts import render

from .models import Cost

from .serializer import CostSerializer

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class CostAllGetView(ListAPIView):
    serializer_class = CostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Cost.objects.filter(user=user) 
        return queryset