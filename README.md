# 🚀 Projeto Integrador: DevOps com GenAI

Especialização em Engenharia de Software: Automação e Inovação com Inteligência Artificial Generativa.

## 🎯 Objetivo
Demonstrar a integração prática entre um pipeline de CI/CD no GitLab e um agente de Inteligência Artificial Generativa (OpenAI) para diagnóstico automático de falhas de build.

## 🛠️ Arquitetura

1.  **Aplicação:** `OrderService` (Python/Flask) com um bug intencional de tipagem (`TypeError`).
2.  **Pipeline:** GitLab CI configurado para detectar a falha nos testes.
3.  **Agente IA:** Script Python que captura o log de erro e consulta a API da OpenAI.
4.  **Feedback:** A explicação do erro é postada automaticamente no Merge Request.

## 📋 Pré-requisitos para Execução

Para rodar este projeto no seu ambiente GitLab, você precisará configurar as seguintes variáveis em **Settings > CI/CD > Variables**:

* `OPENAI_API_KEY`: Sua chave de API da OpenAI (começa com `sk-...`).

> **Nota:** O script utiliza o `CI_JOB_TOKEN` nativo do GitLab para autenticação interna, não sendo necessário criar tokens pessoais do GitLab para esta demo.

## 🏃 Como testar a automação

1.  Crie uma nova branch a partir da `main`.
2.  Faça uma alteração trivial em qualquer arquivo (ex: adicione um comentário no `app.py`) e faça o commit.
3.  Abra um **Merge Request** para a `main`.
4.  Observe o pipeline:
    * O job `unit_test` irá falhar (❌).
    * O job `ai_debugger` será acionado automaticamente.
5.  Acesse a aba **Overview** do seu Merge Request e aguarde o comentário do bot.

## 🧠 Exemplo de Análise da IA

> **Diagnóstico:** O erro `TypeError: unsupported operand type(s) for +: 'float' and 'str'` indica que o código tentou somar um número decimal com um texto.
> **Correção:** Converta a variável `tax` para float antes de somar: `float(tax)`.

## ⚠️ Isenção de Responsabilidade
Este projeto utiliza IA para sugerir correções. As sugestões devem ser sempre validadas por um humano antes de serem aplicadas em produção.