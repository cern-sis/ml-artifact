from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(MLModel)
admin.site.register(MLDataset)
admin.site.register(MLDatasetVersion)
admin.site.register(MLModelVersion)
admin.site.register(Tag)
