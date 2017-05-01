from django.contrib import admin

from .models import Posts

class PostModelAdmin(admin.ModelAdmin):
	list_display = ("title", "updated", "timestamp")
	search_fields = ("title", "content")
	ordering = ("title", "updated", "timestamp")
	list_filter = ("updated", "timestamp")

	class Meta:
		model = Posts

admin.site.register(Posts, PostModelAdmin)