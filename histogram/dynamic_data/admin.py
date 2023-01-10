from django.contrib import admin

from .models import TitleSet

# 标题组管理界面设置
class TitleSetAdmin(admin.ModelAdmin):
    search_fields = ['title']


# 在管理页面注册模型
admin.site.register(TitleSet, TitleSetAdmin)
