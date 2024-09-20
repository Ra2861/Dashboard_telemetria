import logging
import clickhouse_connect
import pandas as pd
import sys
import os

# Adiciona o diretório raiz 'src' ao path do Python para importação relativa
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Importa as configurações do ClickHouse de config.py
from src.config.config import (
    CLICKHOUSE_HOST,
    CLICKHOUSE_PORT,
    CLICKHOUSE_USER,
    CLICKHOUSE_PASSWORD,
    CLICKHOUSE_DB,
)


def connect_to_clickhouse():
    """
    Esta função estabelece uma conexão com o ClickHouse.

    Ela configura o cliente ClickHouse utilizando as credenciais e configurações
    carregadas do arquivo de configuração (config.py).

    Retorna:
        O objeto cliente ClickHouse conectado.

    Exceções:
        Levanta uma exceção caso ocorra algum erro durante a conexão.
    """

    logging.info("Conectando ao ClickHouse...")
    try:
        client = clickhouse_connect.get_client(
            host=CLICKHOUSE_HOST,
            port=CLICKHOUSE_PORT,
            username=CLICKHOUSE_USER,
            password=CLICKHOUSE_PASSWORD,
            database=CLICKHOUSE_DB,
            secure=True,  # Habilita conexão segura (verifique a necessidade)
            verify=False,  # Desabilita verificação de certificado (verifique a necessidade)
        )
        logging.info("Conexão com ClickHouse estabelecida.")
        return client
    except Exception as e:
        logging.error(f"Erro ao conectar ao ClickHouse: {e}")
        raise


def fetch_clickhouse_metrics():
    """
    Esta função busca métricas do ClickHouse.

    Ela primeiro estabelece uma conexão com o ClickHouse utilizando a função
    `connect_to_clickhouse`. Em seguida, executa uma consulta para recuperar dados
    da tabela `grupox` (certifique-se de alterar para a tabela correta). 

    Finalmente, converte o resultado da consulta para um DataFrame do Pandas e o retorna.

    Retorna:
        Um DataFrame do Pandas contendo os dados recuperados.

    Exceções:
        Levanta uma exceção caso ocorra algum erro durante a busca de dados.
    """

    client = connect_to_clickhouse()
    query = "SELECT * FROM grupox"  # Altere para a tabela correta
    try:
        result = client.query(query)
        df = pd.DataFrame(result.result_rows, columns=result.column_names)
        return df
    except Exception as e:
        logging.error(f"Erro ao buscar dados do ClickHouse: {e}")
        raise