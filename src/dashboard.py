import streamlit as st
import pandas as pd
from connectors.prometheus_connector import fetch_prometheus_metrics
import logging

# Configura o nível de log como informativo
logging.basicConfig(level=logging.INFO)

# Título do dashboard
st.title("Painel de Telemetria")


# Função para tratar dados vazios ou com erros de forma amigável
def display_metrics(metrics_df, source):
  """
  Esta função exibe o DataFrame `metrics_df` na interface do Streamlit, 
  tratando casos onde o DataFrame esteja vazio ou contenha erros.

  Parâmetros:
      metrics_df (pd.DataFrame): O DataFrame contendo os dados de telemetria.
      source (str): A fonte dos dados (e.g., Supabase, ClickHouse).
  """
  if metrics_df.empty:
    st.warning(f"Não foram encontrados dados para {source}.")
  else:
    st.write(metrics_df)


# Busca métricas do Supabase
try:
  logging.info("Buscando métricas do Supabase...")
  supabase_metrics = fetch_prometheus_metrics('pg_stat_user_tables')  # Nome correto da métrica
  st.subheader("Métricas do Supabase")
  display_metrics(supabase_metrics, "Supabase")
except Exception as e:
  logging.error(f"Erro ao buscar métricas do Supabase: {e}")
  st.error(f"Erro ao buscar métricas do Supabase: {e}")

# Busca métricas do ClickHouse
try:
  logging.info("Buscando métricas do ClickHouse...")
  clickhouse_metrics = fetch_prometheus_metrics('clickhouse_table_size_bytes')  # Nome correto da métrica
  st.subheader("Métricas do ClickHouse")
  display_metrics(clickhouse_metrics, "ClickHouse")
except Exception as e:
  logging.error(f"Erro ao buscar métricas do ClickHouse: {e}")
  st.error(f"Erro ao buscar métricas do ClickHouse: {e}")