from django.shortcuts import render,redirect,get_object_or_404
from .models import Doctor
from .forms import DoctorForm
# Create your views here.

def doctor_list(request):
    doctors = Doctor.objects.all()

    form = None
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctor/doctor_list/')
    if form is None:
        form = DoctorForm()

    return render(request,'doctor_list.html',{'doctors' : doctors, 'form' : form})

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

# UPDATE
def update_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DoctorForm(instance=doctor)

    # update.html template does not exist in this project currently.
    # Keeping this view for backward compatibility; AJAX will be implemented separately.
    return redirect('/doctor/doctor_list/')

# DELETE
def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    return redirect('/')