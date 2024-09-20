import logging
import pandas as pd
from connectors.supabase_connector import fetch_supabase_metrics
from connectors.clickhouse_connector import fetch_clickhouse_metrics


def fetch_all_metrics():
    """
    Esta função recupera e combina métricas do Supabase e ClickHouse.

    Ela busca dados de ambas as fontes utilizando as funções 
    `fetch_supabase_metrics` e `fetch_clickhouse_metrics` definidas nos 
    módulos `connectors`. Em seguida, adiciona uma nova coluna `source` 
    aos DataFrames resultantes para identificar a origem dos dados 
    (Supabase ou ClickHouse).

    Por fim, concatena os DataFrames utilizando o método `pd.concat` e 
    retorna o DataFrame combinado contendo as métricas de ambas as fontes.

    Retorna:
        pd.DataFrame: DataFrame contendo as métricas combinadas.

    Exceções:
        Levanta uma exceção caso ocorra algum erro durante a busca ou 
        combinação dos dados.
    """

    try:
        # Busca métricas do Supabase
        logging.info("Buscando métricas do Supabase...")
        supabase_metrics = fetch_supabase_metrics()

        # Busca métricas do ClickHouse
        logging.info("Buscando métricas do ClickHouse...")
        clickhouse_metrics = fetch_clickhouse_metrics()

        # Adiciona coluna 'source' para identificar a origem dos dados
        supabase_metrics['source'] = 'Supabase'
        clickhouse_metrics['source'] = 'ClickHouse'

        # Combina os DataFrames
        logging.info("Combinando métricas do Supabase e ClickHouse...")
        combined_metrics = pd.concat([supabase_metrics, clickhouse_metrics], ignore_index=True)

        logging.info("Métricas combinadas com sucesso.")
        return combined_metrics

    except Exception as e:
        logging.error(f"Erro ao buscar ou combinar métricas: {e}")
        raise


if __name__ == "__main__":
    # Para fins de teste, você pode executar este script diretamente para ver os dados combinados
    metrics_df = fetch_all_metrics()
    print(metrics_df)