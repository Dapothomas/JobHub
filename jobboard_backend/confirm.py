from django.conf import settings

print(settings.DATABASES['default']['USER'])  # Will print 'dapo'
print(settings.DATABASES['default']['PASSWORD'])  # Will print 'hellothere'