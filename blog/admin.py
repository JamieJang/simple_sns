from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Post, Tag, Profile, Group

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self,request,obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin,self).get_inline_instances(request,obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Tag)

class TagInline(admin.TabularInline):
	model = Post.tags.through
	extra = 0

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
	list_display = ('author','content','location','q_location','published')
	list_display_links = ('author','content')
	readonly_fields = ('author','published',)

	fieldsets = [
		(None,	{'fields':['author']}),
		('Post',	{'fields':['content','location','q_location','published']}),
	]

	inlines = [ TagInline, ]


	
