from django.apps import AppConfig


class DynamicDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dynamic_data'
    verbose_name = "动态数据"
