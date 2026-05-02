import streamlit as st

st.set_page_config(page_title="Simulado Concurso AEE", layout="wide")

# =========================
# QUESTÕES COMPLETAS
# =========================

questoes = [

# =========================
# CONHECIMENTOS GERAIS
# =========================

{
"pergunta": """Q1 - As políticas contemporâneas de acessibilidade comunicacional...

I. Sustentabilidade depende apenas de estrutura e recursos.
II. Comunicação alternativa integrada desconstrói hierarquias.
III. Capacitação envolve reflexão crítica.

É correto:""",
"opcoes":[
"II e III, apenas",
"I e III, apenas",
"I, II e III",
"II, apenas",
"I, apenas"
],
"resposta":0
},

{
"pergunta": """Q2 - Leitura, tecnologia e cidadania:

I. Leitura deve ser obrigatória com controle rígido.
II. Formação depende de múltiplas dimensões.
III. Recursos digitais podem ajudar.

É correto:""",
"opcoes":[
"I, apenas",
"II e III, apenas",
"I, II e III",
"II, apenas",
"I e III, apenas"
],
"resposta":1
},

{
"pergunta":"Q3 - Função das comissões intergestoras no SNE:",
"opcoes":[
"Autonomia total sem padrão",
"Definir currículo nacional único",
"MEC decide tudo",
"Espaço de diálogo e pactuação",
"Apenas consultivo"
],
"resposta":3
},

{
"pergunta":"Q4 - Abandono afetivo no ECA relaciona-se a:",
"opcoes":[
"Hierarquia de direitos",
"Responsabilidade penal",
"Escola substitui família",
"Separação escola-família",
"Integração emocional e desenvolvimento"
],
"resposta":4
},

{
"pergunta":"Q5 - Notificação de risco nas escolas:",
"opcoes":[
"Criminalização",
"Padronização rígida",
"Transferência total ao judiciário",
"Proteção integral articulada",
"Vigilância invasiva"
],
"resposta":3
},

{
"pergunta":"Q6 - Educação em direitos humanos:",
"opcoes":[
"Ação paralela",
"Eventos isolados",
"Dignidade + inclusão + combate discriminação",
"Complemento opcional",
"Foco urbano"
],
"resposta":2
},

{
"pergunta":"Q7 - Educação digital deve:",
"opcoes":[
"Priorizar hardware",
"Somente acesso",
"Ignorar inclusão",
"Foco em ferramentas",
"Integração crítica e cidadã"
],
"resposta":4
},

{
"pergunta":"Q8 - Avaliação de políticas educacionais:",
"opcoes":[
"Processo complexo e permanente",
"Padrões ideais rígidos",
"Protocolos padronizados",
"Avaliação isolada",
"Ciclos fixos"
],
"resposta":0
},

{
"pergunta":"Q9 - Financiamento educacional:",
"opcoes":[
"Capacidade cognitiva",
"Mais dinheiro = melhor",
"Gestão + equidade",
"Limite atingido",
"Só fator social"
],
"resposta":2
},

{
"pergunta":"Q10 - Estratégia sobre internet nas escolas:",
"opcoes":[
"Reduzir acesso",
"Restrição + educação digital + inclusão",
"Proibir geral",
"Ignorar desigualdade",
"Liberar geral"
],
"resposta":1
},

# =========================
# METODOLOGIA
# =========================

{
"pergunta":"Q11 - Aprendizagem cognitiva:",
"opcoes":[
"Interpretação",
"Mediação",
"Reorganização sistêmica",
"Heurística",
"Interação recursiva"
],
"resposta":2
},

{
"pergunta":"Q12 - Espaços extraescolares:",
"opcoes":[
"Sem planejamento",
"Depende tecnologia",
"Igual escola",
"Enriquecem com articulação pedagógica",
"Substituem escola"
],
"resposta":3
},

{
"pergunta":"Q13 - Juventude e participação:",
"opcoes":[
"I e III",
"III",
"I, II e III",
"I e II",
"II"
],
"resposta":3
},

{
"pergunta":"Q14 - Metodologia pedagógica:",
"opcoes":[
"I e II",
"I, II e III",
"II",
"III",
"I e III"
],
"resposta":0
},

{
"pergunta":"Q15 - Função social da escola:",
"opcoes":[
"I",
"I, II e III",
"III",
"I e II",
"II e III"
],
"resposta":1
},

{
"pergunta":"Q16 - Organização do ensino:",
"opcoes":[
"II e III",
"III",
"I",
"I e II",
"I, II e III"
],
"resposta":4
},

{
"pergunta":"Q17 - Associação:",
"opcoes":[
"2-3-1",
"1-3-2",
"2-1-3",
"3-2-1",
"1-2-3"
],
"resposta":4
},

{
"pergunta":"Q18 - Associação PPP:",
"opcoes":[
"2-1-3",
"3-1-2",
"1-2-3",
"2-3-1",
"1-3-2"
],
"resposta":0
},

{
"pergunta":"Q19 - PPP V/F:",
"opcoes":[
"F-F-V",
"F-V-F",
"V-F-F",
"V-F-V",
"V-V-F"
],
"resposta":3
},

{
"pergunta":"Q20 - Inclusão escolar:",
"opcoes":[
"Protagonismo social",
"Filantropia",
"Igualdade histórica",
"Estado central",
"Universalização"
],
"resposta":0
},

# =========================
# AEE
# =========================

{
"pergunta":"Q21 - Público da Educação Especial:",
"opcoes":[
"A",
"B",
"C",
"D",
"E"
],
"resposta":2
},

{
"pergunta":"Q22 - PBE:",
"opcoes":[
"A",
"B",
"C",
"D",
"E"
],
"resposta":1
},

{
"pergunta":"Q23 - Avaliação TEA:",
"opcoes":[
"A",
"B",
"C",
"D",
"E"
],
"resposta":1
},

{
"pergunta":"Q24 - Intervenção focada:",
"opcoes":[
"A",
"B",
"C",
"D",
"E"
],
"resposta":3
},

{
"pergunta":"Q25 - PECS:",
"opcoes":[
"A",
"B",
"C",
"D",
"E"
],
"resposta":4
},

{
"pergunta":"Q26 - Política inclusiva:",
"opcoes":[
"A",
"B",
"C",
"D",
"E"
],
"resposta":1
},

{
"pergunta":"Q27 - AEE surdez:",
"opcoes":[
"A",
"B",
"C",
"D",
"E"
],
"resposta":4
},

{
"pergunta":"Q28 - Associação:",
"opcoes":[
"A",
"B",
"C",
"D",
"E"
],
"resposta":1
},

{
"pergunta":"Q29 - V/F:",
"opcoes":[
"A",
"B",
"C",
"D",
"E"
],
"resposta":0
},

{
"pergunta":"Q30 - PDI:",
"opcoes":[
"A",
"B",
"C",
"D",
"E"
],
"resposta":0
}

]

# =========================
# SISTEMA
# =========================

if "respostas" not in st.session_state:
    st.session_state.respostas = [None]*len(questoes)

st.title("Simulado Concurso AEE")
st.write("Responda as 30 questões:")

for i, q in enumerate(questoes):

    st.subheader(f"Questão {i+1}")

    resposta = st.radio(
        q["pergunta"],
        [f"{chr(65+j)}) {op}" for j,op in enumerate(q["opcoes"])],
        key=i
    )

    if resposta:
        st.session_state.respostas[i] = ord(resposta[0]) - 65

st.divider()

if st.button("Finalizar Prova"):

    acertos = 0
    erros = []

    for i, q in enumerate(questoes):
        if st.session_state.respostas[i] == q["resposta"]:
            acertos += 1
        else:
            erros.append(i+1)

    st.title("Resultado Final")
    st.write(f"Acertos: {acertos}/30")
    st.write(f"Aproveitamento: {(acertos/30)*100:.1f}%")

    if erros:
        st.write("Errou as questões:")
        st.write(erros)
