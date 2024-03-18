from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Session)
admin.site.register(Allow)
admin.site.register(AllowExit)
admin.site.register(FilledFeedback)
admin.site.register(Feedback)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Question)
admin.site.register(UpdateSeen)

