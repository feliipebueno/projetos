from django.core.exceptions import ValidationError

def file_size(value):
    filesize = value.size
    if filesize > 10485760:
        raise ValidationError("O tamanho maximo do arquivo não pode ser maior que 10MB")
    else:
        return value