from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# import model_utils.fields
from model_utils import Choices



# Create your models here.
class Status(models.Model):
    status_id=models.IntegerField(primary_key=True)
    ok=models.CharField(max_length=200)
    def __str__(self):
        return self.ok

    @property
    def memberss(self):
        return self.members_set.all()

# class CustomUser(User):
#     real_name="{} {}".format(User.first_name , User.last_name)
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name


class Members(models.Model):
    TIMEZONES = Choices(
    ('Canada/Atlantic','Canada/Atlantic'),
    ('Canada/Central','Canada/Central'),
    ('Canada/Eastern','Canada/Eastern'),
    ('Canada/Mountain','Canada/Mountain'),
    ('Canada/Pacific','Canada/Pacific'),
    )
    id=models.CharField(primary_key=True,max_length=200)
    real_name = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    # real_name= models.ForeignKey(CustomUser,related_name="user", on_delete=models.CASCADE)
    # real_name= models.OneToOneField(User, on_delete=models.CASCADE)
    # tz=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)
    tz=models.CharField(max_length=100,blank=True,null=True, choices=TIMEZONES,unique=True)

    status_id=models.ForeignKey(Status,related_name="members",on_delete=models.CASCADE)
    @property
    def activityperiods(self):
        return self.activityperiod_set.all()
    @property
    def userdisplay(self):
        return self.user_set.all()

    def __str__(self):
        return self.id

class ActivityPeriod (models.Model):
    activity_id=models.IntegerField(primary_key=True)
    start_time=models.DateTimeField('date started')
    end_time=models.DateTimeField('date ended')

    id=models.ForeignKey(Members,related_name="activityperiod",on_delete=models.CASCADE)
    def __str__(self):
        return self.start_time + ' | ' + self.end_time




# class ActivityPeriod (models.Model):
#     ok=models.CharField(max_length=200)
#     members=[
#         ('id',models.CharField(primary_key=True,max_length=200)),
#         ('real_name',models.OneToOneField(User, on_delete=models.CASCADE)),
#         ('tz',model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
#         ('activity_periods'
