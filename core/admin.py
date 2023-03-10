from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(VICTIM_DETAILS)
class VICTIM_DETAILS_Admin(admin.ModelAdmin):
    list_display = ['Name','Age','Gender','Address','Contact','Email','Victim_Type','Cuncilor_Name','Date_Of_Treatement']


@admin.register(COUNCILLOR_DETAILS)
class COUNCILLOR_DETAILS_Admin(admin.ModelAdmin):
    list_display = ['Name','Address','Contact','Email','Age','Gender','Speciality']

@admin.register(EVENT_DETAILS)
class EVENT_DETAILS_Admin(admin.ModelAdmin):
    list_display = ['Name','Address','Date_Of_Events','Number_Of_Monitors','Number_Of_Helpers','Need_Of_Helpers','Event_Type']


@admin.register(SPONSER_DETAILS)
class SPONSER_DETAILS(admin.ModelAdmin):
    list_display = ['Name','sponcer_type','Address','Contact','Email','Sponsering_For','Amount','Payment_Type']

@admin.register(BANNER_DETAILS)
class BANNER_DETAILS_Admin(admin.ModelAdmin):
    list_display =['Name','Number_Of_Banner','Size_Of_Banner','Address','Banner_Type']


@admin.register(HELPER_DETAILS)
class HELPER_DETAILS_Admin(admin.ModelAdmin):
    list_display = ['Name','Address','Contact','Email','Age','Intrested']


@admin.register(EVENT_HELPER_DETAILS)
class EVENT_HELPER_DETAILS_Admin(admin.ModelAdmin):
    list_display = ['Name','Helper_Type','Event_Name','Contact','Work','Monitor_Under']


@admin.register(CAMP_HELPER_DETAILS)
class CAMP_HELPER_DETAILS_Admin(admin.ModelAdmin):
    list_display = ['Name','Type','Camp_Name','Contact','Work','Monitor_Under']

@admin.register(UPLOAD_DETAILS)
class UPLOAD_DETAILS_Admin(admin.ModelAdmin):
    list_display = ['Name','About_Image','Image']

@admin.register(FEEDBACK_DETAILS)
class FEEDBACK_DETAILS_Admin(admin.ModelAdmin):
    list_display = ['Name','Feedback']


    