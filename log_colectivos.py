import requests
import csv
import datetime
import os
import time

# === CONFIGURACIÓN ===
PARADAS = ["7881", "5742"]  # 🔧 Podés agregar más paradas si querés
CARPETA_LOGS = "/root/telegram_colectivos/logs"  # Guardaremos un CSV por semana
INTERVALO_MINUTOS = 5  # Cada cuántos minutos recolectar datos

def obtener_nombre_archivo():
    """Genera nombre de archivo basado en año y número de semana ISO"""
    now = datetime.datetime.now()
    year, week, _ = now.isocalendar()  # _ es el día de la semana (1=lunes)
    nombre_archivo = f"colectivos_log_{year}_semana-{week:02d}.csv"
    return os.path.join(CARPETA_LOGS, nombre_archivo)

def obtener_arribos(parada):
    url = f"https://app.cuandollegarosario.com/api/public/parada/{parada}/arribos?multiparada=true"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("arribos", [])
    except Exception as e:
        print(f"[ERROR] No se pudo consultar parada {parada}: {e}")
        return []

def guardar_en_csv():
    now = datetime.datetime.now()
    filas = []

    for parada in PARADAS:
        arribos = obtener_arribos(parada)
        for item in arribos:
            filas.append({
                "fecha": now.strftime("%Y-%m-%d"),
                "hora": now.strftime("%H:%M:%S"),
                "parada": parada,
                "linea": item.get("descripcionCartelBandera", "???"),
                "identificadorCoche": item.get("identificadorCoche", ""),
                "esAdaptado": item.get("esAdaptado", False),
                "tiempo_min": item.get("tiempoArriboMinutos"),
                "distancia_km": item.get("distanciaKm")
            })

    if not filas:
        print(f"[WARN] No se encontraron datos para las paradas {PARADAS}")
        return

    # Crear carpeta si no existe
    os.makedirs(CARPETA_LOGS, exist_ok=True)

    archivo_log = obtener_nombre_archivo()
    fieldnames = ["fecha", "hora", "parada", "linea", "identificadorCoche", "esAdaptado", "tiempo_min", "distancia_km"]

    with open(archivo_log, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if f.tell() == 0:  # Si el archivo está vacío, escribir cabecera
            writer.writeheader()
        writer.writerows(filas)

    print(f"[OK] {len(filas)} registros guardados en {archivo_log}")

if __name__ == "__main__":
    print(f"📊 Logger de colectivos iniciado. Recolectando cada {INTERVALO_MINUTOS} min.")
    while True:
        guardar_en_csv()
        time.sleep(INTERVALO_MINUTOS * 60)
