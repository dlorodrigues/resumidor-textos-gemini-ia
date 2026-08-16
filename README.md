# 📝 Resumidor de Textos com IA (Google Gemini)

## 📖 Sobre o Projeto
Este é o meu primeiro projeto prático focado na integração de Inteligência Artificial com programação. Desenvolvi um script interativo em Python que utiliza a API mais moderna do Google Gemini para ler textos longos e gerar resumos automáticos em tópicos curtos e diretos, facilitando a produtividade.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python
* **Inteligência Artificial:** API do Google Gemini (Interactions API)
* **Ferramentas:** Cursor, Git / GitHub

## 📸 Demonstração do Projeto
*(Abaixo está a captura de tela do projeto rodando no terminal)*

![Funcionamento do Resumidor](/assets/resumidor-gemini.png)
---

## 💡 Exemplo de Uso Prático

**Texto Original (O que o usuário digita):**
> O papel de cuidar de uma pessoa idosa vai muito além de garantir a alimentação e a medicação nos horários corretos. Trata-se de um ato de profunda empatia e conexão humana. Muitas vezes, quem cuida enfrenta uma jornada exaustiva, equilibrando as exigências físicas da rotina com a carga emocional de acompanhar de perto as limitações de alguém, o que exige muita paciência e dedicação diária. A saúde emocional de quem exerce essa função precisa ser uma prioridade, embora frequentemente seja negligenciada. Sentimentos de sobrecarga e estresse são comuns na rotina. Por isso, buscar redes de apoio, ter momentos de descanso e procurar orientações para lidar com as emoções não é um sinal de fraqueza, mas sim uma ferramenta essencial para manter a própria saúde mental em dia. Além disso, a escuta ativa é uma das habilidades mais valiosas nesse processo. Parar para ouvir as memórias e histórias de uma vida inteira traz um conforto imensurável para quem está sendo cuidado, fortalecendo a relação e tornando o ambiente mais seguro. Quem cuida é um pilar fundamental, e zelar por si mesmo é o primeiro passo para conseguir oferecer o melhor apoio ao outro.

**Resposta da Inteligência Artificial (Resultado final):**
> * **Empatia e dedicação diária:** Cuidar de um idoso vai além das tarefas físicas, exigindo paciência e preparo para lidar com o desgaste emocional da rotina.
> * **Importância do autocuidado:** A saúde mental do cuidador é prioridade; buscar momentos de descanso e redes de apoio é essencial para evitar o estresse e a sobrecarga.
> * **Conexão pela escuta ativa:** Ouvir as histórias e memórias do idoso fortalece os laços afetivos e traz conforto, tornando o cuidado mais humano e eficiente.

---

## 💻 Como rodar o projeto no seu computador

1. Baixe o arquivo `resumidor.py`.
2. Instale a biblioteca do Google executando o comando no terminal: 
   ```bash
   pip install google-genai

Crie uma chave de API gratuita no site do Google AI Studio.

Substitua a frase "SUA_CHAVE_AQUI" dentro do código pela sua chave gerada.

Execute o programa digitando no terminal:

python resumidor.py