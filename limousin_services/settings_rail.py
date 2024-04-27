from  limousin_services.settings import *

from decouple import config

SECRET_KEY = config('SECRET_KEY')



ALLOWED_HOSTS = [
    'web-production-a0bb7.up.railway.app',
    
    ]  


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    # Add other origins if needed
]

#Code that relies on the configuration variables
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)



#ALLOWED_HOSTS = ['127.0.0.1']  