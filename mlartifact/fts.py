from os import environ
import sys

environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.contrib.sessions.models import *
from django.db import IntegrityError, connection, transaction

from artifacts.models import *

try:
	with transaction.atomic():
		cursor = connection.cursor()
		content = MLModel.objects.all()
		for text in content:
			fts_txt = text.name + ' ' + text.description
			cursor.execute("INSERT INTO FTSearch (slug, body) VALUES (%s, %s)", (text.id, fts_txt))
except IntegrityError as e:
	raise e
