# Generated by Django 3.1.6 on 2021-05-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_product_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='related_customer', to='mainapp.Order', verbose_name='Заказы покупателя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('payes', 'Заказ оплачен'), ('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('is_ready', 'Заказ готов'), ('completed', 'Заказ выполнен')], default='new', max_length=100, verbose_name='Статус заказ'),
        ),
    ]
