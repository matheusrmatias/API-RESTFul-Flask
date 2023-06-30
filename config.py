# Ativa modo debug do Flask
DEBUG = True

# Inserir nome de usuário do Banco de Dados
USERNAME = ''
# Inserir a senha Banco de Dados
PASSWORD = ''
# Inserir servidor do Banco de Dados (localhost)
SERVER = ''
# Inserir o database
DB = ''

# Conexão com o Banco de Dados
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True