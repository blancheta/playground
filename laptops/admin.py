from django.contrib import admin
from django.utils.safestring import mark_safe

from laptops.models import Laptop, Vendor, Question, Answer


class LaptopAdmin(admin.ModelAdmin):

    actions = ["make_published"]

    @admin.action(description="Mark selected stories as published")
    def make_published(self, request, queryset):
       print("Hello")


admin.site.register(Laptop, LaptopAdmin)


class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'overview_link']

    def overview_link(self, obj):
        return mark_safe(f'<a href="/admin/laptops/overview/?vendor_id={obj.id}">See overview</a>')


admin.site.register(Vendor, VendorAdmin)

# To allow us to use two change list for the laptop model else not possible
class Overview(Laptop):
    class Meta:
        proxy = True

class LaptopCustomListAdmin(admin.ModelAdmin):
    change_list_template = 'admin/laptop/payment_overview.html'
    model = Overview

    def has_add_permission(self, request):
        return False

    list_display = ['name', "brand"]


admin.site.register(Overview, LaptopCustomListAdmin)
admin.site.register(Question)
admin.site.register(Answer)