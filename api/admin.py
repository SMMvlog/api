from django.contrib import admin
from .models import Skill,Experience,Education

# Register your models here.

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','skill_name','exp_in_month']
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id','company_name','roll','Total_worked_month']
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id','University_or_BoardName','Stream_Name','Passing_year']