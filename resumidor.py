from google import genai

# 1. Configurando a sua chave
GOOGLE_API_KEY = "SUA_CHAVE_AQUI"
client = genai.Client(api_key=GOOGLE_API_KEY)

print("=== BEM-VINDO AO RESUMIDOR INTELIGENTE ===")
print("Cole ou digite o texto que você deseja resumir.")
print("DICA: Após colar o texto, aperte Enter e digite a palavra FIM para a IA começar.\n")

# 2. Lógica para receber o texto do usuário
linhas_do_texto = []
while True:
    linha = input()
    if linha.strip().upper() == 'FIM':
        break
    linhas_do_texto.append(linha)

texto_do_usuario = '\n'.join(linhas_do_texto)

# 3. O comando (prompt) que daremos para a IA
comando = f"Por favor, atue como um assistente e faça um resumo em 3 tópicos curtos e diretos do seguinte texto:\n{texto_do_usuario}"

print("\nConectando com a IA e gerando resumo... Aguarde um instante.\n")

# 4. Enviando o pedido usando a nova Interactions API e o Gemini 3.6 Flash
interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input=comando
)

print("=== RESUMO GERADO COM SUCESSO ===")
print(interaction.output_text)