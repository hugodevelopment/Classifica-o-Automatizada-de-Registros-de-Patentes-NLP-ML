import re
import pandas as pd

class PipelineDadosPatentes:
    def __init__(self):
        # Stopwords estendidas com termos burocráticos do INPI e institucionais do CETEM
        self.jargoes_inpi = [
            'a', 'o', 'e', 'do', 'da', 'em', 'para', 'com', 'um', 'uma', 'os', 'as',
            'presente', 'invenção', 'refere-se', 'relatório', 'descritivo', 'caracterizado',
            'compreende', 'patente', 'pedido', 'reivindicação', 'método', 'dispositivo',
            'cetem', 'mcti', 'tecnologia', 'mineral', 'minerais', 'processo', 'desenvolvimento'
        ]

    def limpar_texto(self, texto):
        """Aplica etapas de limpeza textual em uma string individual."""
        if not isinstance(texto, str):
            return ""
        
        # Converter para minúsculo
        texto = texto.lower()
        
        # Remover caracteres especiais e números
        texto = re.sub(r'[^a-zA-Záéíóúàèìòùâêîôûãõç\s]', '', texto)
        
        # Remover jargões repetitivos e stopwords
        palavras = texto.split()
        palavras_filtradas = [p for p in palavras if p not in self.jargoes_inpi]
        
        return " ".join(palavras_filtradas)

    def executar_pipeline(self, caminho_csv):
        """Carrega o arquivo e retorna o DataFrame com os dados textuais tratados."""
        print("🧼 Executando pipeline de limpeza de texto (NLP)...")
        
        # Carrega o arquivo garantindo codificação padrão
        df = pd.read_csv(caminho_csv)
        
        # A coluna 'texto_limpo' será gerada a partir da coluna mapeada no main.py
        df['texto_limpo'] = df['resumo_texto'].apply(self.limpar_texto)
        
        print("✅ Dados textuais processados com sucesso.")
        return df
