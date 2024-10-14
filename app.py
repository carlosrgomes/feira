import streamlit as st

# Definindo perguntas e respostas sobre Beatriz Souza
faq = {
    "Quem é Beatriz Souza?": "Beatriz Souza é uma judoca, sargento do exército e campeã olímpica brasileira. Beatriz conqistou a primeira medalha olímpica de ouro do Brasil de 2024 em Paris e com isso se tornou a primeira mulhera conquistar uma medalha olímpica de ouro na história do Esporte Clube Pinheiros.).",
    "Quais são as medalhas de Beatriz Souza?": "Jogos olímpicos (2 medalhas); Campeonatos mundiais (6 )  Grand slam da FIJ ( 12 ) Jogos pan-americanos ( 3 ) Campeonatos pan-americanos ( 7 ) Campeonato mundial sênior ( 2 ).",
    "Qual é a influência de Beatriz Souza?": "Sua dedicação ao esporte e sua perseverança em um ambiente altamente competitivo fazem dela uma das principais representantes do Brasil no judô feminino. Assim ela contribui para o fortalecimento da imagem do esporte no Brasil e para a valorização das atletas femininas em uma modalidade tradicionalmente dominada pelos homens.",
    "Qual foi a lesão de Beatriz Souza?": "Uma das lesões de Beatriz Souza foi no cotovelo, onde chegava em casa com um esparadrapo e tinham que cortar para ela, Beatriz tratou sua lesão bilateral no cotovelo com fisioterapia e outras medidas para ela conseguir voltar a competir antes das olimpíadas, ela agora acha muito mais importante cuidar do corpo.",
    "Como Beatriz Souza começou no judô?": "A atleta se apaixonou pelo judô quando tinha apenas 7 anos. “Eu era uma criança cheia de energia, tentei natação e dança, mas nada me parava, até que eu conheci o judô”.",
    "Aonde Beatriz Souza nasceu?": "Ela nasceu em Itariri, São Paulo, mas cresceu em Peruíbe, São Paulo.",
}

st.title("💬 Chatbot sobre Beatriz Souza")

# Inicializando a sessão
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Me faça perguntas sobre Beatriz Souza."}]

# Exibindo mensagens anteriores
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Opções de perguntas para o selectbox
questions = list(faq.keys())
questions.insert(0, "Selecione uma pergunta...")  # Adicionando uma opção inicial

# Usando selectbox para perguntas
selected_question = st.selectbox("Escolha uma pergunta:", questions)

if selected_question != "Selecione uma pergunta...":
    st.session_state.messages.append({"role": "user", "content": selected_question})
    st.chat_message("user").write(selected_question)

    # Obtendo a resposta com base na pergunta do usuário
    response = faq.get(selected_question, "Desculpe, não sei a resposta para essa pergunta.")
    
    # Adicionando a mensagem do assistente ao histórico de mensagens
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Exibindo a mensagem do assistente na interface
    st.chat_message("assistant").write(response)