from rest_framework import serializers
from .models import Category,Item,Reviews,CartItems,Table,Reservation,Contact
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import datetime

from django.utils import timezone

class ReadOnlyDateTimeField(serializers.DateTimeField):
    def to_representation(self,value):
        if not timezone.is_aware(value):
            value=timezone.make_aware(value,timezone.get_current_timezone())
        value=timezone.localtime(value)
        return super().to_representation(value)



class UserSerializer(serializers.ModelSerializer):
    token=serializers.SerializerMethodField()

    class Meta:
        model=User
        fields=('id','username','email','password','token')
        extra_kwargs={'password': {'write_only': True}}

    def get_token(self,obj):
        token,created=Token.objects.get_or_create(user=obj)
        return token.key

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        read_only_fields=['created_at','updated_at']


class ItemSerializer(serializers.ModelSerializer):
    category_name=serializers.ReadOnlyField(source='category.name')
    category_slug=serializers.ReadOnlyField(source='category.slug')
    created_by=UserSerializer(read_only=True)
    class Meta:
        model=Item
        fields='__all__'
        read_only_fields=['slug']


class ReviewsSerializer(serializers.ModelSerializer):
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    item=serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    class Meta:
        model=Reviews
        fields='__all__'



class CartItemsSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    item=ItemSerializer(read_only=True)
    item_id=serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(),source='item')
    ordered_date=ReadOnlyDateTimeField(read_only=True)
    class Meta:
        model=CartItems
        fields=['id','user','item','item_id','ordered','quantity','ordered_date','status']
        read_only_fields=['ordered_date']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields='__all__'


class ReservationSerializer(serializers.ModelSerializer):
    table_number=TableSerializer()
    class Meta:
        model=Reservation
        fields='__all__'

    def create(self,validated_data):
        table_data=validated_data.pop('table_number')
        table=Table.objects.create(**table_data)
        reservation=Reservation.objects.create(table_number=table,**validated_data)
        return reservation


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'



class CartItemsSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    item=ItemSerializer(read_only=True)
    item_id=serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(),source='item')
    ordered_date=ReadOnlyDateTimeField(read_only=True)
    class Meta:
        model=CartItems
        fields=['id','user','item','item_id','ordered','quantity','ordered_date','status']
        read_only_fields=['ordered_date']


