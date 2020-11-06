from django.contrib import admin
from .models import Profile,City,Skills,Sumary,Education,Experience,Experience_benefits
from .models import Project,Category,Client,Service,Info,TESTIMONIALS



# Register your models here.
admin.site.register(Profile)
admin.site.register(City)
admin.site.register(Skills)
admin.site.register(Sumary)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Experience_benefits )
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Info)
admin.site.register(TESTIMONIALS)