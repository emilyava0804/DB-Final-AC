from django.db import models

# Create your models here.
class employee(models.Model):
	employeeTypes = (
		('Manager', 'Manager'),
		('Staff', 'Staff'),
		('Medic', 'Medical'),
		('CEO', 'CEO'),
		('Maintanence', 'Maintanence'),
		('Custodian', 'Custodian'),
	)
	employeeID = models.AutoField(primary_key=True)
	employeeType = models.CharField(max_length=11, choices=employeeTypes)
	employeeDOB = models.DateField()
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	salary = models.IntegerField()

	def __str__(self):
		return self.fname


class employeePhone(models.Model):
	ePhoneID = models.AutoField(primary_key=True)
	employeeID = models.ForeignKey(employee, on_delete=models.CASCADE)
	ePhoneNumber = models.IntegerField()


class park(models.Model):
	parkID = models.AutoField(primary_key=True)
	parkName = models.CharField(max_length=30)

	def __str__(self):
		return self.parkName

class volunteer(models.Model):
	volunteerID = models.AutoField(primary_key=True)
	vFname = models.CharField(max_length=30)
	vLname = models.CharField(max_length=30)
	volunteerDOB = models.DateField()
	hours = models.IntegerField()
	parkID = models.ForeignKey(park, on_delete=models.CASCADE)

	def __str__(self):
		return self.vFname

class volunteerPhone(models.Model):
	vPhoneID = models.AutoField(primary_key=True)
	volunteerID = models.ForeignKey(volunteer, on_delete=models.CASCADE)
	vPhoneNumber = models.IntegerField()


class animalFood(models.Model):
	foodTypes = (
		('bamboo', 'bamboo'),
		('eucalyptus', 'eucalyptus'),
		('grass', 'grass'),
		('nuts', 'nuts'),
		('meat', 'meat'),
		('fish', 'fish'),
		('lettuce', 'lettuce'),
		('banana', 'banana'),
		('worms', 'worms'),
		('mice', 'mice'),
	)
	foodID = models.AutoField(primary_key=True)
	food = models.CharField(max_length=10, choices=foodTypes)

	def __str__(self):
		return self.food

class exhibit(models.Model):
	exhibitID = models.AutoField(primary_key=True)
	exhibitName = models.CharField(max_length=30)
	parkID = models.ForeignKey(park, on_delete=models.CASCADE)
	animalType =models.CharField(max_length=30)
	foodID = models.ForeignKey(animalFood, on_delete=models.CASCADE)

	def __str__(self):
		return self.exhibitName

class animal(models.Model):
	genders = (
		('F', 'Female'),
		('M', 'Male'),
	)
	animalID = models.AutoField(primary_key=True)
	animalName = models.CharField(max_length=30)
	animalAge = models.IntegerField()
	animalGender = models.CharField(max_length=1, choices = genders)
	exhibitID = models.ForeignKey(exhibit, on_delete=models.CASCADE)

	def __str__(self):
		return self.animalName

class specialNeed(models.Model):
	needID = models.AutoField(primary_key=True)
	need = models.CharField(max_length=30)
	care = models.CharField(max_length=30)
	restrictions = models.CharField(max_length=30)

	def __str__(self):
		return self.need

class specialAnimal(models.Model):
	specialID = models.AutoField(primary_key=True)
	animalID = models.ForeignKey(animal, on_delete=models.CASCADE)
	needID = models.ForeignKey(specialNeed, on_delete=models.CASCADE)
