from django.db import models

# 定义标题模型
class TitleSet(models.Model):
    title = models.CharField(max_length=30) # 定义数据库字段：第一标题
    text = models.CharField(max_length=30) # 定义数据库字段：第二标题

    """定义控制台/后台的模型表示"""
    def __str__(self):
        return "1: %s, 2: %s" % (self.title, self.text)
    
