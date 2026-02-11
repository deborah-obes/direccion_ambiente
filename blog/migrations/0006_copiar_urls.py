from django.db import migrations

def copiar_urls(apps, schema_editor):
    Galeria = apps.get_model('blog', 'Galeria')
    for item in Galeria.objects.all():
        if item.url and not item.album_url:
            item.album_url = item.url
            item.save()
            print(f"Copiado: {item.titulo}")

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0005_galeria_album_url'),
    ]
    operations = [
        migrations.RunPython(copiar_urls),
    ]