

# Register your models here.

from django.contrib import admin
from .models import Participant, Reservation

class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 1  
    readonly_fields = ("Reservation_date",)  
    autocomplete_fields = ('participant',)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "cin",
        "participant_category",
        "created_at",
        "updated_at",
    )
    
    search_fields = ("username", "first_name", "last_name", "email", "cin")
    list_per_page = 10
    ordering = ("created_at",)
    readonly_fields = ("created_at", "updated_at")
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('username', 'first_name', 'last_name', 'email', 'cin', 'participant_category')
        }),
        ('Tracking Data', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    inlines = [ReservationInline]
    list_filter = ('participant_category', 'created_at')
    list_editable = ('first_name', 'last_name')



class ReservationAdmin(admin.ModelAdmin):
    list_display=['conference','participant','confirmed','Reservation_date']
    actions=['confirmed','unconfirmed']

    def confirmed(self,request,queryset):
        queryset.update(confirmed=True)
        self.message_user(request,"les reservations sont confirmees")
    confirmed.short_description="reservation a confirmer"

    def unconfirmed(self,request,queryset):
        queryset.update(confirmed=True)
        self.message_user(request,"les reservations sont pas confirmees")
    unconfirmed.short_description="reservation a non confirmer"

admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Reservation, ReservationAdmin)


