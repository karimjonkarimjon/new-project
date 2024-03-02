from .models import Category_Portfolia

def menu_links(request):
    maxsulot_turi = Category_Portfolia.objects.all()
    
    context = {
        "maxsulot_all": maxsulot_turi
    }
    return context