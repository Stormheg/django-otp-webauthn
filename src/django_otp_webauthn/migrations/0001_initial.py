# Generated by Django 5.0.4 on 2024-04-30 15:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="WebAuthnCredential",
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
                    "name",
                    models.CharField(
                        help_text="The human-readable name of this device.",
                        max_length=64,
                    ),
                ),
                (
                    "confirmed",
                    models.BooleanField(
                        default=True, help_text="Is this device ready for use?"
                    ),
                ),
                (
                    "credential_type",
                    models.CharField(
                        choices=[("public-key", "Public Key")],
                        default="public-key",
                        editable=False,
                        max_length=32,
                        verbose_name="credential type",
                    ),
                ),
                (
                    "credential_id",
                    models.BinaryField(
                        max_length=1023, verbose_name="credential id data"
                    ),
                ),
                (
                    "public_key",
                    models.BinaryField(
                        max_length=1023, verbose_name="COSE public key data"
                    ),
                ),
                (
                    "transports",
                    models.JSONField(
                        default=list, editable=False, verbose_name="transports"
                    ),
                ),
                (
                    "sign_count",
                    models.PositiveIntegerField(
                        default=0, editable=False, verbose_name="sign count"
                    ),
                ),
                (
                    "backup_eligible",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="backup eligible"
                    ),
                ),
                (
                    "backup_state",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="backup state"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "last_used_at",
                    models.DateTimeField(null=True, verbose_name="last used at"),
                ),
                (
                    "aaguid",
                    models.CharField(
                        editable=False, max_length=36, verbose_name="AAGUID"
                    ),
                ),
                (
                    "credential_id_sha256",
                    models.BinaryField(
                        max_length=32, unique=True, verbose_name="hashed credential id"
                    ),
                ),
                (
                    "discoverable",
                    models.BooleanField(
                        default=None,
                        editable=False,
                        null=True,
                        verbose_name="discoverable",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user that this device belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "WebAuthn credential",
                "verbose_name_plural": "WebAuthn credentials",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WebAuthnAttestation",
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
                    "fmt",
                    models.CharField(
                        choices=[
                            ("packed", "packed"),
                            ("tpm", "tpm"),
                            ("android-key", "android-key"),
                            ("android-safetynet", "android-safetynet"),
                            ("fido-u2f", "fido-u2f"),
                            ("none", "none"),
                        ],
                        editable=False,
                        max_length=255,
                        verbose_name="format",
                    ),
                ),
                ("data", models.BinaryField(verbose_name="data")),
                (
                    "client_data_json",
                    models.BinaryField(verbose_name="client data JSON"),
                ),
                (
                    "credential",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attestation",
                        to="django_otp_webauthn.webauthncredential",
                        verbose_name="credential",
                    ),
                ),
            ],
            options={
                "verbose_name": "WebAuthn attestation",
                "verbose_name_plural": "WebAuthn attestations",
                "abstract": False,
            },
        ),
        migrations.AddIndex(
            model_name="webauthncredential",
            index=models.Index(
                fields=["credential_id_sha256"], name="webauthncredential_sha256_idx"
            ),
        ),
    ]
