from orm.manage import init_django, migrate

init_django()

from orm.db.models import *

migrate()