# Chatbot Bonnie - Ecossistemas de Inovação

## 📋 Descrição do Projeto

O **Chatbot Bonnie** é um assistente virtual inteligente desenvolvido em Python que utiliza a API do Google Gemini para responder perguntas especializadas sobre ecossistemas de inovação no Brasil, com foco especial no Parque Tecnológico de Santos.

### 🎯 Funcionalidades Principais

- **Assistente Especializada**: Bonnie possui conhecimento específico sobre ecossistemas de inovação, parques tecnológicos, startups e empreendedorismo no Brasil
- **Interação Limitada**: Permite exatamente 3 perguntas por sessão para manter foco na conversa
- **Controle de Escopo**: Rejeita automaticamente perguntas fora do tema de inovação tecnológica
- **Resumo Executivo**: Gera um resumo profissional da conversa utilizando IA

### 🏢 Área de Negócio

O projeto foca no **ecossistema de inovação brasileiro**, abrangendo:
- Parques tecnológicos e científicos
- Startups e empreendedorismo
- Políticas públicas de CT&I
- Incubadoras e aceleradoras
- Transferência de tecnologia universidade-empresa
- Dados e estatísticas do setor

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.11 ou superior
- Biblioteca `google-generativeai`
- Chave de API do Google Gemini (gratuita)
- Conexão com a internet

### Passo a Passo Detalhado

1. **Clone o repositório:**
   ```bash
   git clone [URL-DO-REPOSITORIO]
   cd Projeto1
   ```

2. **Instale as dependências:**
   ```bash
   pip install google-generativeai
   ```

3. **Configure a chave de API do Gemini:**
   
   **3.1 - Obtenha sua chave de API gratuita:**
   - Acesse: https://aistudio.google.com/app/apikey
   - Faça login com sua conta Google
   - Clique em "Create API Key" ou "Criar chave de API"
   - Selecione "Create API key in new project" se for seu primeiro projeto
   - Copie a chave gerada 
   - **⚠️ AVISO**: Guarde a chave em local seguro, ela não será exibida novamente

   **3.2 - Configure no arquivo `gemini_config.py`:**
   - Abra o arquivo `gemini_config.py` no seu editor de texto
   - Localize a linha que contém `genai.configure(api_key=...)`
   - Substitua `"YOUR_API_KEY_HERE"` pela sua chave do Gemini

4**Execute o chatbot:**
   ```bash
   python main.py
   ```

### Estrutura de Arquivos

```
📁 Projeto1/
├── 📄 main.py                 # Arquivo principal de execução
├── 📄 gemini_config.py        # Configuração da API Gemini
├── 📄 contexto.py             # Contexto para IA 
├── 📄 instrucoes_sistema.py   # Instruções para o modelo IA
├── 📄 resumo_conversa.py      # Geração do resumo da conversa
├── 📄 README.md               # Arquivo README
└── 📁 __pycache__/           # Arquivos Python compilados
```