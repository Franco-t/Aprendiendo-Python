# filepath: /D:/Archivo de Programa/proyecto personal/python/djangoproject/registrar/management/commands/delete_ventas.py
from django.core.management.base import BaseCommand
from registrar.models import Venta

class Command(BaseCommand):
    help = 'Delete all rows in the Venta table'

    def handle(self, *args, **kwargs):
        Venta.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all rows in the Venta table'))