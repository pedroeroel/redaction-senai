# Redaction - Plataforma Inteligente de Correção de Redação

> Projeto de Trabalho de Conclusão de Curso (TCC) focado na preparação para o ENEM através de inteligência artificial e gamificação.

## 📋 Sobre o Projeto

O **Redaction** é uma aplicação web full-stack desenvolvida para democratizar o acesso a correções de redação de qualidade. A plataforma permite que estudantes escrevam redações, recebam feedback instantâneo baseado nas 5 competências do ENEM, aprendam através de mini-aulas interativas e fixem o conteúdo com jogos educativos (gamificação).

## 🚀 Tecnologias Utilizadas

### Backend
*   **Linguagem:** Python 3.10+
*   **Framework Web:** Flask
*   **Banco de Dados:** Google Firebase Firestore (NoSQL)
*   **Autenticação:** Custom Session Management (via Flask Session)
*   **Gerenciamento de Ambiente:** python-dotenv

### Frontend
*   **Estrutura:** HTML5 (Jinja2 Templates)
*   **Estilização:** Tailwind CSS (via CDN para desenvolvimento ágil)
*   **Interatividade:** Vanilla JavaScript (ES6+)
*   **Visualização de Dados:** Chart.js (para gráficos de desempenho)
*   **Ícones:** Heroicons (SVG)

## ⚙️ Arquitetura do Banco de Dados (Firestore)

O sistema utiliza uma estrutura NoSQL baseada em coleções e documentos:

1.  **`register` (Coleção de Usuários)**
    *   Documento por usuário contendo: `username`, `email`, `password`, `score`, `admin` (bool), `completed_classes` (array).
    *   **Sub-coleção `essays`**: Armazena as redações do usuário, notas por competência e comentários.

2.  **`classes` (Conteúdo Global)**
    *   Armazena o conteúdo das mini-aulas interativas disponíveis para todos.

## 🛠️ Instalação e Configuração

### Pré-requisitos
*   Python 3.x instalado.
*   Conta no Firebase e arquivo de credenciais (`serviceAccountKey.json`).

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/pedroeroel/redaction-senai.git
    cd redaction-senai
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuração do Firebase:**
    *   Crie um projeto no console do Firebase.
    *   Gere uma nova chave privada em *Configurações do Projeto > Contas de Serviço*.
    *   Renomeie o arquivo baixado para `serviceAccountKey.json`.
    *   Mova este arquivo para a pasta `instance/` ou raiz do projeto.

5.  **Variáveis de Ambiente (.env):**
    Crie um arquivo `.env` na raiz se desejar passar a chave via string (opcional se usar o arquivo JSON):
    ```env
    SECRET_KEY=sua_chave_secreta_aqui
    ```

6.  **Execute a aplicação:**
    ```bash
    python run.py
    ```
    Acesse em: `http://127.0.0.1:5000`

## 📱 Funcionalidades Principais

1.  **Sistema de Redação:**
    *   Editor de texto com contador de linhas e caracteres em tempo real.
    *   Validação de critérios mínimos (ex: 7 linhas).
    *   Feedback visual com *loading states*.

2.  **Dashboard de Análise:**
    *   Gráficos (Pie Charts) detalhando a nota por competência.
    *   Histórico de evoluçāo.

3.  **Gamificação:**
    *   **Duelo de Conectivos:** Quiz para treinar coesão textual.
    *   **Corretor Fantasma:** Jogo de identificação de erros ortográficos.
    *   **Montador de Frases:** Drag-and-drop para estruturação sintática.
    *   Sistema de XP (Pontos) integrado ao banco de dados.

4.  **Temas Atuais:**
    *   Biblioteca de conteúdo com repertórios socioculturais, dados estatísticos e argumentos prontos para temas de alta relevância:
        *   Desigualdade Social no Brasil.
        *   Inteligência Artificial e Ética.
        *   Desafios da Educação Pública.
        *   Violência contra a Mulher.
        *   Inclusão de Pessoas com Deficiência.
        *   Saúde Mental entre os Jovens.

5.  **Painel Administrativo:**
    *   Visão geral de usuários cadastrados.
    *   Métricas globais da plataforma.

## 🎨 Design System

O projeto utiliza uma paleta de cores *Dark Mode* personalizada para conforto visual e modernidade:

*   **Background:** `#1F113B` (Roxo Profundo)
*   **Surface/Cards:** `#3D1E8D` e `#2A0F5E`
*   **Accent/Primary:** `#A78BFA` (Lilás)
*   **Text:** `#E8E1CF` (Beige Claro para alto contraste)
*   **Success/Error:** Tailwind standard colors (Emerald/Red).

## 📄 Autoria e Licenciamento

Este projeto foi desenvolvido para fins acadêmicos pela equipe AlphaTech, alunos do Técnico em Desenvolvimento de Sistemas na escola SENAI Luiz Pagliato (Sorocaba) em Itapeva.

A equipe foi composta por:

* [Pedro Eduardo Roel](https://linkedin.com/in/pedroedroel) (Dev. Fullstack)
* Mariana Meirelles (SCRUM Master)
* Joaquim Vitorino (Tech Lead)
* Yasmim Moraes (Dev. Frontend)

Acesse a [licença](LICENSE).

---

© 2024 AlphaTech. All rights reserved.