from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

class Book(models.Model):
    FICTION = 'FIC'
    NON_FICTION = 'NON'
    SCIENCE = 'SCI'
    TECHNOLOGY = 'TECH'
    BUSINESS = 'BUS'
    SELF_HELP = 'SELF'
    BIOGRAPHY = 'BIO'
    HISTORY = 'HIST'
    
    TOPIC_CHOICES = [
        (FICTION, 'Fiction'),
        (NON_FICTION, 'Non-Fiction'),
        (SCIENCE, 'Science'),
        (TECHNOLOGY, 'Technology'),
        (BUSINESS, 'Business'),
        (SELF_HELP, 'Self Help'),
        (BIOGRAPHY, 'Biography'),
        (HISTORY, 'History'),
    ]

    NOT_STARTED = 'NS'
    READING = 'RD'
    COMPLETED = 'CP'
    
    STATUS_CHOICES = [
        (NOT_STARTED, 'Not Started'),
        (READING, 'Reading'),
        (COMPLETED, 'Completed'),
    ]

    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Rating must be at least 1"),
            MaxValueValidator(100, message="Rating cannot exceed 100")
        ],
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    cover = models.ImageField(null=True, blank=True)
    topic = models.CharField(
        max_length=4,
        choices=TOPIC_CHOICES,
        default=None,
    )
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=NOT_STARTED,
    )
    
    class Meta:
        ordering = ["-created_at"]

    #constructor
    def __str__(self):
        return(f"{self.name} by {self.author}")
