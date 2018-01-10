from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['name', 'father_name', 'last_name']}),
        ('Particular data',     {'fields': ['birthday', 'sex']}),
        ('Years of government', {'fields': ['start_of_government', 'end_of_government']}),
        ('Addition data',       {'fields': ['creation_date', 'father_id', 'mother_id']})
    ]

admin.site.register(Person, PersonAdmin)
