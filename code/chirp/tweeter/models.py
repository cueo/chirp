from django.db import models
# Create your models here.

class User(models.Model):
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

	img = models.ImageField(upload_to='/profile_pic/', height_field=None, width_field=None, max_length=100, blank=True)
	joined_on = models.DateTimeField(auto_now_add=True)

	following = models.ManyToManyField('self', symmetrical=False, blank=True)

	def __str__(self):
		return '@' + self.handle + ' ' + self.name

class UserLoginCredentials(models.Model):
	uid = models.ForeignKey(User, on_delete=models.CASCADE)
	pwd = models.CharField(max_length=255)
	ts = models.DateTimeField(auto_now=True)

class Tweet(models.Model):
	tid = models.AutoField(primary_key=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	tweet = models.CharField(max_length=140)
	ts = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '@' + self.author.handle + '<br/>' + self.tweet + '<br/> on ' + self.ts.strftime('%A, %d %B %Y at %H:%M')
