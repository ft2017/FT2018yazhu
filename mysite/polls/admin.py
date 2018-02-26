
from django.contrib import admin

# from .models import Question

# admin.site.register(Question)
# from django.contrib import admin

from .models import Choice, Question
from .models import Yazhu





from import_export import resources
from import_export.admin import ImportExportModelAdmin
class PostResource(resources.ModelResource):
    class Meta:
        model = Yazhu
class PostAdmin(ImportExportModelAdmin):
     resource_class = PostResource





class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
# admin.ModelAdmin
class YazhuAdmin(ImportExportModelAdmin):

    
    fieldsets = [
        (None,               {'fields': ['work_date','work_prod','work_mach','work_by','work_support','work_leader','work_qtyall','work_qtyok','work_rej','work_rejper']}),
        ('不良', {'fields': ['rej01','rej02','rej03','rej04','rej05','rej06','rej07','rej08','rej09','rej10','rej11'], 'classes': ['collapse']}),
    ]
    resource_class = PostResource


admin.site.register(Yazhu, YazhuAdmin)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text','question_description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
