from django.contrib import admin

# Register your models here.
# models에서 SnsData를 import 해옵니다.
from .models import SnsData

# 아래의 코드를 입력하면 SnsData를 admin 페이지에서 관리할 수 있습니다.
admin.site.register(SnsData)