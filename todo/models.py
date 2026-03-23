from django.db import models

# Create your models here.
developer=[
        ("Anuj" ,"Anuj"),
        ("Sourav" ,"Sourav"),
        ]
category=[
        ("Work" ,"Work"),
        ("Personal" ,"Personal"),
        ("Urgent" ,"Urgent"),
        ("Long-term" ,"Long-term"),
        ]
prioritize=[
        ("High" ,"urgent"),
        ("Medium" ,"important but not urgent"),
        ("Low" ,"optional"),
        ]
class Task(models.Model):
    start_date=models.DateField()
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100,choices=category,blank=True)
    assigned=models.CharField(max_length=100,choices=developer,blank=True)
    prioritize=models.CharField(max_length=100,choices=prioritize,blank=True)
    end_date=models.DateField()
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='1. Task'