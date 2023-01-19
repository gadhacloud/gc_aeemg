from django.contrib import admin
import site
from .models import Membre, Organe, User

admin.site.register(User)
admin.site.register(Membre)
admin.site.register(Organe)


class adminUser(admin.ModelAdmin):
    list_display=('id','membre','login','organe','motDePasse','type')
    list_filter=('id','membre','login','organe','type',)



class adminMembre(admin.ModelAdmin):
    list_display=('id','nom')
    list_filter=('id','nom',)


class adminOrgane(admin.ModelAdmin):
    list_display=('id','nom')
    list_filter=('id','nom',)