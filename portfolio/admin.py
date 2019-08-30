from django.contrib import admin
from .models import Post
from .models import SnsData
from .models import About

# 아래의 코드를 입력하면 SnsData를 admin 페이지에서 관리할 수 있습니다.
admin.site.register(SnsData)
admin.site.register(Post)
admin.site.register(About)

# Register your models here.
