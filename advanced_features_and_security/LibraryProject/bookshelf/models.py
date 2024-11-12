from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.conf import settings

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='courses')


    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'

class Library(models.Model):
    name = models.CharField(max_length = 50)
    books = models.ManyToManyField(Book, related_name='courses')

    def __str__(self) -> str:
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length = 50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name



class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_photots', null=True, blank=True)    


    def __str__(self) -> str:
        return self.email                                                                                                                                             


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError("Enter correct email address")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._id)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    objects = CustomUserManager() 



class Book(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
