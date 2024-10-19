from django.db import models
from categories.models import Category
from django.utils import timezone
# Create your models here.
from django.core.validators import MaxValueValidator,FileExtensionValidator
from django.core.exceptions import ValidationError


class Conference(models.Model):
    description=models.TextField()
    title=models.CharField(max_length=255)
    program=models.FileField(upload_to='files/',validators=[FileExtensionValidator(allowed_extensions=['pdf','png','jpg','jpeg'],message='only pdf,png,jpg,jpeg are allowed')])

    start_date=models.DateField(default=timezone.now().date())
    end_date=models.DateField()
    location=models.CharField(max_length=255)
    price=models.FloatField()
    capacity=models.IntegerField(validators=[MaxValueValidator(limit_value=900,message='capacity must be under 900')])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="conferences")
    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError('end date must be after start date')
    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(
                    start_date__gte=timezone.now().date()
                ),
                name="the start date must be equal or greater than today"
            )
        ]
    def __str__(self):
        return (f"title conference {self.title} : {self.location}")