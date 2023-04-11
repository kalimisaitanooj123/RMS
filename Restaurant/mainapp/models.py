from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinLengthValidator

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name



class Item(models.Model):
    LABELS = (
        ('Best Selling Foods', 'Best Selling Foods'),
        ('New Food', 'New Food'),
        ('Spicy Foods🔥', 'Spicy Foods🔥'),
    )

    LABEL_COLOUR = (
        ('danger', 'danger'),
        ('success', 'success'),
        ('primary', 'primary'),
        ('info', 'info'),
        ('warning', 'warning'),
    )
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=25000, blank=True)
    price = models.FloatField()
    instructions = models.CharField(max_length=25000, default="Available")
    image = models.ImageField(default='default.png', upload_to='images/')
    labels = models.CharField(max_length=25, choices=LABELS, blank=True)
    label_colour = models.CharField(max_length=15, choices=LABEL_COLOUR, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(default="foods")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:dishes", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("main:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_item_delete_url(self):
        return reverse("main:item-delete", kwargs={
            'slug': self.slug
        })

    def get_update_item_url(self):
        return reverse("main:item-update", kwargs={
            'slug': self.slug
        })




class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rslug = models.SlugField()
    review = models.TextField()
    posted_on = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.review


class CartItems(models.Model):
    ORDER_STATUS = (
        ('Active', 'Active'),
        ('Delivered', 'Delivered')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    ordered_date = models.DateTimeField(default=timezone.now,null=True,blank=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Active')


    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def __str__(self):
        return self.item.title

    def get_remove_from_cart_url(self):
        return reverse("main:remove-from-cart", kwargs={
            'pk': self.pk
        })

    def update_status_url(self):
        return reverse("main:update_status", kwargs={
            'pk': self.pk
        })




class Table(models.Model):
    table_number = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    is_booked = models.CharField(max_length=200,default='Available',null=True)

    def __str__(self):
        return str(self.table_number)

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    table_number = models.ForeignKey(Table,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} - Table {self.table_number} - {self.date} {self.time}"






class Contact(models.Model):
    name = models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    comments = models.CharField(max_length=100)
    phone=models.IntegerField(null=True)

    def __str__(self):
        return self.name



