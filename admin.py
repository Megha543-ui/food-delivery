from django.contrib import admin
from food.models import SignupUser
from food.models import Payment
from food.models import Contact

admin.site.register(SignupUser)
admin.site.register(Payment)
admin.site.register(Contact)

# Register your models here.
