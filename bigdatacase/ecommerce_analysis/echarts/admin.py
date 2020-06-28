from django.contrib import admin
from .models  import viewafter
from .models  import cartafter
from .models  import transafter


# Register your models here.

admin.site.register(viewafter)
admin.site.register(cartafter)
admin.site.register(transafter)