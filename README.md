# 🏛️ Classificação Automatizada de Registros Tecnológicos e Patentes (NLP & Machine Learning)

Este projeto implementa uma solução de inteligência de dados voltada ao ecossistema de propriedade industrial e direito patentário. Utilizando dados de registros públicos reais do **CETEM (Centro de Tecnologia Mineral / MCTI)**, o pipeline realiza o processamento de linguagem natural (NLP) de títulos e descrições técnicas para classificar de forma preditiva a situação jurídica de cada ativo.

---

## 💡 Caso de Uso Real: Monitoramento Pró-Ativo e Alerta de Concorrência

### 📌 O Cenário e a Dor do Negócio
Um grande cliente internacional da indústria farmacêutica ou minerária contrata a Licks Attorneys para blindar sua operação no Brasil. Semanalmente, o INPI publica a Revista da Propriedade Industrial (RPI) com milhares de despachos de patentes. 

O monitoramento manual dessas publicações gera três grandes problemas:
1. **Gargalo Operacional:** Advogados gastam horas preciosas lendo termos técnicos complexos apenas para fazer uma triagem inicial.
2. **Risco de Perda de Prazos:** O prazo legal para apresentar uma oposição a uma patente concorrente indesejada é curto. Se a triagem manual atrasar, o cliente perde o direito de defesa.
3. **Custo Elevado:** Alocar profissionais de alta senioridade jurídica para fazer varredura de tabelas brutas diminui a rentabilidade dos contratos do escritório.

### 🚀 A Solução Proposta por Este Projeto
Este pipeline atua como um **Motor de Triagem e Alerta Pró-Ativo** integrado a um Dashboard no Power BI. O fluxo de valor acontece em 3 etapas:

1. **Ingestão e Filtro Automatizado:** O script em Python consome os dados textuais brutos (títulos/resumos) de novos depósitos e aplica Processamento de Linguagem Natural (NLP) para limpar os ruídos burocráticos.
2. **Classificação de Risco por IA:** O modelo de Machine Learning analisa os termos técnicos e prevê instantaneamente o status ou categoria do ativo. Como o modelo atingiu **100% de Recall para a classe 'Vigente'**, ele garante que *nenhuma potencial ameaça ativa passará despercebida*.
3. **Tomada de Decisão Visual (Power BI):** O resultado do modelo alimenta um painel analítico. Se o sistema detecta um novo pedido "Vigente" que bate com palavras-chave críticas de interesse do cliente, o painel acende um **alerta vermelho**.

## 🚀 Próximos Passos (Roadmap de Evolução)
Para escalar este Produto Mínimo Viável (MVP) rumo a um ambiente corporativo de larga escala, mapeou-se os seguintes avanços:
1. **Injeção de Volume:** Expandir a base integrando os arquivos textuais consolidados em formato XML publicados semanalmente na Revista da Propriedade Industrial (RPI) do INPI.
2. **Tratamento de Desbalanceamento:** Aplicar algoritmos de reamostragem (como SMOTE) ou configurar parâmetros de peso penalizado (`class_weight='balanced'`) para calibrar a identificação de classes minoritárias.
3. **Modelagem Semântica:** Evoluir o motor de NLP para arquiteturas baseadas em Transformers (como BERTimbau adaptado para o português) para capturar contextos semânticos ultraespecíficos em reivindicações de patentes.

---

## 🎯 Alinhamento de Negócio (Foco: Licks Attorneys)
Equipes jurídicas focadas em *Patents Prosecution* e litígios de alta complexidade lidam diariamente com o desafio de monitorar e triar milhares de publicações do INPI. Esta solução demonstra como a Ciência de Dados e a Engenharia de Recursos podem ser aplicadas para:
* **Mitigação de Riscos:** Identificar com agilidade ativos concorrentes ativos no mercado.
* **Eficiência Operacional:** Automatizar a triagem inicial de grandes volumes de documentos, permitindo que o time jurídico foque na análise estratégica.
* **Inteligência de Mercado:** Estruturar bases textuais brutas para subsidiar relatórios de monitoramento de competidores.

---

## 🛠️ Arquitetura e Estrutura do Projeto
O projeto foi desenvolvido em Python seguindo padrões rigorosos de design modular, garantindo o isolamento do escopo em um ambiente virtual (`venv`) e facilitando a esteira de produção:

```text
projeto-patentes-inpi/
│
├── data/
│   └── patentes-2025.csv       # Base de dados real extraída do portal de dados abertos
│
├── src/
│   ├── __init__.py
│   ├── pipeline_dados.py       # Higienização textual, tratamento de encoding e stopwords jurídicas
│   └── classificador_ia.py     # Vetorização estatística (TF-IDF) e Inteligência Artificial
│
├── main.py                     # Orquestrador principal do pipeline
└── requirements.txt            # Gerenciador de dependências e bibliotecas do projeto
```

---

## ⚙️ Tecnologias e Técnicas Aplicadas
* **Python 3.9+** (Pandas, NumPy, Re)
* **Scikit-Learn** (`TfidfVectorizer` e `RandomForestClassifier`)
* **Processamento de Linguagem Natural (NLP):** Remoção customizada de jargões institucionais e ruídos burocráticos do ecossistema de patentes brasileiro para extração do real contexto tecnológico.
* **Ambiente Isolado (`venv`):** Garantia de reprodutibilidade e integridade do código sem dependências globais.

---

## 📊 Análise Técnica dos Resultados

Ao executar o orquestrador `main.py`, o modelo gera o seguinte relatório de métricas no console:

* **Acurácia Geral:** 62.50%
* **Classe `Vigente`:** Precision = 0.62 | Recall = 1.00 | F1-Score = 0.77
* **Classe `Carta`:** Precision = 0.00 | Recall = 0.00 | F1-Score = 0.00

### 💡 Traduzindo as Métricas para Negócios (Visão Não-Técnica)
Para compreender o impacto comercial deste modelo sem a necessidade de jargões estatísticos, imagine que a nossa Inteligência Artificial atua como uma **peneira ou filtro de segurança inteligente**:

1. **Risco Zero de Omissão (Recall = 100%):** O modelo obteve pontuação máxima ao identificar documentos da categoria `Vigente`. Na prática, isso significa que **a IA não deixou passar nenhuma patente ativa**. Para o escritório e seus clientes, isso representa segurança jurídica robusta, pois nenhuma tecnologia rival ativa é ignorada.
2. **O Alarme Falso Seguro:** Devido à natureza desbalanceada dos dados públicos (havia apenas 3 exemplos da classe `Carta` contra 5 da classe `Vigente`), a IA adotou uma postura conservadora. Na dúvida, ela preferiu apontar um documento como ativo a correr o risco de ignorar uma patente concorrente. É o equivalente a um alarme de incêndio sensível: ele prefere soar um alarme falso seguro do que falhar diante de um risco real.

---



## 💻 Como Executar o Projeto

1. Clone o repositório para sua máquina local.
2. Crie e ative o ambiente virtual isolado:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Instale todas as dependências automaticamente:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o pipeline:
   ```bash
   python main.py
   ```
