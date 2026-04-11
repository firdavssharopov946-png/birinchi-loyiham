from django.shortcuts import render
from .models import Mahsulot, Mijoz, Buyurtma
from django.db.models import Count
from django.db.models.functions import TruncDay
from datetime import timedelta
from django.utils import timezone
from .models import Buyurtma  

def buyurtmalar(request):
    
    hamma_buyurtmalar = Buyurtma.objects.all() 
    
    
    return render(request, 'buyurtmalar.html', {'buyurtmalar': hamma_buyurtmalar})

def home(request):
    return render(request, 'index.html')


from django.shortcuts import render
from .models import Mahsulot, Mijoz, Buyurtma
from django.db.models import Sum

def dashboard_view(request):
    soni = Mahsulot.objects.count()
    mijozlar = Mijoz.objects.count()
    daromad = Buyurtma.objects.aggregate(Sum('umumiy_narxi'))['umumiy_narxi__sum'] or 0

    context = {
        'soni': soni,
        'mijozlar': mijozlar,
        'daromad': daromad,
    }
    return render(request, 'dashboard.html', context)




def dashboard(request):
    m_soni = Mahsulot.objects.count()
    mi_soni = Mijoz.objects.count()
    b_soni = Buyurtma.objects.count()
    
    mahsulotlar = Mahsulot.objects.all().order_by('-id')[:5]
    
    buyurtmalar = Buyurtma.objects.all().order_by('-id')[:5]

    context = {
        'mahsulotlar_soni': m_soni,
        'mijozlar_soni': mi_soni,
        'buyurtmalar_soni': b_soni,
        'mahsulotlar_royxati': mahsulotlar,
        'oxirgi_buyurtmalar': buyurtmalar,
    }
    
    return render(request, 'dashboard.html', context)


def buyurtmalar(request):
    hamma_buyurtmalar = Buyurtma.objects.all() 
    return render(request, 'buyurtmalar.html', {'buyurtmalar': hamma_buyurtmalar})

def mahsulotlar(request):
    return render(request, 'mahsulotlar.html')

def mijozlar(request):
    data = Mijoz.objects.all()
    return render(request, 'mijozlar.html', {'mijozlar': data})



def mijozlar_sahifasi(request):
    hamma_mijozlar = Mijoz.objects.all()
    return render(request, 'mijozlar.html', {'mijozlar': hamma_mijozlar})


def mahsulotlar_view(request):
    products = Mahsulot.objects.all()
    return render(request, 'mahsulotlar.html', {'mahsulotlar': products})


def mijozlar_view(request):
    hamma_mijozlar = Mijoz.objects.all() 
    
    return render(request, 'mijozlar.html', {'mijozlar': hamma_mijozlar})



from django.shortcuts import render, redirect
from .models import Mahsulot, Mijoz, Buyurtma


def mahsulot_qoshish(request):
    if request.method == "POST":
        nomi = request.POST.get('nomi')
        narxi = request.POST.get('narxi')
        miqdori = request.POST.get('miqdori')
        
        Mahsulot.objects.create(nomi=nomi, narxi=narxi, miqdori=miqdori)
        return redirect('dashboard') 
        
    return render(request, 'mahsulot_qoshish.html')


from django.shortcuts import render, redirect
from .models import Buyurtma

def buyurtmalar_view(request):
    buyurtmalar = Buyurtma.objects.all().order_by('-sana')
    return render(request, 'buyurtmalar.html', {'buyurtmalar': buyurtmalar})

def buyurtma_qoshish(request):
    if request.method == "POST":
        mijoz_ismi = request.POST.get('mijoz')
        telefon_raqam = request.POST.get('tel')
        mahsulot = request.POST.get('mahsulot')
        narx = request.POST.get('narx')
        
        Buyurtma.objects.create(
            mijoz_nomi=mijoz_ismi,
            telefon=telefon_raqam,
            mahsulot_nomi=mahsulot,
            narxi=narx,
            holat="Kutilmoqda" 
        )
        
        return redirect('buyurtmalar') 

    return render(request, 'buyurtma_qoshish.html')

def mijoz_qoshish(request):
    if request.method == "POST":
        ismi_dan_kelgan = request.POST.get('ismi') 
        telefon_dan_kelgan = request.POST.get('telefon')

        Mijoz.objects.create(
            ism=ismi_dan_kelgan, 
            tel=telefon_dan_kelgan 
        )
        return redirect('dashboard')
    return render(request, 'mijoz_qoshish.html')


def buyurtmalar_list(request):
    buyurtmalar = Buyurtma.objects.all().select_related('mijoz', 'mahsulot').order_by('-sana')
    
    return render(request, 'buyurtmalar.html', {'buyurtmalar': buyurtmalar})


