
from django.contrib import admin

# from .models import Question

# admin.site.register(Question)
# from django.contrib import admin

from .models import Choice, Question
from .models import Jitai
# from .models import JitaiXX
from .models import Yazhu
from .models import Information


from import_export import resources
from import_export.admin import ImportExportModelAdmin
class PostResource(resources.ModelResource):
    class Meta:
        model = Jitai
# class JitaiResource(resources.ModelResource):
#     class Meta:
#         model = Jitai
class PostAdmin(ImportExportModelAdmin):
     resource_class = PostResource
     # ,JitaiResource






class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text','question_description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


class JitaiAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['jitai_id']}),
    ]
    # resource_class = JitaiResource
    resource_class = PostResource

admin.site.register(Jitai, JitaiAdmin)


# admin.site.register(JitaiXX)
# admin.ModelAdmin
class YazhuAdmin(ImportExportModelAdmin):

    
    fieldsets = [
        (None,               {'fields': ['work_date','work_prod','work_mach','work_by','work_support','work_leader','work_qtyall','work_qtyok','work_rej','work_rejper']}),
        ('不良', {'fields': ['rej01','rej02','rej03','rej04','rej05','rej06','rej07','rej08','rej09','rej10','rej11'], 'classes': ['collapse']}),
    ]
    # resource_class = PostResource


admin.site.register(Yazhu, YazhuAdmin)

class InformationAdmin(admin.ModelAdmin):
    list_display = ('group','empe_id','empe_name','empe_dept','tel')
    fieldsets = [
        (None,               {'fields': ['group','empe_id','empe_name','empe_dept','tel']}),
    ]
    # resource_class = JitaiResource
    # resource_class = PostResource

admin.site.register(Information, InformationAdmin)