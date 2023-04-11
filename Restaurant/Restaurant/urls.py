from django.urls import path, include
from rest_framework import routers
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from mainapp.views import *
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path
from mainapp.views import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
    ItemListCreateView,
    ItemRetrieveUpdateDestroyView,
    CartItemsListCreateView,
    CartItemsRetrieveUpdateDestroyView,
    TableListCreateView,
    TableRetrieveUpdateDestroyView,
    ReservationList,
    ReservationDetail,
    ContactList,
    ContactDetail,
    UserList,
    UserCreate,
    ReservationByUserList,
ObtainAuthToken,LoginView,LogoutView
)
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from mainapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('items/', ItemListCreateView.as_view(), name='item_list_create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item_retrieve_update_destroy'),
    path('items/<int:item_id>/reviews/', ItemReviewsList.as_view(), name='item_reviews_list'),
    path('cart_items/', CartItemsListCreateView.as_view(), name='cart_items_list_create'),
    path('cart_items/<int:pk>/', CartItemsRetrieveUpdateDestroyView.as_view(),name='cart_items_retrieve_update_destroy'),
    path('categories/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category_retrieve_update_destroy'),
    path('tables/', TableListCreateView.as_view(), name='table_list_create'),
    path('tables/<int:pk>/', TableRetrieveUpdateDestroyView.as_view(), name='table_retrieve_update_destroy'),
    path('tables/<int:table_id>/reservations/', ReservationList.as_view(), name='reservation_list_create'),
    path('contacts/', ContactList.as_view(), name='contact_list_create'),
    path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact_retrieve_update_destroy'),
    path('reviews/', ReviewListCreateView.as_view(), name='review_list_create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDeleteView.as_view(), name='review_retrieve_update_delete'),
    path('users/', UserList.as_view(), name='user_list_create'),
    path('users/create/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='api_login'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
#     path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
#     path('categories/<int:pk>/items/', ItemListCreateView.as_view(), name='category-item-list'),
#     path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-detail'),
#     path('items/<int:pk>/reviews/', ItemRetrieveUpdateDestroyView.as_view(), name='item-reviews'),
#     path('items/<int:pk>/add_to_cart/', ItemRetrieveUpdateDestroyView.as_view(), name='item-add-to-cart'),
#     path('cart_items/', CartItemsListCreateView.as_view(), name='cart-item-list-create'),
#     path('cart_items/<int:pk>/', CartItemsRetrieveUpdateDestroyView.as_view(), name='cart-item-detail'),
#     path('tables/', TableListCreateView.as_view(), name='table-list-create'),
#     path('tables/<int:pk>/', TableRetrieveUpdateDestroyView.as_view(), name='table-detail'),
#     path('reservations/', ReservationList.as_view(), name='reservation-list'),
#     path('reservations/<int:pk>/', ReservationDetail.as_view(), name='reservation-detail'),
#     path('users/', UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
#     path('users/<int:pk>/reservations/', ReservationByUserList.as_view(), name='user-reservation-list'),
#     path('contacts/', ContactList.as_view(), name='contact-list'),
#     path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# path("admin/", admin.site.urls),
# # Authentication
# path('items/<int:item_id>/reviews/', ItemReviewsList.as_view(), name='item_reviews_list'),
# path('api-auth/', include('rest_framework.urls')),
# path('token/', obtain_auth_token, name='api_token_auth'),
# path('login/', LoginView.as_view(), name='api_login'),
# path('logout/', LogoutView.as_view(), name='api_logout'),
#
# # Categories
# path('categories/', CategoryListCreateView.as_view(), name='category_list_create'),
# path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(),
#      name='category_retrieve_update_destroy'),
#
# # Items
# path('items/', ItemListCreateView.as_view(), name='item_list_create'),
# path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item_retrieve_update_destroy'),
#
# # Cart Items
# path('cart_items/', CartItemsListCreateView.as_view(), name='cart_items_list_create'),
# path('cart_items/<int:pk>/', CartItemsRetrieveUpdateDestroyView.as_view(),
#      name='cart_items_retrieve_update_destroy'),
#
# # Tables
# path('tables/', TableListCreateView.as_view(), name='table_list_create'),
# path('tables/<int:pk>/', TableRetrieveUpdateDestroyView.as_view(), name='table_retrieve_update_destroy'),
#
# # Reservations
# path('reservations/', ReservationList.as_view(), name='reservation_list_create'),
# path('reservations/<int:pk>/', ReservationDetail.as_view(), name='reservation_retrieve_update_destroy'),
#
# # Contacts
# path('contacts/', ContactList.as_view(), name='contact_list_create'),
# path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact_retrieve_update_destroy'),
# path('reviews/', ReviewListCreateView.as_view(), name='review_list_create'),
# path('reviews/<int:pk>/', ReviewRetrieveUpdateDeleteView.as_view(), name='review_retrieve_update_delete'),
# # Users
# path('users/', UserList.as_view(), name='user_list_create'),
# path('users/create/', UserCreate.as_view(), name='user_create'),