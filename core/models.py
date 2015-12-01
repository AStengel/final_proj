from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
VISIBILITY_CHOICES = (
(0, 'Public'),
(1, 'Anonymous'),
)
RATING_CHOICES = (
(0, 'None'),
(1, '*'),
(2, '**'),
(3, '***'),
(4, '****'),
(5, '*****'),
)
# Create your models here.

class Course(models.Model):
  course = models.CharField(max_length=300)
  professor = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)
  visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)

  def get_absolute_url(self):
    return reverse("course_detail", args=[self.id])

  def __unicode__(self):
    return self.course

class Note(models.Model):
  course = models.ForeignKey(Course)
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add=True)
  text = models.TextField()
  visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)
  rating = models.IntegerField(choices=RATING_CHOICES, default=0)

  def __unicode__(self):
    return self.text

class Vote(models.Model):
  user = models.ForeignKey(User)
  course = models.ForeignKey(Course, blank=True, null=True)
  note = models.ForeignKey(Note, blank=True, null=True)

  def __unicode__(self):
    return "%s upvoted" % (self.user.username)