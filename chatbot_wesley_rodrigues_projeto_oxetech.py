# chatbot_wesley_rodrigues_projeto_oxetech.py

import difflib
from gtts import gTTS
import os
import tkinter as tk
from tkinter import scrolledtext

# Dicionário de FAQ

faq = {
    "horário": "Nosso horário de funcionamento é de segunda a sexta, das 9h às 18h (horário de Brasília). Fora desse horário, você pode nos enviar mensagens que responderemos assim que possível.",
    "endereço": "Atendemos clientes em todo o Brasil e exterior. Todo o atendimento e entrega de soluções são realizados online, garantindo rapidez e segurança.",
    "telefone": "Nosso telefone de contato é (82) 98872-3078. Também atendemos via WhatsApp e e-mail para suporte e dúvidas.",
    "pagamento": "Aceitamos cartões de crédito, débito, PIX e boleto bancário. Para empresas, também podemos emitir nota fiscal.",
    "entrega": "Os projetos e soluções são entregues 100% online. Dependendo da complexidade, o prazo médio varia de 7 a 30 dias úteis.",
    "serviços": (
        "Oferecemos soluções de automação empresarial, agentes de IA personalizados, integração com ERP, "
        "dashboards inteligentes, relatórios automatizados e otimização de processos de vendas e operações. "
        "Exemplos de uso incluem: atendimento automatizado no WhatsApp, geração de relatórios financeiros, "
        "controle de estoque e análise de performance de vendas."
    ),
    "suporte": "Disponibilizamos suporte técnico via chat, e-mail ou reuniões online. Se surgir qualquer problema, nossa equipe te ajuda a resolver rapidamente.",
    "personalizacao": "Nossos agentes de IA podem ser totalmente personalizados de acordo com as necessidades do seu negócio. Podemos criar fluxos específicos e funcionalidades exclusivas.",
    "treinamento": "Oferecemos treinamento completo para a equipe do cliente, garantindo que todos saibam usar a solução de forma eficiente e sem dificuldades técnicas.",
    "seguranca": "Todos os dados dos clientes são tratados com total confidencialidade e segurança, seguindo as melhores práticas de proteção de dados.",
    "prazo_projeto": "O prazo de entrega depende da complexidade do projeto. Projetos simples podem ser entregues em 7 dias úteis, enquanto soluções completas podem levar até 30 dias úteis.",
    "demonstracao": "Você pode solicitar uma demonstração gratuita das nossas soluções antes de contratar. Assim você conhece exatamente como funciona o agente de IA para o seu negócio.",
    "contrato": "Todos os serviços são formalizados via contrato, garantindo segurança jurídica para ambas as partes.",
    "cancelamento": "O cancelamento do serviço segue cláusulas contratuais. Nossa equipe ajuda no processo para garantir uma transição tranquila, caso necessário.",
    "integração_erp": "Nosso agente de IA pode se integrar ao seu ERP para automatizar vendas, estoque, faturamento e relatórios. Exemplo: seu cliente faz um pedido no WhatsApp e o ERP atualiza automaticamente o estoque.",
    "relatorios": "Você pode gerar relatórios financeiros, de vendas, estoque e performance de forma automática. Os relatórios podem ser enviados por e-mail ou visualizados em dashboards online.",
    "facilidade_uso": "Não é necessário conhecimento técnico para usar nossos agentes de IA. Eles são intuitivos e a equipe fornece treinamento completo.",
    "expansao": "Após a entrega, é possível alterar, expandir ou adicionar novas funcionalidades ao agente de IA, conforme o crescimento do seu negócio.",
    "teste_gratuito": "Oferecemos testes ou pilotos do serviço em alguns casos. Entre em contato para verificarmos a disponibilidade para sua empresa.",
    "faq": "Se você não encontrou sua pergunta aqui, pode nos contatar diretamente pelo WhatsApp ou e-mail. Estamos sempre prontos para ajudar!"
}

# Função de busca inteligente corrigida

def buscar_resposta(pergunta):
    pergunta = pergunta.lower()
    chaves = list(faq.keys())
    
    # Busca exata por palavra-chave

    for chave in chaves:
        if chave in pergunta:
            return faq[chave]
    
    # Busca por similaridade (fallback)

    chave_proxima = difflib.get_close_matches(pergunta, chaves, n=1, cutoff=0.5)
    if chave_proxima:
        return faq[chave_proxima[0]]
    
    return "Desculpe, não encontrei uma resposta para sua pergunta. Você pode nos contatar pelo WhatsApp ou e-mail."

# Função para falar a resposta

def falar_resposta(texto):
    tts = gTTS(text=texto, lang='pt-br')
    arquivo_audio = "resposta.mp3"
    tts.save(arquivo_audio)
    os.system(f"start {arquivo_audio}")  # Windows
    # Mac: os.system(f"afplay {arquivo_audio}")
    # Linux: os.system(f"mpg123 {arquivo_audio}")

# Função para salvar histórico

def salvar_historico(pergunta, resposta):
    with open("historico_chat.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Você: {pergunta}\n")
        arquivo.write(f"Chatbot: {resposta}\n")
        arquivo.write("-" * 40 + "\n")

# Função da interface gráfica

def iniciar_chat_gui():
    def enviar_mensagem():
        pergunta = caixa_pergunta.get()
        if pergunta.strip() == "":
            return
        chat_texto.config(state='normal')
        chat_texto.insert(tk.END, f"Você: {pergunta}\n")
        
        resposta = buscar_resposta(pergunta)
        chat_texto.insert(tk.END, f"Chatbot: {resposta}\n\n")
        chat_texto.config(state='disabled')
        chat_texto.yview(tk.END)
        
        falar_resposta(resposta)
        salvar_historico(pergunta, resposta)
        
        caixa_pergunta.delete(0, tk.END)

    # Criar janela principal

    janela = tk.Tk()
    janela.title("Chatbot FAQ")
    janela.geometry("500x500")

    # Área de texto para o chat

    chat_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, state='disabled')
    chat_texto.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Caixa de entrada da pergunta

    caixa_pergunta = tk.Entry(janela, width=50)
    caixa_pergunta.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.X, expand=True)

    # Botão de enviar

    botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem)
    botao_enviar.pack(padx=10, pady=5, side=tk.RIGHT)

    janela.mainloop()

# Inicia o chatbot

if __name__ == "__main__":
    iniciar_chat_gui()
