from distutils.command.upload import upload
from platform import mac_ver
from tabnanny import check
from django.db import models
from idna import check_label

# Create your models here.
Gender_Choice=[
    ('male','male'),
    ('Female','Female')
]

Victim_type=(
    ('Women Violence','Women Violence'),
    ('Children Violence','Children Violence'),
    ('psychology Violence','psychology Violence'),
    ('Helth Care','Helth Care'),
    ('Other','Other')
)

class VICTIM_DETAILS(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Gender=models.CharField(choices=Gender_Choice,max_length=20)
    Address=models.CharField(max_length=100)
    Contact=models.IntegerField()
    Email=models.EmailField()
    Victim_Type=models.CharField(choices=Victim_type,max_length=20)
    Cuncilor_Name=models.CharField(max_length=50)
    Date_Of_Treatement=models.DateField()


Victim_Type=(
    ('Women Violence','Women Violence'),
    ('Children Violence','Children Violence'),
    ('psychology Violence','psychology Violence'),
    ('Helth Care','Helth Care'),
    ('Other','Other')
)

class COUNCILLOR_DETAILS(models.Model):
    Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=100)
    Contact=models.IntegerField()
    Email=models.EmailField()
    Age=models.IntegerField()
    Gender=models.CharField(choices=Gender_Choice,max_length=20)
    Speciality=models.CharField(choices=Victim_type,max_length=20)


class CAMPS_DETAILS(models.Model):
    Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=100)
    DateOfCamps=models.DateField()
    Days_For_Camp=models.IntegerField()
    Number_Of_Monitors=models.IntegerField()
    Number_Of_Helpers=models.IntegerField()
    Need_Of_Helpers=models.IntegerField()


Event_Type=(
    ('Health Care','Health Care'),
    ('Women Rights','Women Rights'),
    ('Carrer Guidence','Carrer Guidence'),
    ('Other','Other')
)


class EVENT_DETAILS(models.Model):
    Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=100)
    Date_Of_Events=models.DateField()
    Number_Of_Monitors=models.IntegerField()
    Number_Of_Helpers=models.IntegerField()
    Need_Of_Helpers=models.IntegerField()
    Event_Type=models.CharField(choices=Event_Type,max_length=20)

Sponcer_Type=(
    ('Self','Self'),
    ('Organisation','Organisation')
)

Sponsering=(
    ('Camps','Camps'),
    ('Event','Event')
)

PaymentType=(
    ('Debit Card','Debit Card'),
    ('Credit Card','Credit Card'),
    ('Cash','Cash')
)

class SPONSER_DETAILS(models.Model):
    Name=models.CharField(max_length=50)
    sponcer_type=models.CharField(choices=Sponcer_Type,max_length=20)
    Address=models.CharField(max_length=100)
    Contact=models.IntegerField()
    Email=models.EmailField()
    Sponsering_For=models.CharField(max_length=20,choices=Sponsering)
    Amount=models.IntegerField()
    Payment_Type=models.CharField(max_length=20,choices=PaymentType)


BannerTypes=(
    ('Camps','Camps'),
    ('Event','Event')
)

class BANNER_DETAILS(models.Model):
    Name=models.CharField(max_length=50)
    Number_Of_Banner=models.IntegerField()
    Size_Of_Banner=models.IntegerField()
    Address=models.CharField(max_length=100)
    Banner_Type=models.CharField(choices=BannerTypes,max_length=20)
    

Help_intrested=(
    ('Camps','Camps'),
    ('Event','Event')
)


class HELPER_DETAILS(models.Model):
    Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=100)
    Contact=models.IntegerField()
    Email=models.EmailField()
    Age=models.IntegerField()
    Intrested=models.CharField(max_length=20,choices=Help_intrested)


helper_type=(
    ('Helper','Helper'),
    ('Monitor','Monitor'),
    ('Other','Other')
)

work_type=(
    ('Back Stage','Back Stage'),
    ('On Stage','On Stage'),
    ('Decoration','Decoration')
)


class EVENT_HELPER_DETAILS(models.Model):
    Name=models.CharField(max_length=50)
    Helper_Type=models.CharField(choices=helper_type,max_length=20)
    Event_Name=models.CharField(max_length=50)
    Contact=models.IntegerField()
    Work=models.CharField(max_length=20,choices=work_type)
    Monitor_Under=models.CharField(max_length=50)


class CAMP_HELPER_DETAILS(models.Model):
    Name=models.CharField(max_length=50)
    Type=models.CharField(choices=helper_type,max_length=20)
    Camp_Name=models.CharField(max_length=50)
    Contact=models.IntegerField()
    Work=models.CharField(max_length=20,choices=work_type)
    Monitor_Under=models.CharField(max_length=50)


class UPLOAD_DETAILS(models.Model):
    Name=models.CharField(max_length=50)
    About_Image=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='Images')

class FEEDBACK_DETAILS(models.Model):
    Name=models.CharField(max_length=50)
    Feedback=models.CharField(max_length=70)
