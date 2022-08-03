from tkinter.font import families
from django.contrib import admin
from django.urls import path
from desafiomvt.views import list_fam
from desafiomvt.views import create_fam
urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_fam/', create_fam),
    path('familia/', list_fam)
]
