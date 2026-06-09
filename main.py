import os
import pandas as pd
from src.pipeline_dados import PipelineDadosPatentes
from src.classificador_ia import ClassificadorPatentesIA

if __name__ == '__main__':
    print("🚀 Inicializando Modelo com Dados Reais Ajustados do CETEM/MCTI")
    
    caminho_dados = os.path.join("C:/Users/T-Gamer/Documents/Desenvolvimento 2026/Classificador_Dados_Inpi/data", "patentes-2025.csv")
    
    if not os.path.exists(caminho_dados):
        raise FileNotFoundError(f"Arquivo não localizado em: {caminho_dados}")
        
    # 1. Carrega pulando as duas primeiras linhas de título institucional
    print("📖 Lendo arquivo CSV ignorando cabeçalho inválido...")
       # Altere a linha 16 do seu main.py para este formato robusto:
    df_real = pd.read_csv(caminho_dados, sep=None, engine='python', encoding='latin1')

    
    # Exibe as colunas no terminal apenas para validação visual sua
    print("Colunas detectadas:", df_real.columns.tolist())
    
    # Mapeamento com base na imagem real do seu LibreOffice
    df_real['resumo_texto'] = df_real['TITULO']  
    df_real['categoria_ipc'] = df_real['SITUACAO'] # Classificaremos a situação jurídica da patente
    
    # Remove registros nulos para não quebrar a IA
    df_real = df_real.dropna(subset=['resumo_texto', 'categoria_ipc'])
    
    # Salva a versão corrigida de forma temporária para o pipeline ler
    df_real.to_csv(caminho_dados, index=False)
    
    # 2. Executa o módulo de Limpeza e NLP
    pipeline = PipelineDadosPatentes()
    df_tratado = pipeline.executar_pipeline(caminho_dados)
    
    # 3. Executa o módulo de Machine Learning
    classificador = ClassificadorPatentesIA()
    modelo, vetorizador = classificador.treinar(df_tratado)
    
    print("\n✅ Script finalizado com sucesso usando a estrutura real do documento!")
