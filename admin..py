from django.contrib import admin
from models import *

class BookInfoAdmin(admin.ModelAdmin):
	list_display = ['id','btitle','bpub_date']
	list_filter = ['btitle']
	search_fields = ['btitle']
	list_per_page = 1
	fieldsets = [
    	('basic',{'fields': ['btitle']}),
    	('more', {'fields': ['bpub_date']})
	]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)



# Register your models here.
