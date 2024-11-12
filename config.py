class Config:
    DB_NAME = 'db'
    SHOULD_PRINT = False

config = Config()

def get_db_name():
    return config.DB_NAME

def set_db_name(value):
    print(f'set DB name to {value} {type(value)}')
    config.DB_NAME = value


def set_should_print(value):
    print(f'set should print to {value} {type(value)}')
    config.SHOULD_PRINT = value

def check_should_print():
    print(f'should print: {config.SHOULD_PRINT}')

def get_should_print():
    return config.SHOULD_PRINT