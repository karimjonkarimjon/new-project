from django.shortcuts import render, get_object_or_404
from .models import Portfolia, Services
from Product.models import Add_Team
from Category.models import Category_Portfolia
from contact.forms import ContactForm
from aboute.models import Abaute_us
from pricing.models import Pricing
# Create your views here.
def Ad_Services(malumot, category_slug=None):
    add_servis = Services.objects.all()
    add_team = Add_Team.objects.all()
    add_aboute = Abaute_us.objects.all()
    add_pricing = Pricing.objects.all()
    a = ContactForm
    if malumot.method == "POST":
        a = ContactForm(malumot.POST)
        if a.is_valid():
            toplam = a.save(commit=False)
            a = ContactForm()
            toplam.save()
        
        
    if category_slug == None:
        products = Portfolia.objects.filter(mavjudmi=True)
    else:
        categoryes = get_object_or_404(Category_Portfolia, slug=category_slug)
        products = Portfolia.objects.filter(mavjudmi=True, categpory=categoryes)

    context = {
        "servic": add_servis,
        "team": add_team,
        "contact_for": a,
        "home_category": products,
        "about": add_aboute,
        "addpricing": add_pricing,
    }
    return render(malumot, "home.html", context)

def getID(request, id):
    post = Services.objects.get(id=id)
    
    context = {
        "servic":post
    }
    
    return render(request, "postapp/detail.html", context)

def Detail(malumot,id):
    stre = Portfolia.objects.get(id=id)
 
    context = {
        "home_category":stre,
    } 
    return render(malumot,"postapp/detail_product.html",context)