from prometheus_api_client import PrometheusConnect
import pandas as pd
import logging


def connect_to_prometheus(url='http://localhost:9090'):
  """
  Esta função estabelece uma conexão com uma instância do Prometheus.

  Parâmetros:
      url (str, opcional): A URL da instância do Prometheus. O padrão é
                             "http://localhost:9090".

  Retorna:
      Objeto PrometheusConnect conectado.

  Exceções:
      Levanta uma exceção caso ocorra algum erro durante a conexão.
  """

  logging.info("Conectando ao Prometheus...")
  try:
    prom = PrometheusConnect(url=url, disable_ssl=True)
    logging.info("Conectado ao Prometheus.")
    return prom
  except Exception as e:
    logging.error(f"Erro ao conectar ao Prometheus: {e}")
    raise


def fetch_prometheus_metrics(metric_name, start_time=None, end_time=None):
  """
  Esta função busca métricas de uma instância do Prometheus.

  Parâmetros:
      metric_name (str): O nome da métrica a ser recuperada.
      start_time (str, opcional): Timestamp inicial para consulta (formato ISO8601).
      end_time (str, opcional): Timestamp final para consulta (formato ISO8601).

  Retorna:
      Um DataFrame do Pandas contendo os dados recuperados da métrica.

  Exceções:
      Levanta uma exceção caso ocorra algum erro durante a busca de dados.
  """

  prom = connect_to_prometheus()
  try:
    # Recupera o valor atual da métrica
    metrics_data = prom.get_current_metric_value(metric_name=metric_name)
    # Converte o dado JSON para um DataFrame do Pandas
    metrics_df = pd.json_normalize(metrics_data)
    return metrics_df
  except Exception as e:
    logging.error(f"Erro ao buscar métricas do Prometheus: {e}")
    raise