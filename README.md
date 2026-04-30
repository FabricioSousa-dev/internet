### 🇺🇸 English Version: `README.md`

# Network Performance & Connectivity Tool 🌐

A Python-based utility to measure internet health, including bandwidth (download/upload) and connection latency using both high-level APIs and low-level TCP sockets.

## ⚙️ How it Works

The script is divided into two main diagnostic modules:

1.  **Speedtest Module (`speedtest-cli`):**
    *   Identifies the nearest and fastest server based on your location.
    *   Measures **Ping** (latency), **Download**, and **Upload** speeds.
    *   Converts raw bit data into **Mbps** for better readability.
2.  **Socket Connectivity Module (`socket`):**
    *   Performs a low-level **TCP Handshake** with `google.com` on port 80.
    *   Calculates the precise time taken to establish a connection, providing a real-world "ping" from a protocol perspective.

## 🚀 Installation & Usage

### Prerequisites
*   Python 3.x
*   Pip (Python package manager)

### Setup
1.  Clone this repository:
    ```bash
    git clone https://github.com/FabricioSousa-dev/internet.git
    cd internet
    ```
2.  Install the required dependencies:
    ```bash
    pip install speedtest-cli emoji
    
```

### Running the tool
Simply execute the script:
```bash
python internet_test.py
```

## 🛠️ Built With
*   **[Socket](https://docs.python.org/3/library/socket.html):** For low-level network interface testing.
*   **[Speedtest-cli](https://pypi.org/project/speedtest-cli/):** To interact with Speedtest.net infrastructure.
*   **[Emoji](https://pypi.org/project/emoji/):** For a more user-friendly terminal output.

---

### 🇧🇷 Versão em Português: `README.pt-br.md`

# Ferramenta de Performance e Conectividade de Rede 🌐

Um utilitário em Python para medir a saúde da sua conexão, incluindo largura de banda (download/upload) e latência, utilizando tanto APIs de alto nível quanto sockets TCP de baixo nível.

## ⚙️ Como Funciona

O script é dividido em dois módulos principais de diagnóstico:

1.  **Módulo Speedtest (`speedtest-cli`):**
    *   Identifica o servidor mais próximo e rápido baseado na sua localização.
    *   Mede **Ping** (latência), velocidade de **Download** e **Upload**.
    *   Converte os dados brutos (bits) para **Mbps** para facilitar a leitura.
2.  **Módulo de Conectividade Socket (`socket`):**
    *   Realiza um **Handshake TCP** de baixo nível com o endereço `google.com` na porta 80.
    *   Calcula o tempo exato para estabelecer a conexão, fornecendo um "ping" real sob a perspectiva do protocolo de transporte.

## 🚀 Instalação e Uso

### Pré-requisitos
*   Python 3.x
*   Pip (Gerenciador de pacotes do Python)

### Configuração
1.  Clone o repositório:
    ```bash
    git clone https://github.com/FabricioSousa-dev/internet.git
    cd internet
    ```
2.  Instale as dependências necessárias:
    ```bash
    pip install speedtest-cli emoji
    ```

### Executando a ferramenta
Basta executar o script:
```bash
python internet_test.py
```

## 🛠️ Tecnologias Utilizadas
*   **Socket:** Para testes de interface de rede de baixo nível.
*   **Speedtest-cli:** Para interação com a infraestrutura do Speedtest.net.
*   **Emoji:** Para uma saída de terminal mais amigável e visual.


O código está muito bem estruturado e o uso de Sockets para validar a conexão é uma prática excelente para quem estuda sistemas de informação! O que achou dessas sugestões?
```
