from django.conf import settings


LISTENCLOSELY_YOWSUP_NUMBER = getattr(settings, 'LISTENCLOSELY_YOWSUP_NUMBER', None)

LISTENCLOSELY_YOWSUP_PASS = getattr(settings, 'LISTENCLOSELY_YOWSUP_PASS', None)

LISTENCLOSELY_YOWSUP_ENCRYPTION = getattr(settings, 'LISTENCLOSELY_YOWSUP_ENCRYPTION', True)

LISTENCLOSELY_YOWSUP_TOP_LAYERS = getattr(settings, 'LISTENCLOSELY_YOWSUP_TOP_LAYERS', None)
