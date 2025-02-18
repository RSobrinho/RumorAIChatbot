
## Chatbot RumorAIChatbot

Este projeto implementa um chatbot utilizando a plataforma Rasa para facilitar a detecção e comunicação de rumores . O chatbot permite que usuários reportem informações que podem ser cruciais para a saúde pública, auxiliando na rápida identificação e resposta a eventos de saúde.

## Terminologias Comuns

-   **Intenção**: Representa a intenção do usuário. Ex:  `SaudarProHub`,  `para_que_serve`,  `Rumor`.
-   **Entidade**: Dados específicos extraídos da entrada do usuário. Ex:  `tipo_afetado`,  `descricao`.
-   **Ação**: Tarefas que o bot executa, que podem ser ações padrão ou personalizadas.
-   **Slot**: Armazena informações extraídas durante a conversa.
-   **NLU**: Natural Language Understanding, responsável por compreender a entrada do usuário.
-   **História**: Exemplos de conversas que o bot pode ter com um usuário.
-   **Regra**: Define regras específicas para o comportamento do bot.
-   **Domínio**: Define a estrutura do bot, incluindo intents, entities, slots, actions e respostas.
-   **actions_auxiliares**: Ações auxiliares que suportam funcionalidades adicionais do bot.
-   **actions_formulario_principal**: Principais ações relacionadas ao formulário de boato.

## Requisitos

1.  **Python 3.8 ou superior**

## Executando o pipenv

Com o python 3.8.10 instalado, e na raiz do projeto, execute:

```
pip install pipenv
```

```
pipenv shell
```

```
pipenv install
```

## Executando o Rasa

Primeiramente, entre na pasta rasa e execute:

```
cd rasa_chatbot
```

Para treinar um novo modelo no rasa, execute:
```
rasa train
```

Para executar o modelo rasa existente, execute:
```
rasa shell
```

## Executando o Servidor de Ações do Rasa

Em outro terminal, você pode executar o servidor de ações para validar seu chatbot. Então, na pasta rasa_chatbot, execute:

```
rasa run actions
```

## Considerações

-   **Ativação de Tempo Limite:** O tempo limite só será ativado quando o formulário for iniciado, pois está configurado dentro das regras.
-   **Estrutura de Diretório:** Os diretórios são estruturados para separar actions_auxiliares e actions_formulario_principal. Dentro de actions_auxiliares, existem ações relacionadas ao suporte do início e do fim do formulário. O actions_formulario_principal contém as principais ações relacionadas ao formulário. Essa estrutura facilita a validação das ações e mantém as ações personalizadas organizadas dentro da mesma pasta.
-   **Palavra-chave ON:** A palavra-chave ON é usada como prefixo (representando "on" em português) para ajudar a ordenar os arquivos na IDE e seguir um fluxo simplificado e simples, melhorando a qualidade interna do código.
-   **Separação de Arquivos de Configuração:** Regras, dados NLU e histórias são colocados em arquivos .yml separados e organizados em suas respectivas pastas (nlu, rules, stories). Isso mantém a configuração organizada e mais fácil de gerenciar.

## Links Úteis

-   [Documentação do Rasa](https://rasa.com/docs/rasa/)
-   [Documentação do Heyoo](https://github.com/Neurotech-HQ/heyoo)

Você pode configurar a URL do servidor em endpoints.yml

## EXEMPLO DE REQUISIÇÃO HTTP POST

```
curl --request POST   --url http://localhost:5005/webhooks/whatsapp/webhook   --header 'Content-Type: application/json'   --data '{"object":"whatsapp_business_account","entry":[{"id":"261206653746280","changes":[{"value":{"messaging_product":"whatsapp","metadata":{"display_phone_number":"any","phone_number_id":"anyId"},"contacts":[{"profile":{"name":"AnyName \u2708\ufe0f"},"wa_id":"5567991987012"}],"messages":[{"from":"5567991987012","id":"wamid.abced","timestamp":"1712801
```
