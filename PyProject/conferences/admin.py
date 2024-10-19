from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Conference
from users.models import *
from django.db.models import Count
# Register your models here.
class ReservationInline(admin.TabularInline):
    model=Reservation
    extra=1
    readonly_fields=('Reservation_date',)
    can_delete=True
class ConferenceDateFilter(admin.SimpleListFilter):
    title='date conf filter'
    parameter_name='conference_date'
    def lookups(self, request, model_admin):
        return (
            ('past','past conf'),
            ('today','tofay conf'),
            ('upcoming','upcoming conf'),
        )
    def queryset(self, request, queryset):
        if self.value()=='past':
            return queryset.filter(end_date__lt=timezone.now().date())
        if self.value()=='today':
            return queryset.filter(start_date=timezone.now().date())
        if self.value()=='upcoming':
            return queryset.filter(start_date__gt=timezone.now().date())

class ParticipantFilter(admin.SimpleListFilter):
    title="participant filter"
    parameter_name="participants"

    def lookups(self, request,admin_model):
        return (
            ('0',('No participants')),
            ('more',('More participants'))
        )

    def queryset(self,request,queryset):
        if self.value()=='0':
            return queryset.filter(Reservations__isnull=True)
        if self.value()=='more':
            return queryset.filter(Reservations__isnull=False)
        return queryset
class conferenceAdmin(admin.ModelAdmin):
    list_display=('title','location','start_date','end_date','price')
    search_fields=('title',)
    list_per_page=2
    ordering=('start_date','title')
    fieldsets=(
        ('description',{
            'fields':('title','description','category','location')
        }),
        ('horaires',{
            'fields':('start_date','end_date','created_at','updated_at')
        }),
        ('Documents',{
            'fields':('program',)
        })
    )
    readonly_fields=('created_at','updated_at') #car les attributs sont pas modifiables
    inlines=[ReservationInline]
    autocomplete_fields=('category',)
    list_filter=('title',ParticipantFilter)
admin.site.register(Conference,conferenceAdmin) #(modele,classe de personnalisation du modele)
"""
    def queryset(self,request,queryset):
        if self.value()=='0': #on a fait la liasion many to many dans la classe participant, annotate pour calculer
            return queryset.annotate(Participant_count=Count('Reservations')).filter(Participant_count=0)
        if self.value()=='more':
            return queryset.annotate(Participant_count=Count('Reservations')).filter(Participant_count__gt=0)
        return queryset
"""