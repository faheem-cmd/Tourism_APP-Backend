from django.db import models


class places(models.Model):
    place = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to="places/")
    image2 = models.ImageField(upload_to="places/")
    content = models.TextField()

    def __str__(self):
        return self.place


class user(models.Model):
    name = models.CharField(max_length=15)
    place = models.CharField(max_length=30)
    experience = models.TextField()
    rating = models.CharField(max_length=10)
    image = models.ImageField(upload_to="users/", blank=True, null=True)
    profile = models.ImageField(upload_to="users/", blank=True, null=True)


    def __str__(self):
        return self.place


class feedback(models.Model):
    name = models.CharField(max_length=200)
    feedback = models.TextField()

    def __str__(self):
        return self.feedback


class slider(models.Model):
    subject = models.CharField(max_length=200)
    image = models.URLField(max_length=500)
    image2 = models.URLField(max_length=500)
    image3 = models.URLField(max_length=500)
    image4 = models.URLField(max_length=500)
    image5 = models.URLField(max_length=500)

    def __str__(self):
        return self.subject



class Employee(models.Model):
    emplyee_regNo = models.TextField(unique=True)
    emplyee_name = models.TextField()
    employee_email = models.TextField()
    employee_mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emplyee_name


class gallery(models.Model):
    uri = models.URLField(max_length=500)

    def __str__(self):
        return self.uri


class reels(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    image = models.ImageField(upload_to="reels/")

    def __str__(self):
        return self.name


class popular(models.Model):
    name = models.CharField(max_length=30)
    history = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class history(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class review(models.Model):
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.comment
