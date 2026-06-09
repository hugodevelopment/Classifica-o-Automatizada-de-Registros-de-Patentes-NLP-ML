from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

class ClassificadorPatentesIA:
    def __init__(self, max_features=300):
        # Reduzimos um pouco o max_features para ajustar ao volume textual do CETEM
        self.vectorizer = TfidfVectorizer(max_features=max_features)
        self.modelo = RandomForestClassifier(n_estimators=100, random_state=42)

    def treinar(self, df):
        """Vetoriza o texto tratado e treina o classificador supervisionado."""
        print("🤖 Vetorizando termos de tecnologia (TF-IDF)...")
        X = self.vectorizer.fit_transform(df['texto_limpo'])
        y = df['categoria_ipc']
        
        # Divisão simples de treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
        
        print("🏋️ Treinando o modelo Random Forest da Inteligência Artificial...")
        self.modelo.fit(X_train, y_train)
        
        # Rodar predições de teste e avaliar
        predicoes = self.modelo.predict(X_test)
        self._exibir_metricas(y_test, predicoes)
        
        return self.modelo, self.vectorizer

    def _exibir_metricas(self, y_true, y_pred):
        """Exibe no console os resultados técnicos da performance do modelo."""
        print("\n📊 --- RESULTADOS TÉCNICOS DA IA ---")
        print(f"Acurácia Geral: {accuracy_score(y_true, y_pred) * 100:.2f}%")
        print("\nRelatório de Classificação por Categoria (Métricas Completas):")
        # zero_division=0 evita travamentos caso alguma categoria pequena não seja classificada
        print(classification_report(y_true, y_pred, zero_division=0))
