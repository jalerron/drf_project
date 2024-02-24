from django.contrib import admin

from users.models import Payments, User


# Register your models here.
@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
