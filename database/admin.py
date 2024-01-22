from django.contrib import admin
from .models import Users, Coords, Perevals, Images, Level


@admin.register(Perevals)
class PerevalsAdmin(admin.ModelAdmin):
    list_display = ('short_beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'status', 'level', 'user', 'coord')

    def short_beauty_title(self, obj):
        return obj.beauty_title[:50] + '...' if len(obj.beauty_title) > 50 else obj.beauty_title
    short_beauty_title.short_description = 'Название перевала'

    def user_info(self, obj):
        return f"{obj.user.name} - {obj.user.fam} - {obj.user.otc}"
    user_info.short_description = 'Информация о пользователе'


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('fam', 'name', 'otc', 'email', 'phone')


@admin.register(Coords)
class CoordsAdmin(admin.ModelAdmin):
    list_display = ('perevals', 'latitude', 'longitude', 'height')


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('pereval', 'title', 'date_added', 'image')


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('summer', 'autumn', 'winter', 'spring')
