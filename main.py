# main.py
from gemini_config import configure_gemini, ask_gemini
from contexto import get_contexto
from instrucoes_sistema import get_instrucoes_sistema, construir_prompt
from resumo_conversa import gerar_resumo_profissional

def exibir_boas_vindas():
    """Exibe a mensagem de boas-vindas ao usuário."""
    print("Olá, me chamo Bonnie, sua assistente virtual.")
    print("Estou à disposição para esclarecer dúvidas sobre o Parque "
          "Tecnológico de Santos e ecossistemas de inovação.")
    print("Você pode fazer até 3 perguntas sobre esses assuntos!")
    print("-" * 60)


def coletar_perguntas_e_respostas(model, instrucoes, contexto):
    """
    Coleta as perguntas do usuário e gera as respostas usando o Gemini.

    Args:
        model: Modelo Gemini configurado
        instrucoes (str): Instruções do sistema
        contexto (str): Contexto sobre ecossistemas de inovação
    """
    respostas = []

    for i in range(3):
        print()  # Linha em branco para melhor formatação
        user_input = input(f"Pergunta {i+1}/3: ")

        # Constrói o prompt completo
        prompt = construir_prompt(instrucoes, contexto, user_input)

        # Obtém a resposta do Gemini
        resposta = ask_gemini(model, prompt)
        respostas.append((user_input, resposta))

        print(f"Bonnie: {resposta}")

    return respostas


def exibir_resumo_conversa(respostas):
    print("\n" + "=" * 60)
    print("RESUMO DA CONVERSA:")
    print("=" * 60)

    for idx, (pergunta, resposta) in enumerate(respostas, 1):
        print(f"\n{idx}) Pergunta: {pergunta}")
        print(f"   Resposta: {resposta}")

    print("\n" + "-" * 60)
    print("Obrigada por conversar! Para novas dúvidas, reinicie o chatbot.")


def main():
    """Função principal que coordena a execução do chatbot."""
    # Exibe mensagem de boas-vindas
    exibir_boas_vindas()

    # Configuração inicial
    model = configure_gemini()
    contexto = get_contexto()
    instrucoes = get_instrucoes_sistema()

    # Coleta perguntas e gera respostas
    respostas = coletar_perguntas_e_respostas(model, instrucoes, contexto)

    # Exibe resumo final
if __name__ == "__main__":
    main()
