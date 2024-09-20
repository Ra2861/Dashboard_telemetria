import logging
import psycopg2
import pandas as pd
import sys
import os

# Adiciona o diretório raiz 'src' ao path do Python para importação relativa
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Importa as configurações do Supabase de config.py
from src.config.config import (
    SUPABASE_DB,
    SUPABASE_USER,
    SUPABASE_PASSWORD,
    SUPABASE_HOST,
    SUPABASE_PORT,
    TIMEOUT,
)


def connect_to_supabase():
    """
    Esta função estabelece uma conexão com o banco de dados PostgreSQL do Supabase.

    Ela utiliza as credenciais e configurações carregadas do arquivo de 
    configuração (config.py) para conectar ao banco de dados. Também configura 
    um limite de tempo para operações com o banco (statement_timeout) utilizando 
    o valor definido na variável TIMEOUT.

    Retorna:
        A conexão estabelecida com o banco de dados PostgreSQL do Supabase.

    Exceções:
        Levanta uma exceção psycopg2.Error caso ocorra algum erro durante a conexão.
    """

    logging.info("Conectando ao Supabase PostgreSQL...")
    try:
        conn = psycopg2.connect(
            dbname=SUPABASE_DB,
            user=SUPABASE_USER,
            password=SUPABASE_PASSWORD,
            host=SUPABASE_HOST,
            port=SUPABASE_PORT,
            options=f"-c statement_timeout={TIMEOUT}",
        )
        logging.info("Conexão com Supabase estabelecida.")
        return conn
    except psycopg2.Error as e:
        logging.error(f"Erro ao conectar ao Supabase: {e}")
        raise


def fetch_supabase_metrics():
    """
    Esta função busca dados de telemetria da base de dados Supabase.

    Primeiramente, ela estabelece uma conexão com o banco utilizando a função 
    `connect_to_supabase`. Em seguida, executa uma consulta para recuperar 
    informações sobre os esquemas, tabelas, número de linhas e tamanho total 
    utilizando a view `pg_stat_user_tables`.

    Por fim, converte o resultado da consulta para um DataFrame do Pandas e fecha 
    a conexão com o banco.

    Retorna:
        Um DataFrame do Pandas contendo os dados de telemetria recuperados.

    Exceções:
        Levanta uma exceção caso ocorra algum erro durante a busca de dados 
        ou fechamento da conexão.
    """

    conn = connect_to_supabase()
    query = """
    SELECT 
        schemaname,
        relname AS table_name,
        n_live_tup AS row_count,
        pg_size_pretty(pg_total_relation_size(relid)) AS total_size
    FROM 
        pg_stat_user_tables;
    """
    try:
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        logging.error(f"Erro ao buscar dados de telemetria do Supabase: {e}")
        conn.close()
        raise