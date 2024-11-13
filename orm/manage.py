
def init_django(name='db'):
    import django
    from django.conf import settings

    if settings.configured:
        return

    settings.configure(
        INSTALLED_APPS=[
            'orm.db',
        ],
        DATABASES={
           'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': f'{name}.sqlite3', # This is where you put the name of the db file. 
                        # If one doesn't exist, it will be created at migration time.
                'OPTIONS': {
                    # 'timeout': 20,  # Optional: Increase the timeout for lock contention
                    # 'journal_mode': 'WAL',  # Enable Write-Ahead Logging
                }
            }
        }
    )
    django.setup()
    # from django.core.management import execute_from_command_line
    # execute_from_command_line(['migrate'])


def migrate():
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', "migrate"])



if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    import django
    from django.conf import settings

    if settings.configured:
        exit()

    settings.configure(
        INSTALLED_APPS=[
            'db',
        ],
        DATABASES={
           'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3', # This is where you put the name of the db file. 
                        # If one doesn't exist, it will be created at migration time.
            }
        }
    )
    django.setup()
    execute_from_command_line()
