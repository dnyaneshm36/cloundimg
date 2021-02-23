from django.contrib import admin
from .models import Tree
# Register your models here.
# admin.site.register(Tree)

# Register your models here.
from .models import Tree,Bestimages
# Register your models here.

class Treeadmin(admin.ModelAdmin):
    list_display= ['id','name','image','desc','image_data']
    # class Meta:
    #     model = Myfrienddetail
class Bestimagesadmin(admin.ModelAdmin):
    list_display= ['id','name','image','desc']

admin.site.register(Tree, Treeadmin)
admin.site.register(Bestimages, Bestimagesadmin)
