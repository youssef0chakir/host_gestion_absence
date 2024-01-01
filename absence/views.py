from django.shortcuts import render, redirect 
from absence.models  import Etudiant as etudiant, Absence as abs, Cours
from django.db.models import Q
from django.db.models import Sum


#etudiant 
 
def indexEtu(request):
    query = request.GET.get('search')
    if query:
        # Si une recherche est effectuée, filtrez les étudiants en fonction de l'ID ou du nom
            mem = Etudiant.objects.filter(Q(id_etudiant=query) | Q(nom=query))    
    else:
        # Si aucune recherche, affichez tous les étudiants
        mem = Etudiant.objects.all()

    return render(request, 'indexEtu.html', {'mem': mem})


def addEtu(request):
    return render(request,'addEtu.html')

def addEtuRec(request):
    x=request.POST['id']
    y=request.POST['first']
    z=request.POST['last']

    if etudiant.objects.filter(id_etudiant=x).exists():
        error_message = "Student ID exist"
        return render(request, 'addEtu.html', {'error_message': error_message})

    mem=etudiant(id_etudiant=x,nom=y,prenom=z)
    mem.save()
    return redirect("/")


def deleteEtu(request,id_etudiant):
    mem=etudiant.objects.get(id_etudiant=id_etudiant)
    mem.delete()
    return redirect("/")

def updateEtu(request,id_etudiant):
    mem=etudiant.objects.get(id_etudiant=id_etudiant)
    return render(request,'updateEtu.html',{'mem':mem})

def updateEtuRec(request,id_etudiant):
    x=request.POST['id']
    y=request.POST['first']
    z=request.POST['last']
    mem=etudiant.objects.get(id_etudiant=id_etudiant)
    #mem.id_etudiant=x
    mem.nom=y
    mem.prenom=z
    mem.save()
    return redirect("/")


 #Absence

 

def indexAbs(request):
    query = request.GET.get('search')
    
    total_absence = None
    total_absence = abs.objects.filter(id_etudiant=query).aggregate(Sum('nombre_heures_absence'))['nombre_heures_absence__sum']


    if query:
             mem = abs.objects.filter(Q(id_etudiant=query) )    
    else:
         mem = abs.objects.all()
        
    


    return render(request, 'indexAbs.html', {'mem': mem,'total_absence':total_absence})

 
def addAbs(request):
    return render(request,'addAbs.html')


from django.shortcuts import render, redirect 
from absence.models import Etudiant, Absence, Cours

def addAbsRec(request):
    x = request.POST.get('id_etudiant')
    y = request.POST.get('id_cours')
    z = request.POST.get('date')
    w = request.POST.get('heure')

    # Convert x and y to integers
    try:
        x = int(x)
        y = int(y)
    except (TypeError, ValueError):
        error_message = "Invalid Student ID or Course ID"
        return render(request, 'addAbs.html', {'error_message': error_message})

    # Check if the id_etudiant and id_cours exist in respective tables
    if not etudiant.objects.filter(id_etudiant=x).exists():
        error_message = "Student ID does not exist"
        return render(request, 'addAbs.html', {'error_message': error_message})

    if not Cours.objects.filter(id_cours=y).exists():
        error_message = "Course ID does not exist"
        return render(request, 'addAbs.html', {'error_message': error_message})

    # Create Absence instance with integer IDs
    absence_instance = abs(
        id_etudiant=x,
        id_cours=y,
        nombre_heures_absence=w,
        date_absence=z
    )
    absence_instance.save()
    return redirect("/indexAbs")


def deleteAbs(request,id):
    mem=abs.objects.get(id=id)
    mem.delete()
    return redirect("/indexAbs")

def updateAbs(request,id):
    mem=abs.objects.get(id=id)
    return render(request,'updateAbs.html',{'mem':mem})

def updateAbsRec(request,id):
    x=request.POST['heure']
    y=request.POST['date']
    z=request.POST['id_cours']
    w=request.POST['id_etudiant']
    mem=abs.objects.get(id=id)
     

    mem.nombre_heures_absence=x
    mem.date_absence=y
    mem.id_cours=z
    mem.etudiant=w
    mem.save()
    return redirect("/indexAbs")