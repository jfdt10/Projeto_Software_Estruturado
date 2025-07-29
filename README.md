# PROJETO ESTRUTURADO APP FITNESS

## Descrição

Aplicativo de fitness completo, desenvolvido em Python, utilizando arquitetura orientada a objetos e banco de dados TinyDB (JSON). O projeto inicialmente será no terminal com previsão futura para uso de interface de prototipagem streamlit.

## Funcionalidades Principais

- **Criação e gerenciamento de planos de treino personalizados**
- **Registro de atividades físicas**: passos, calorias gastas, exercícios realizados
- **Registro e análise da alimentação** e ingestão de nutrientes
- **Definição de metas** (ex: emagrecimento, hipertrofia) e acompanhamento do progresso
- **Compatibilidade com dispositivos vestíveis** (manual, simulado ou importação de CSV)
- **Compartilhamento de progresso** e participação em desafios com outros usuários
- **Acesso a vídeos e conteúdos instrutivos** sobre treinos e saúde
- **Recomendações personalizadas** de treino e nutrição
- **Sistema de avaliação e feedback** para treinos e programas
- **Fórum e comunidade** para suporte, dúvidas e motivação

## Estrutura do Projeto

```
fitness_app/
│
├── main.py                # Entrada do app no terminal (CLI)
├── app.py                 # Entrada para futura interface Streamlit
├── requirements.txt
├── fitness.json           # Banco de dados TinyDB
│
├── core/
│   ├── __init__.py
│   ├── database.py        # Setup TinyDB, funções CRUD, backup/import
│   ├── auth.py            # Cadastro/login de usuários
│   ├── models.py          # Classes principais (Usuário, PlanoTreino, etc.)
│   └── utils.py           # Funções auxiliares
│
├── services/
│   ├── workout.py         # Serviço de planos de treino
│   ├── activity.py        # Serviço de atividades físicas
│   ├── nutrition.py       # Serviço de nutrição
│   ├── goal.py            # Serviço de metas e progresso
│   ├── wearable.py        # Serviço de integração com wearables
│   ├── social.py          # Serviço de desafios e social
│   ├── video.py           # (Em breve) Serviço de vídeos
│   ├── recommendation.py  # (Em breve) Serviço de recomendações
│   ├── feedback.py        # (Em breve) Serviço de feedback
│   └── forum.py           # (Em breve) Serviço de fórum
│
├── data/
│   ├── workouts.json         # Exemplos de treinos prontos
│   ├── food_database.json    # Base de dados de alimentos
│   ├── metas.json            # Exemplos de metas
│   ├── wearable.csv   # Exemplo de dados de wearable
│   └── video_library.json    # (Em breve) Base de vídeos
```

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/jfdt10/Projeto_Software_Estruturado.git
   cd Projeto_Software_Estruturado
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

- **Terminal (CLI):**
  ```bash
  python fitness_app/main.py
  ```
- **Interface Web (em breve):**
  ```bash
  python fitness_app/app.py
  ```

## Licença

Este projeto está sob a licença MIT.

---

Se quiser, posso ajustar ou incluir mais detalhes específicos!
