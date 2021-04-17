from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Director(models.Model):
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others'),
    )
    first_name = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=230, blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=30, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.number}, {self.website}"


class Studio(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    prefix = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title


class NewMovie(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    prefix = models.CharField(max_length=500, blank=True, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    director = models.ManyToManyField(Director, blank=True)
    studio = models.ForeignKey('Studio', on_delete=models.SET_NULL, null=True)
    release_date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    review = models.TextField()
    genre = models.ManyToManyField('Genre', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.director.name} released on {self.release_date}"
