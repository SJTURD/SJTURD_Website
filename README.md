# SJTURD_Website
SJTURD Website

## Requirements
Python 3.5

Django 1.10

React 15.3.1

## Cautions
* Some Constants
  ```Python
  STATIC_URL = '/static/'
  
  STATIC_ROOT = os.path.join(BASE_DIR, 'static')

  STATICFILES_DIRS = [
      os.path.join(BASE_DIR, 'public/static'),
  ]

  MEDIA_URL = '/media/'

  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```
  
* Every time static files are updated:
  ```Bash
  python manage.py collectstatic
  ```
  If something is deleted:
  ```Bash
  python manage.py collectstatic --clear
  ```
  
* Every time database schema is  updated:
  ```Bash
  python manage.py makemigrations [APP_NAME]
  ```
    
* Make sure you have applied all the migrations before run the server:
  ```Bash
  python manage.py migrate
  ```
  
* If you need any test data:
  ```Bash
  python manage.py loaddata [FIXTURE_NAME]
  ```