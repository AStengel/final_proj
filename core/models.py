from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Course(models.Model):
  course = models.CharField(max_length=300)
  professor = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def get_absolute_url(self):
    return reverse("course_detail", args=[self.id])

  def __unicode__(self):
    return self.title

class Note(models.Model):
  course = models.ForeignKey(Course)
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add=True)
  text = models.TextField()

  def __unicode__(self):
    return self.text