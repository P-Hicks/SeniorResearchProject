from config import get_db_name


def setup1():
    from orm.manage import init_django
    db_name = get_db_name()
    print(f'DB: {db_name}')
    init_django(name=db_name)


def setup2():
    from orm.manage import migrate
    from orm.db import models

    migrate()