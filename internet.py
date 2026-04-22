import socket
import speedtest
import time
import emoji

print(emoji.emojize("Iniciando teste :globe_with_meridians:...\n", language="alias"))
time.sleep(2)

# ---------------- SPEEDTEST ----------------
try:
    print(emoji.emojize("Escolhendo o melhor servidor :satellite_antenna:\n", language="alias"))
    st = speedtest.Speedtest()
    st.get_best_server()

    print("Testando o ping...\n")
    ping = st.results.ping

    print("Testando download...\n")
    download = st.download()

    print("Testando upload...\n")
    upload = st.upload()

    download_mbps = download / 1_000_000
    upload_mbps = upload / 1_000_000

    print("\n******** RESULTADO SPEEDTEST ********\n")
    print(f"Ping: {ping:.2f} ms")
    print(f"Download: {download_mbps:.2f} Mbps")
    print(f"Upload: {upload_mbps:.2f} Mbps")

except Exception as e:
    print("\n⚠ Erro no Speedtest:", e)
    print("Pulando teste de velocidade...")

# ---------------- SOCKET ----------------

print(emoji.emojize("\n🌐 Testando conexão via socket...\n", language="alias"))

try:
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tempo_inicial = time.time()
    sc.connect(('www.google.com', 80))
    tempo_final = time.time()

    ping_socket = (tempo_final - tempo_inicial) * 1000

    print("Conexão bem sucedida ✅")
    print(f"Ping (socket): {ping_socket:.2f} ms")

    sc.close()

except Exception as e:
    print("❌ Erro na conexão socket:", e)

print("\nPrograma finalizado.")
