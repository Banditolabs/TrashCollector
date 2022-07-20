from django.db import models
from django.urls import reverse

ACTIONS = (
    ('A', 'Admire'),
    ('D', 'Devour'),
    ('B', 'Bathe'),  
)
USES = (
    ('N', 'None'),
    ('S', 'Smashing'),
    ('C', 'Cutting'),
    ('T', 'Tricking'),
    ('M', 'Moving'),
    ('E', 'Eating')
)
RATINGS = (
    ('N', 'None'),
    ('E', 'Effective'),
    ('M', 'Mediocre'),
    ('P', 'Poor')
)

# Create your models here.

class Use(models.Model):
    use = models.CharField(
        max_length=50,
        choices=USES,
        default=USES[0][0]
        )
    rating = models.CharField(
        max_length=50,
        choices=RATINGS,
        default=RATINGS[0][0]
        )

    def __str__(self):
        return f"{self.get_use_display()}"

    def get_absolute_url(self):
        return reverse('use_detail', kwargs={'pk': self.id})

class Trash(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    uses = models.ManyToManyField(Use)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
    # reverse takes the name key of the page and Kwargs to reverse engineer the url to forward to upon success.
    # this is a fallback in case of no success_url
        return reverse('detail', kwargs={'trash_id': self.id})
    
    
class Feeding(models.Model):
    date = models.DateField('Wut was th day')
    meal = models.CharField(
        max_length=1,
        choices=ACTIONS,
        default=ACTIONS[0][0]
    )
    trash = models.ForeignKey(Trash, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining a Field.choice
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']