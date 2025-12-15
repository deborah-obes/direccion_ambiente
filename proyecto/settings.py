# Agregar al final
SITE_NAME = 'Dirección de Ambiente y Espacios Verdes'

INSTALLED_APPS += ['blog']

TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_URL = '/admin/login/'