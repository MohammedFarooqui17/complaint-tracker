from django.db import models

from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('superadmin', 'Super Admin'),
    ]

    name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    department = models.CharField(max_length=100 , null=True)
    location = models.CharField(max_length=100)
    issue_raise_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    tat = models.IntegerField()
    due_date = models.DateTimeField()
    emp_code = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    emp_level = models.CharField(max_length=10, default='L0')  # Default value set
    password = models.CharField(max_length=128, default='default_password')  # Temporary default

    def __str__(self):
        return self.name




class Complaint(models.Model):
    COMPLAINT_STATUS_CHOICES = [
        ('done', 'Done'),
        ('wip', 'Work in Progress'),
        ('overdue', 'Overdue'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resolved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='resolved_complaints')
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    complaint_type = models.CharField(max_length=100)
    description = models.TextField()
    issue_raise_date = models.DateTimeField(auto_now_add=True)
    complain_status = models.CharField(max_length=20, choices=COMPLAINT_STATUS_CHOICES)
    due_date = models.DateTimeField()
    tat = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.complaint_type} - {self.user.name}"



class DeletedUser(models.Model):
    id = models.IntegerField(primary_key=True)  # Primary Key
    name = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    emp_code = models.CharField(max_length=50, null=True, blank=True)
    emp_level = models.CharField(
        max_length=2,
        choices=[('L0', 'Level 0'), ('L1', 'Level 1'), ('L2', 'Level 2')],
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'deleted_users'  # Name of the table in the database
        managed = False  # To prevent migrations for this table

    def __str__(self):
        return self.name if self.name else f"DeletedUser {self.id}"
