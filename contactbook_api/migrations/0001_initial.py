from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone_number', models.IntegerField(unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
