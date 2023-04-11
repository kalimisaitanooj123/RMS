from django.contrib import admin
from .models import Category,Item,Reviews,CartItems,Table,Reservation,Contact


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('name',)}


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('title',)}
    list_display=['title','price','category']
    list_filter=['category']


class ReviewsAdmin(admin.ModelAdmin):
    list_display=['user','item','posted_on']


class CartItemsAdmin(admin.ModelAdmin):
    list_display=['user','item','quantity','ordered_date','status']
    list_filter=['ordered','status']


class TableAdmin(admin.ModelAdmin):
    list_display=['table_number','capacity','is_booked']


class ReservationAdmin(admin.ModelAdmin):
    list_display=['name','phone_number','email','table_number','date','time','party_size']
    list_filter=['table_number','date']


class ContactAdmin(admin.ModelAdmin):
    list_display=['name','Email','comments','phone']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Reviews,ReviewsAdmin)
admin.site.register(CartItems,CartItemsAdmin)
admin.site.register(Table,TableAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Contact,ContactAdmin)
