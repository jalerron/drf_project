from django.contrib import admin

from users.models import Payments


# Register your models here.
@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    pass
