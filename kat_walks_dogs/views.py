from django.shortcuts import render
from rest_framework import views, permissions, viewsets
from .serializers import ReviewSerializer
from .models import Review

# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
