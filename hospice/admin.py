from django.contrib import admin

# Register your models here.
from hospice.models import Hospice,Patient,Admit


# Register your models here.
@admin.register(Hospice)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','city',)
    ordering = ('name',)
    search_fields = ('name','city',)
    list_filter = ('name', 'city',)
    
@admin.register(Patient)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','age',)
    ordering = ('name',)
    search_fields = ('name','age',)
    list_filter = ('name', 'age',)

@admin.register(Admit)
class EatsAdmin(admin.ModelAdmin):
    list_display = ('hsp','pname','admit_date',)
    ordering = ('hsp',)
    search_fields = ('hsp','pname','admit_date',)
    list_filter = ('hsp', 'pname','admit_date',)

