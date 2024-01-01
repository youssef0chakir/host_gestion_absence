from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexEtu,name="indexEtu"),
    path('indexEtu/',views.indexEtu,name="indexEtu"),

    path('addEtu/',views.addEtu,name="addEtu"),
    path("addEtuRec/",views.addEtuRec,name="addEtuRec"),

    path('deleteEtu/<int:id_etudiant>/',views.deleteEtu,name="deleteEtu"),
    path('indexEtu/deleteEtu/<int:id_etudiant>/',views.deleteEtu,name="deleteEtu"),

    path('indexEtu/updateEtu/<int:id_etudiant>/',views.updateEtu,name="updateEtu"),

    path('updateEtu/<int:id_etudiant>/',views.updateEtu,name="updateEtu"),
    path('updateEtu/updateEtuRec/<int:id_etudiant>/',views.updateEtuRec,name="updateEtuRec"),

     




    path('indexAbs/',views.indexAbs,name="indexAbs"),
    path('addAbs/',views.addAbs,name="addAbs"),
    path("addAbsRec/",views.addAbsRec,name="addAbsRec"),

    path('deleteAbs/<int:id>/',views.deleteAbs,name="deleteAbs"),
    path('indexAbs/deleteAbs/<int:id>/',views.deleteAbs,name="deleteAbs"),
    
    
     path('indexAbs/updateAbs/<int:id>/',views.updateAbs,name="updateAbs"),
    path('updateAbs/updateAbsRec/<int:id>/',views.updateAbsRec,name="updateAbsRec")
]