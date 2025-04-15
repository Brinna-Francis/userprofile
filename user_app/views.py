from django.shortcuts import render,redirect

from .forms import ProfileForm,ProjectForm
from .models import Profile, Project


def createProfile(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        address = request.POST.get('address')
        location = request.POST.get('location')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        age = request.POST.get('age')
        qualifications = request.POST.get('qualifications')
        skills = request.POST.get('skills')
        certifications = request.POST.get('certifications', 'None')
        work_experience = request.POST.get('work_experience')

        profile = Profile(
            username=username,
            address=address,
            location=location,
            email=email,
            phone_number=phone_number,
            age=age,
            qualifications=qualifications,
            skills=skills,
            certifications=certifications,
            work_experience=work_experience
        )

        profile.save()

    return render(request, 'profile.html', {'profiles': profiles})

def listProfile(request):
    profiles=Profile.objects.all()

    return render(request, 'listprofile.html',{'profiles':profiles})

def detailsView(request,profile_id):
    profile=Profile.objects.get(id=profile_id)
    return render(request, 'detailsview.html', {'profile': profile})





def updateProfile(request,profile_id):

    profile = Profile.objects.get(id=profile_id)

    if request.method=="POST":
        form = ProfileForm(request.POST,instance=profile)

        if form.is_valid():
            form.save()
        username = request.POST.get('username')
        address = request.POST.get('address')
        location = request.POST.get('location')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        age = request.POST.get('age')
        qualifications = request.POST.get('qualifications')
        skills = request.POST.get('skills')
        certifications = request.POST.get('certifications', 'None')
        work_experience = request.POST.get('work_experience')

        profile.username=username
        profile.address=address
        profile.location=location
        profile.email=email
        profile.phone_number=phone_number
        profile.age=age
        profile.qualifications=qualifications
        profile.skills=skills
        profile.certifications=certifications
        profile.work_experience=work_experience

        profile.save()

        return redirect("/")
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'updateview.html', {'form': form,'profile':profile})

def deleteView(request,profile_id):

    profile=Profile.objects.get(id=profile_id)

    if request.method=="POST":

        profile.delete()

        return redirect("listview/")

    return render(request, 'deleteview.html',{'profile': profile})



def createProfile(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':

        form=ProfileForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form=ProfileForm()
    return render(request,'profile.html',{'form':form,'profiles':profiles})


def createProject(request):

    proj_details = Project.objects.all()

    if request.method == 'POST':
        form=ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            print("JJJJJJJJJJJJJJJJJJ")
            form.save()

            return redirect("/")

    else:
        form=ProjectForm()
    return render(request,'project.html',{'form':form,'data':proj_details})




