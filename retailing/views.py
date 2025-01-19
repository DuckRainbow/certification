from django.http import Http404
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from retailing.models import Contact, Product, Supplier
from callboard.paginators import CustomPagination
from callboard.serializers import AdSerializer, FeedbackSerializer, AdDetailSerializer
from users.permissions import IsAdmin, IsAuthor