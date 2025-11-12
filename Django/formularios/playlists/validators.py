# playlists/validators.py

from django.core.exceptions import ValidationError


def validate_music_length(value):
    if value not in range(1, 3601):
        raise ValidationError(
            f"A duração da música deve ser um número"
            f" inteiro entre 1 e 3600 segundos. O valor "
            f"{value} não é válido."
        )


def validate_name(value):
    if any(
        char.isdigit() for char in value
    ):  # checa se algum dos caracteres é um dígito
        raise ValidationError("O nome não pode conter números.")
