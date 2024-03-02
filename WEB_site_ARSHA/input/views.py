from django.shortcuts import render
from .forms import InpForm
# Create your views here.
def add_inp(malumot):
    ab = InpForm
    if malumot.method == "POST":
        ab = InpForm(malumot.POST)
        if ab.is_valid():
            toplam = ab.save(commit=False)
            toplam.save()
            
    context = {
        'add_inp': ab,
    }
    
    return render(malumot, "footer.html", context)