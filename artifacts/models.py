import uuid

from django.db import models
from django.db import connection, transaction
from django.db.utils import OperationalError


class Tag(models.Model):
    name = models.CharField(max_length=200)


class MLDataset(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class MLDatasetVersion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=200)
    version = models.CharField(max_length=200)
    ml_dataset = models.ForeignKey(MLDataset, on_delete=models.CASCADE)


class MLModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)


class MLModelVersion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=200)
    version = models.CharField(max_length=200)
    ml_model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
    ml_dataset_version = models.ForeignKey(MLDatasetVersion, on_delete=models.CASCADE)


def update_index(sender, instance, created, **kwargs):
    try:
        with transaction.atomic():
            cursor = connection.cursor()
            fts_txt = instance.name + ' ' + instance.description
            # txt should be stripped from HTML, stop words etc. to get smaller size of the database
            if created:
                # add if object is created, not updated
                cursor.execute("INSERT INTO FTSearch (slug, body) VALUES (%s, %s)", (instance.id, fts_txt))
    except Exception:
        cursor.execute("CREATE VIRTUAL TABLE FTSearch using FTS3(slug, body)")

models.signals.post_save.connect(update_index, sender=MLModel)
