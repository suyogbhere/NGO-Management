from tokenize import Name
from aiohttp import request
from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from.forms import BannerForm, CouncillorForm, EventForm, FeedbackForm, HelperForm, HelperInCampForm, HelperInEventForm, SponcerForm, UploadForm, signup,VictimForm
from django.contrib.auth import authenticate,login,logout
from.models import ( HELPER_DETAILS, VICTIM_DETAILS,COUNCILLOR_DETAILS,CAMPS_DETAILS,
EVENT_DETAILS,SPONSER_DETAILS,BANNER_DETAILS,EVENT_HELPER_DETAILS,CAMP_HELPER_DETAILS,
UPLOAD_DETAILS,FEEDBACK_DETAILS)

# Create your views here.
def home(request):
    return render(request,'core/home.html')

# SIGNUP PAGE
def SignupPage(request):
    if request.method == 'POST':
        fm = signup(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Succefully')
            return HttpResponseRedirect('/login/')
    else:
        fm = signup()
    return render(request,'core/signup.html',{'form':fm})
 

# LOGIN PAGE
def loginpage(request):
    return render(request,'core/login.html')

# ADMIN LOGIN PAGE
def adminlogin(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass= fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user.is_superuser:
                login(request,user)
                messages.success(request,'log in succefully!!!')
                return HttpResponseRedirect('/adminhome/')
            else:
                messages.error(request,'Sorry You are not Admin user!!!!')
    else:
        fm=AuthenticationForm()
    return render(request,'core/adminlogin.html',{'form':fm})


# HELPER LOGIN PAGE
def helperlogin(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass= fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'log in succefully!!!')
                return HttpResponseRedirect('/helperhome/')
    else:
        fm=AuthenticationForm()
    return render(request,'core/helperlogin.html',{'form':fm})



# ADMIN HOME PAGE
def adminhomepage(request):
    return render(request,'core/adminhome.html')


# HELPER HOME PAGE
def helperhomepage(request):
    return render(request,'core/helperhome.html')


# LOGOUT PAGE
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# PROJECT ABOUT PAGE 
def aboutpage(request):
    return render(request,'core/about.html')

# Feedback Page
def feedbackPage(request):
    if request.method == 'POST':
        fm=FeedbackForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['Name']
            fd=fm.cleaned_data['Feedback']
            data=FEEDBACK_DETAILS(Name=nm,Feedback=fd)
            data.save()
            messages.success(request,'thanks for your feedback!!!')
    else:
        fm=FeedbackForm()
    return render(request,'core/feedback.html',{'form':fm})


# show feedback
def showfeedback(request):
    fm=FEEDBACK_DETAILS.objects.all()
    return render(request,'core/showfeedback.html',{'form':fm})

# delete feedback
def deletefeedback(request,id):
    if request.method == 'POST':
        pi = FEEDBACK_DETAILS.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/showfeedback/')


# Upload Images
def uploadPage(request):
    if request.method == 'POST':
        fm=UploadForm(request.POST, request.FILES)
        if fm.is_valid():
            nm=fm.cleaned_data['Name']
            ai=fm.cleaned_data['About_Image']
            im=fm.cleaned_data['Image']
            data=UPLOAD_DETAILS(Name=nm,About_Image=ai,Image=im)
            data.save()
            messages.success(request,'Image Upload Successfully!!!')
    else:
        fm=UploadForm()
    return render(request,'core/uploadimg.html',{'form':fm})

# Image shows
def showimage(request):
    fm=UPLOAD_DETAILS.objects.all()
    return render(request,'core/showimage.html',{'form':fm})

# UPDATE IMAGE
def update_image(request,id):
    if request.method == 'POST':
        pi=UPLOAD_DETAILS.objects.get(pk=id)
        fm=UploadForm(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update details Succefully!!!')
    else:
        pi=UPLOAD_DETAILS.objects.get(pk=id)
        fm=UploadForm(instance=pi)
    return render(request,'core/updateimage.html',{'form':fm})

# delete image
def delete_image(request,id):
    if request.method=='POST':
        pi =UPLOAD_DETAILS.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/showimage/')


#victim page
def VictimPage(request):
    if request.method =='POST':
        fm=VictimForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['Name']
            ag=fm.cleaned_data['Age']
            gd=fm.cleaned_data['Gender']
            ad=fm.cleaned_data['Address']
            co=fm.cleaned_data['Contact']
            em=fm.cleaned_data['Email']
            vt=fm.cleaned_data['Victim_Type']
            cn=fm.cleaned_data['Cuncilor_Name']
            dot=fm.cleaned_data['Date_Of_Treatement']
            data=VICTIM_DETAILS(Name=nm,Age=ag,Gender=gd,Address=ad,Contact=co,Email=em,Victim_Type=vt,
                                Cuncilor_Name=cn,Date_Of_Treatement=dot)
            data.save()
            messages.success(request,'Record Save Succefully!!!')
    else:
        fm=VictimForm()
    return render(request,'core/victim.html',{'form':fm})


# show victim data
def ShowVictimData(request):
    fm=VICTIM_DETAILS.objects.all()
    return render(request,'core/showvictimdetails.html',{'form':fm})

#This function will update data
def update_victim_data(request,id):
    if request.method == 'POST':
        pi=VICTIM_DETAILS.objects.get(pk=id)
        fm=VictimForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update details Succefully!!!')
    else:
        pi=VICTIM_DETAILS.objects.get(pk=id)
        fm=VictimForm(instance=pi)
    return render(request,'core/updatevictim.html',{'form':fm})

#This function will delete data
def victim_delete_data(request,id):
    if request.method=='POST':
        pi =VICTIM_DETAILS.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/VictimData/')



#  councillor data
def CouncillorPage(request):
    if request.method =='POST':
        fm=CouncillorForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['Name']
            ad=fm.cleaned_data['Address']
            co=fm.cleaned_data['Contact']
            em=fm.cleaned_data['Email']
            ag=fm.cleaned_data['Age']
            gd=fm.cleaned_data['Gender']
            sp=fm.cleaned_data['Speciality']
            data=COUNCILLOR_DETAILS(Name=nm,Age=ag,Gender=gd,Address=ad,Contact=co,Email=em,Speciality=sp)
            data.save()
            messages.success(request,'Record Save Succefully!!!')
    else:
        fm=CouncillorForm()
    return render(request,'core/councillor.html',{'form':fm})


# show councilor data
def ShowCouncillorData(request):
    fm=COUNCILLOR_DETAILS.objects.all()
    return render(request,'core/showcouncillordetails.html',{'form':fm})

#This function will update data
def update_councillor_data(request,id):
    if request.method == 'POST':
        pi=COUNCILLOR_DETAILS.objects.get(pk=id)
        fm=CouncillorForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update details Succefully!!!')
    else:
        pi=COUNCILLOR_DETAILS.objects.get(pk=id)
        fm=CouncillorForm(instance=pi)
    return render(request,'core/updatecouncillor.html',{'form':fm})

#This function will delete data
def councillor_delete_data(request,id):
    if request.method=='POST':
        pi =COUNCILLOR_DETAILS.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/councillorData/')



# Event page
def EventPage(request):
    if request.method =='POST':
        fm=EventForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['Name']
            ad=fm.cleaned_data['Address']
            doe=fm.cleaned_data['Date_Of_Events']
            et=fm.cleaned_data['Event_Type']
            nom=fm.cleaned_data['Number_Of_Monitors']
            noh=fm.cleaned_data['Number_Of_Helpers']
            nh=fm.cleaned_data['Need_Of_Helpers']
            data=EVENT_DETAILS(Name=nm,Address=ad,Date_Of_Events=doe,Event_Type=et,Number_Of_Monitors=nom,
                                Number_Of_Helpers=noh,Need_Of_Helpers=nh)
            data.save()
            messages.success(request,'Record Save Succefully!!!')
    else:
        fm=EventForm()
    return render(request,'core/event.html',{'form':fm})


# show Event data
def ShowEventData(request):
    fm=EVENT_DETAILS.objects.all()
    return render(request,'core/showeventdetails.html',{'form':fm})

#This function will update data
def update_event_data(request,id):
    if request.method == 'POST':
        pi=EVENT_DETAILS.objects.get(pk=id)
        fm=EventForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update details Succefully!!!')
    else:
        pi=EVENT_DETAILS.objects.get(pk=id)
        fm=EventForm(instance=pi)
    return render(request,'core/updatevent.html',{'form':fm})

#This function will delete data
def event_delete_data(request,id):
    if request.method=='POST':
        pi =EVENT_DETAILS.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/eventData/')



#  Sponcers Page
def SponsersPage(request):
    if request.method =='POST':
        fm=SponcerForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['Name']
            st=fm.cleaned_data['sponcer_type']
            ad=fm.cleaned_data['Address']
            co=fm.cleaned_data['Contact']
            em=fm.cleaned_data['Email']
            sf=fm.cleaned_data['Sponsering_For']
            am=fm.cleaned_data['Amount']
            pt=fm.cleaned_data['Payment_Type']
            data=SPONSER_DETAILS(Name=nm,sponcer_type=st,Address=ad,Contact=co,Email=em,Sponsering_For=sf,
                        Amount=am,Payment_Type=pt)
            data.save()
            messages.success(request,'Record Save Succefully!!!')
    else:
        fm=SponcerForm()
    return render(request,'core/sponsers.html',{'form':fm})


# show sponsors data
def ShowSponsorsData(request):
    fm=SPONSER_DETAILS.objects.all()
    return render(request,'core/showsponserdetails.html',{'form':fm})

#This function will update data
def update_sponsors_data(request,id):
    if request.method == 'POST':
        pi=SPONSER_DETAILS.objects.get(pk=id)
        fm=SponcerForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update details Succefully!!!')
    else:
        pi=SPONSER_DETAILS.objects.get(pk=id)
        fm=SponcerForm(instance=pi)
    return render(request,'core/updatesponsers.html',{'form':fm})

#This function will delete data
def sponsors_delete_data(request,id):
    if request.method=='POST':
        pi =SPONSER_DETAILS.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/sponsersData/')


# Banner page
def BannerPage(request):
    if request.method =='POST':
        fm=BannerForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['Name']
            ad=fm.cleaned_data['Address']
            nob=fm.cleaned_data['Number_Of_Banner']
            sob=fm.cleaned_data['Size_Of_Banner']
            bt=fm.cleaned_data['Banner_Type']
            data=BANNER_DETAILS(Name=nm,Address=ad,Number_Of_Banner=nob,Size_Of_Banner=sob,Banner_Type=bt,
                               )
            data.save()
            messages.success(request,'Record Save Succefully!!!')
    else:
        fm=BannerForm()
    return render(request,'core/banner.html',{'form':fm})


# show Banner data
def ShowBannerData(request):
    fm=BANNER_DETAILS.objects.all()
    return render(request,'core/showbannerdetails.html',{'form':fm})

#This function will update data
def update_banner_data(request,id):
    if request.method == 'POST':
        pi=BANNER_DETAILS.objects.get(pk=id)
        fm=BannerForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update details Succefully!!!')
    else:
        pi=BANNER_DETAILS.objects.get(pk=id)
        fm=BannerForm(instance=pi)
    return render(request,'core/updatebanner.html',{'form':fm})

#This function will delete data
def banner_delete_data(request,id):
    if request.method=='POST':
        pi =BANNER_DETAILS.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/bannerData/')


# Helper page
def HelperPage(request):
    if request.method =='POST':
        fm=HelperForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['Name']
            ad=fm.cleaned_data['Address']
            co=fm.cleaned_data['Contact']
            em=fm.cleaned_data['Email']
            ag=fm.cleaned_data['Age']
            intre=fm.cleaned_data['Intrested']
            data=HELPER_DETAILS(Name=nm,Address=ad,Contact=co,Email=em,Age=ag,Intrested=intre)
            data.save()
            messages.success(request,'Record Save Succefully!!!')
    else:
        fm=HelperForm()
    return render(request,'core/helper.html',{'form':fm})


# show Helper data
def ShowHelperData(request):
    fm=HELPER_DETAILS.objects.all()
    return render(request,'core/showhelperdetails.html',{'form':fm})

#This function will update data
def update_helper_data(request,id):
    if request.method == 'POST':
        pi=HELPER_DETAILS.objects.get(pk=id)
        fm=HelperForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update details Succefully!!!')
    else:
        pi=HELPER_DETAILS.objects.get(pk=id)
        fm=HelperForm(instance=pi)
    return render(request,'core/updatehelper.html',{'form':fm})

#This function will delete data
def helper_delete_data(request,id):
    if request.method=='POST':
        pi =HELPER_DETAILS.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/helperData/')



# Helper IN Events page
def HelperInEventPage(request):
    if request.method =='POST':
        fm=HelperInEventForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['Name']
            ht=fm.cleaned_data['Helper_Type']
            en=fm.cleaned_data['Event_Name']
            co=fm.cleaned_data['Contact']
            wo=fm.cleaned_data['Work']
            mo=fm.cleaned_data['Monitor_Under']
            data=EVENT_HELPER_DETAILS(Name=nm,Helper_Type=ht,Event_Name=en,Contact=co,Work=wo,Monitor_Under=mo)
            data.save()
            messages.success(request,'Record Save Succefully!!!')
    else:
        fm=HelperInEventForm()
    return render(request,'core/helperinevents.html',{'form':fm})


# show Helper data
def ShowHelperInEventData(request):
    fm=EVENT_HELPER_DETAILS.objects.all()
    return render(request,'core/showhelpereventdetails.html',{'form':fm})

#This function will update data
def update_helperevent_data(request,id):
    if request.method == 'POST':
        pi=EVENT_HELPER_DETAILS.objects.get(pk=id)
        fm=HelperInEventForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update details Succefully!!!')
    else:
        pi=EVENT_HELPER_DETAILS.objects.get(pk=id)
        fm=HelperInEventForm(instance=pi)
    return render(request,'core/updatehelperevent.html',{'form':fm})

#This function will delete data
def helperinevent_delete_data(request,id):
    if request.method=='POST':
        pi =EVENT_HELPER_DETAILS.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/helpereventdata/')



# Helper IN Camp page
def HelperInCampPage(request):
    if request.method =='POST':
        fm=HelperInCampForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['Name']
            tp=fm.cleaned_data['Type']
            cn=fm.cleaned_data['Camp_Name']
            co=fm.cleaned_data['Contact']
            wo=fm.cleaned_data['Work']
            mo=fm.cleaned_data['Monitor_Under']
            data=CAMP_HELPER_DETAILS(Name=nm,Type=tp,Camp_Name=cn,Contact=co,Work=wo,Monitor_Under=mo)
            data.save()
            messages.success(request,'Record Save Succefully!!!')
    else:
        fm=HelperInCampForm()
    return render(request,'core/helperincamps.html',{'form':fm})


# show Helper in camp data
def ShowHelperInCampData(request):
    fm=CAMP_HELPER_DETAILS.objects.all()
    return render(request,'core/showhelpercampdetails.html',{'form':fm})

#This function will update data
def update_helpercamp_data(request,id):
    if request.method == 'POST':
        pi=CAMP_HELPER_DETAILS.objects.get(pk=id)
        fm=HelperInCampForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update details Succefully!!!')
    else:
        pi=CAMP_HELPER_DETAILS.objects.get(pk=id)
        fm=HelperInCampForm(instance=pi)
    return render(request,'core/updatehelpercamp.html',{'form':fm})

#This function will delete data
def helperincamp_delete_data(request,id):
    if request.method=='POST':
        pi =CAMP_HELPER_DETAILS.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/helpercampdata/')




