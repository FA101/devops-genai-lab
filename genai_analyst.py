import os
import requests
import gitlab # Requer: pip install python-gitlab
from openai import OpenAI

# Configurações obtidas das variáveis de ambiente do GitLab CI
GITLAB_URL = "https://gitlab.com" # Ou sua instância on-premise
PROJECT_ID = os.getenv('CI_PROJECT_ID')
PIPELINE_ID = os.getenv('CI_PIPELINE_ID')
MR_IID = os.getenv('CI_MERGE_REQUEST_IID')
GITLAB_TOKEN = os.getenv('CI_JOB_TOKEN') # Token automático do job
OPENAI_KEY = os.getenv('OPENAI_API_KEY')

def get_failed_job_trace():
    """Busca o log do job 'unit_test' que falhou neste pipeline."""
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    # 1. Listar jobs do pipeline atual
    url = f"{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/pipelines/{PIPELINE_ID}/jobs"
    response = requests.get(url, headers=headers)
    jobs = response.json()
    
    for job in jobs:
        if job['name'] == 'unit_test' and job['status'] == 'failed':
            # 2. Baixar o trace (log) do job falho
            trace_url = f"{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/jobs/{job['id']}/trace"
            trace = requests.get(trace_url, headers=headers)
            return trace.text
    return None

def analyze_with_ai(error_log):
    """Envia o log para a OpenAI e recebe o diagnóstico."""
    client = OpenAI(api_key=OPENAI_KEY)
    
    prompt = f"""
    Você é um Engenheiro DevOps Sênior especialista em Python.
    Analise o seguinte log de erro de um pipeline de CI/CD.
    1. Identifique a causa raiz.
    2. Sugira a correção do código.
    3. Seja breve e didático.
    
    LOG DO ERRO:
    {error_log[-2000:]} # Enviando apenas os últimos 2000 caracteres para economizar tokens
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content

def post_comment_on_mr(message):
    """Posta a análise da IA como comentário no Merge Request."""
    if not MR_IID:
        print("Não estamos em um Merge Request. Imprimindo no console.")
        print(message)
        return

    url = f"{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/merge_requests/{MR_IID}/notes"
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    data = {"body": f"🤖 **Análise Automática de Falha (GenAI):**\n\n{message}"}
    requests.post(url, headers=headers, json=data)

if __name__ == "__main__":
    print("🔍 Buscando logs de falha...")
    log = get_failed_job_trace()
    
    if log:
        print("🧠 Log encontrado. Solicitando análise à IA...")
        analysis = analyze_with_ai(log)
        post_comment_on_mr(analysis)
        print("✅ Análise concluída e enviada.")
    else:
        print("❌ Nenhum job falho encontrado ou log inacessível.")