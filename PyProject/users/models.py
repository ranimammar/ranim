from django.db import models
from django.contrib.auth.models import AbstractUser
from conferences.models import Conference
# Create your models here.
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
def email_validator(value):
    if not value.endswith('@esprit.tn'):
        raise ValidationError('Email invalid')
class Participant(AbstractUser):
    cin_validator=RegexValidator(regex=r'^\d{8}$',message='only numbers are allowed') #{8},{1,8},{1,} on n'a pas un min,{,8}
    cin=models.CharField(primary_key=True,max_length=8,validators=[cin_validator])
    email=models.EmailField(unique=True,max_length=255,validators=[email_validator])
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    username=models.CharField(unique=True,max_length=255)
    USERNAME_FIELD='username' #l'authentification
    CHOICES=(
        ('etudiant','etudiant'),
        ('chercheur','chercheur'),
        ('docteur','docteur'),
        ('enseignant','enseignant')
    )
    participant_category=models.CharField(max_length=255,choices=CHOICES)
    reservations = models.ManyToManyField(Conference,through='Reservation',related_name='Reservations')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural="Participants"



class Reservation(models.Model):
   conference=models.ForeignKey(Conference,on_delete=models.CASCADE)
   participant=models.ForeignKey(Participant,on_delete=models.CASCADE)
   confirmed=models.BooleanField(default=False)
   Reservation_date=models.DateTimeField(auto_now_add=True)
   def clean(self):
       if self.conference.start_date < timezone().now().date():
           raise ValidationError('you can only reserve for upcoming conference')
       Reservation_count=Reservation.objects.filter(
           Participant=self.participant,
           Reservation_date__date=timezone.now().date())
       if Reservation_count>=3:
           raise ValidationError("You can on ly make 3re per day")
       
   class Meta :
      unique_together=('conference','participant')
    