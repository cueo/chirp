from django.db import models

# Create your models here.

class UserProfile(models.Model):
	uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=42)
	handle = models.CharField(max_length=42, unique=True)
	email_id = models.EmailField(max_length=255, unique=True)
	dob = models.DateField()
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other')
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

	img = models.ImageField(upload_to='/profile_pic/', height_field=None, width_field=None, max_length=100)
	joined_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '@' + self.handle + ' ' + self.name

class UserLoginCredentials(models.Model):
	uid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	pwd = models.CharField(max_length=255)
	ts = models.DateTimeField(auto_now=True)

class Tweet(models.Model):
	tid = models.IntegerField(primary_key=True)
	uid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	tweet = models.CharField(max_length=140)
	ts = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
	follower_uid = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower')
	followed_uid = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followed')
