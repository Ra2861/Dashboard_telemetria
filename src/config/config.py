# Importa a biblioteca `os` para manipulação do sistema operacional
import os

# Importa a biblioteca `dotenv` para carregar variáveis de ambiente de um arquivo .env
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env (se existir)
load_dotenv()

# ## Configurações do Supabase

# URL do banco de dados Supabase (carregada da variável de ambiente SUPABASE_DB)
SUPABASE_DB = os.getenv("SUPABASE_DB")

# Usuário do banco de dados Supabase (carregado da variável de ambiente SUPABASE_USER)
SUPABASE_USER = os.getenv("SUPABASE_USER")

# Senha do banco de dados Supabase (carregado da variável de ambiente SUPABASE_PASSWORD)
SUPABASE_PASSWORD = os.getenv("SUPABASE_PASSWORD")

# Host do Supabase (carregado da variável de ambiente SUPABASE_HOST)
SUPABASE_HOST = os.getenv("SUPABASE_HOST")

# Porta do Supabase (carregado da variável de ambiente SUPABASE_PORT)
SUPABASE_PORT = os.getenv("SUPABASE_PORT")

# Tempo limite de conexão (carregado da variável de ambiente TIMEOUT, default 600 segundos)
TIMEOUT = os.getenv("TIMEOUT", 60000000000)  # Valor padrão em nanossegundos

# ## Configurações do ClickHouse

# Host do ClickHouse (carregado da variável de ambiente CLICKHOUSE_HOST)
CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST")

# Porta do ClickHouse (carregado da variável de ambiente CLICKHOUSE_PORT)
CLICKHOUSE_PORT = os.getenv("CLICKHOUSE_PORT")

# Usuário do ClickHouse (carregado da variável de ambiente CLICKHOUSE_USER)
CLICKHOUSE_USER = os.getenv("CLICKHOUSE_USER")

# Senha do ClickHouse (carregado da variável de ambiente CLICKHOUSE_PASSWORD)
CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD")

# Banco de dados ClickHouse (carregado da variável de ambiente CLICKHOUSE_DB)
CLICKHOUSE_DB = os.getenv("CLICKHOUSE_DB")