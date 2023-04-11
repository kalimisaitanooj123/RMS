from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import authentication, permissions
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import UserSerializer
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# views.py
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Category, Item, Reviews, CartItems, Table, Reservation, Contact
from .serializers import CategorySerializer, ItemSerializer, ReviewsSerializer, CartItemsSerializer, TableSerializer, ReservationSerializer, ContactSerializer, UserSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.prefetch_related('item_set')

    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer=self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.prefetch_related('item_set')

    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance)
        return Response(serializer.data)
class ItemListCreateView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.prefetch_related('reviews_set')

    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer=self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.prefetch_related('reviews_set')

    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        cart_item=CartItems.objects.create(item=self.get_object(), user=request.user)
        serializer=CartItemsSerializer(cart_item)
        return Response(serializer.data)


class CartItemsListCreateView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]
    queryset=CartItems.objects.all()
    serializer_class=CartItemsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartItemsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]
    queryset=CartItems.objects.all()
    serializer_class=CartItemsSerializer


class TableListCreateView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]
    queryset=Table.objects.all()
    serializer_class=TableSerializer


class TableRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]
    queryset=Table.objects.all()
    serializer_class=TableSerializer


class ReservationList(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAdminUser]
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAdminUser]
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

class ContactList(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer

class UserList(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=User.objects.all()
    serializer_class=UserSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[AllowAny]
    queryset=User.objects.all()
    serializer_class=UserSerializer

    def post(self, request, *args, **kwargs):
        response=super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user=User.objects.get(username=request.data['username'])
            token, created=Token.objects.get_or_create(user=user)
            return Response({'token':token.key}, status=status.HTTP_201_CREATED)
        return response




class ObtainAuthToken(APIView):
    def post(self, request, *args, **kwargs):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username, password=password)
        if not user:
            return Response({'error':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        token, created=Token.objects.get_or_create(user=user)

        return Response({'token':token.key})

class LoginView(APIView):
    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            user=authenticate(username=serializer.validated_data['username'],
                                password=serializer.validated_data['password'])
            if user is not None:
                token, created=Token.objects.get_or_create(user=user)
                return Response({'token':token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response(status=204)


class ReservationByUserList(generics.ListAPIView):
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAdminUser]
    serializer_class=ReservationSerializer

    def get_queryset(self):
        user=self.kwargs['pk']
        return Reservation.objects.filter(user=user)




class ReviewListCreateView(generics.ListCreateAPIView):
    queryset=Reviews.objects.all()
    serializer_class=ReviewsSerializer
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAdminUser]

class ReviewRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Reviews.objects.all()
    serializer_class=ReviewsSerializer
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAdminUser]



class ItemReviewsList(ListAPIView):
    serializer_class=ReviewsSerializer

    def get_queryset(self):
        item_id=self.kwargs['item_id']
        return Reviews.objects.filter(item_id=item_id)