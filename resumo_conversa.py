# resumo_conversa.py
from gemini_config import ask_gemini

def gerar_resumo_profissional(respostas, model, instrucoes):
    """ Gera um resumo profissional da conversa utilizando IA para análise
    e síntese das informações discutidas."""

    conversa_completa = ""
    for idx, (pergunta, resposta) in enumerate(respostas, 1):
        conversa_completa += f"Pergunta {idx}: {pergunta}\n"
        conversa_completa += f"Resposta {idx}: {resposta}\n\n"

    instrucoes_resumo = """
        Você é um especialista em ecossistemas de inovação e deve gerar um
        resumo profissional e executivo da conversa apresentada.

        INSTRUÇÕES PARA O RESUMO:
        - Crie um resumo estruturado e profissional
        - Identifique os principais temas abordados
        - Destaque insights importantes mencionados
        - Organize as informações de forma lógica
        - Use linguagem técnica apropriada
        - Mantenha tom executivo e objetivo
        - Limite o resumo a 300-400 palavras
        - Use formatação simples sem markdown
        - Para listas, use hífen (-) seguido de espaço

        ESTRUTURA DO RESUMO:
        1. Introdução sobre os temas discutidos
        2. Principais pontos abordados (use lista com -)
        3. Insights e dados relevantes mencionados
        4. Conclusão sobre a importância dos temas

        """

    prompt_resumo = f"{instrucoes_resumo}\n{conversa_completa}\n\nRESUMO EXECUTIVO:"
    
    resumo = ask_gemini(model, prompt_resumo)
    return resumo
