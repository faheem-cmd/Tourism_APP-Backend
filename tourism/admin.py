from django.contrib import admin

from .models import places
from .models import user
from .models import feedback
from .models import slider
from .models import Employee
from .models import gallery
from .models import reels
from .models import popular
from .models import history
from .models import review





admin.site.register(places)
admin.site.register(user)
admin.site.register(feedback)
admin.site.register(slider)
admin.site.register(Employee)
admin.site.register(gallery)
admin.site.register(reels)
admin.site.register(popular)
admin.site.register(history)
admin.site.register(review)


