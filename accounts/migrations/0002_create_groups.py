# accounts/migrations/000X_create_groups_and_permissions.py

from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_groups_and_permissions(apps, schema_editor):
    # Създаване на групите (ако не съществуват)
    editors_group, created = Group.objects.get_or_create(name='Editors')
    customers_group, created = Group.objects.get_or_create(name='Customers')

    # Взимаме моделите чрез apps, за да избегнем проблеми с цикличен импорт
    Article = apps.get_model('articles', 'Article')
    Product = apps.get_model('store', 'Product')

    # Получаваме всички permissions за Article и Product
    article_ct = ContentType.objects.get_for_model(Article)
    product_ct = ContentType.objects.get_for_model(Product)

    article_perms = Permission.objects.filter(content_type=article_ct)
    product_perms = Permission.objects.filter(content_type=product_ct)

    # Editors получават всички права за статии и продукти
    editors_group.permissions.set(article_perms | product_perms)

    # Customers получават само права за разглеждане (view) – ако съществуват
    # Ако искате Customers да нямат никакви права, просто коментирайте реда по-долу
    view_perms = Permission.objects.filter(
        content_type__in=[article_ct, product_ct],
        codename__startswith='view_'
    )
    customers_group.permissions.set(view_perms)

    # Ако предпочитате Customers да нямат права, вместо горния ред използвайте:
    # customers_group.permissions.clear()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),   # или последната миграция на accounts
        ('articles', '0001_initial'),  # за да сме сигурни, че Article съществува
        ('store', '0001_initial'),     # за да сме сигурни, че Product съществува
    ]

    operations = [
        migrations.RunPython(create_groups_and_permissions),
    ]