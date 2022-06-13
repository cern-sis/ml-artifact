from django.db import IntegrityError, models
from django.db import connection, transaction
from django.db.utils import OperationalError


class Artifacts(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.description


def update_index(sender, instance, created, **kwargs):
    try:
        with transaction.atomic():
            cursor = connection.cursor()
            fts_txt = instance.name + ' ' + instance.title + ' ' + instance.description
            # txt should be stripped from HTML, stop words etc. to get smaller size of the database
            if created:
                # add if object is created, not updated
                cursor.execute("INSERT INTO FTSearch (slug, body) VALUES (%s, %s)", (instance.id, fts_txt))
    except OperationalError:
        cursor.execute("CREATE VIRTUAL TABLE FTSearch using FTS3(slug, body)")

models.signals.post_save.connect(update_index, sender=Artifacts)
