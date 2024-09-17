def setup1():
    from orm.manage import init_django

    init_django()


def setup2():
    from orm.manage import migrate
    from orm.db import models

    migrate()