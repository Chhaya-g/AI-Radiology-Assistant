
class Config:
    SECRET_KEY = "dev secret key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///radiologyassistant.db"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MINUTES_BETWEEN_DUPLICATE_DELETION = 30
    SEARCH_CASES_PER_PAGE = 60

# class Config:
#     SECRET_KEY = "dev secret key"
#     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:chhaya31@localhost/radiologyassistant.db"  # Update with your MySQL credentials
#     MAX_CONTENT_LENGTH = 16 * 1024 * 1024
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     MINUTES_BETWEEN_DUPLICATE_DELETION = 30
#     SEARCH_CASES_PER_PAGE = 60
