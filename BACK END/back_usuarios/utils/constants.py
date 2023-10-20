JWT_SECRET_KEY = "fefa93357496f4115eb5b63d6a4d3c2b946988c15823f228a967dd120e93c9c0"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 1

# Base de datos LOCAL
LOCAL_DB = {
    'db_host':'localhost',
    'db_user':'postgres',
    'db_password':'1087423755',
    'db_database':'scenariojobs',
    'db_port':'5432'
}

# Base de datos AWS
# AWS_DB = {
#     'db_host':'rds-scenariojobs-database.cbd3bd42asse.us-east-1.rds.amazonaws.com',
#     'db_user':'postgres',
#     'db_password':'3hXEFQm%7;_6cp=z94',
#     'db_database':'rds_scenariojobs_database',
#     'db_port':'5432'
# }
AWS_DB = {
    'db_host':'rajje.db.elephantsql.com',
    'db_user':'hzndkfkd',
    'db_password':'YGJ5AYTW7zp20fbesImf2x0Fzww2JfT9',
    'db_database':'hzndkfkd',
    'db_port':'5432'
}

def get_db_data(env):
    if env == 'dev':
        return LOCAL_DB
    elif env == 'prod':
        return AWS_DB