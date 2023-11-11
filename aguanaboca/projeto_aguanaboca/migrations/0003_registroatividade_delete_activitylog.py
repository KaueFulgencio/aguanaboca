# Generated by Django 4.2.4 on 2023-11-11 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projeto_aguanaboca', '0002_alter_produto_imagem_alter_produto_preco_activitylog'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroAtividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.CharField(choices=[('adicao', 'Adição'), ('edicao', 'Edição'), ('remocao', 'Remoção')], max_length=10)),
                ('item_id', models.PositiveIntegerField()),
                ('tipo_item', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ActivityLog',
        ),
    ]
