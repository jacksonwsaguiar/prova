# PROVA

## Instruções de Instalação e Execução

1. Clone o repositório:
    ```bash
    git clone https://github.com/jacksonwsaguiar/prova
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd prova
    ```

3. Instale as dependências:
    ```bash
    pip install gtts speech_recognition pyttsx3
    ```
    
## Executando o projeto

Para executar, use o seguinte comando:
    ```bash
    python3 app.py 
    ```
## Explicação
Este script em Python realiza a sintetização de fala a partir de uma frase.

1. Ao executar a apliação o terminal solicita que o usuario digite uma frase.
2. o texto é entao carregado e processado pelo gtts.
3. Em seguida é reproduzido pelo pyttsx3.
4. O processo se repete até o usuario digitar "sair".
