from django.shortcuts import render,get_object_or_404, redirect
from CustomUser.models import UserProfile
from .forms import PersonelForm
def dashboard(request):
    context = {} #TODO: ask project manager for date needs to be use in panel
    return render(request, 'index.html', context)

#* PERSONEL BLOCK
def personel_list(request):
    context = {
        'personels' : UserProfile.objects.filter(is_active=True,is_staff=True).order_by('date_joined'),
    }
    return render(request, 'listkarmand.html', context)
def personel_add(request):
    personel_form = PersonelForm(request.POST or None)

    if personel_form.is_valid():
        personel_form.save()
        return redirect() #TODO: redirect to personal list


