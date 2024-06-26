# Generated by Django 5.0.6 on 2024-06-02 15:07

import django.db.models.deletion
import pos_app.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pos_app", "0003_remove_customer_no_ktp_remove_profile_bio_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="select_car",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="status",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="user_create",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="user_update",
        ),
        migrations.RenameField(
            model_name="car",
            old_name="name",
            new_name="name_car",
        ),
        migrations.RenameField(
            model_name="car",
            old_name="price",
            new_name="price_day",
        ),
        migrations.RenameField(
            model_name="profile",
            old_name="avatar",
            new_name="image_ktp",
        ),
        migrations.AddField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(default="None", max_length=15),
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code_book",
                    models.CharField(
                        default=pos_app.models.generate_code_book,
                        editable=False,
                        max_length=20,
                    ),
                ),
                ("date_rental", models.DateTimeField()),
                ("date_return", models.DateTimeField()),
                ("location_pickup", models.CharField(max_length=100)),
                ("quantity", models.IntegerField()),
                (
                    "rent_type",
                    models.CharField(
                        choices=[
                            ("With Driver", "With Driver"),
                            ("Without Driver", "Without Driver"),
                        ],
                        default="With Driver",
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_update", models.DateTimeField(auto_now=True)),
                (
                    "name_booking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_booking",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "select_car",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="car_booking",
                        to="pos_app.car",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="customer_status",
                        to="pos_app.statusmodel",
                    ),
                ),
                (
                    "user_create",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_create_customer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_update",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_update_customer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="payment",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="customer_payment",
                to="pos_app.booking",
            ),
        ),
        migrations.DeleteModel(
            name="InfoRent",
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
    ]
