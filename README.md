🌐 [Read this in English](README_en.md)

# 🚌 Log Colectivos Rosario

Script en **Python** que consulta periódicamente el estado de llegada de colectivos en Rosario y guarda los datos en archivos **CSV semanales** para su posterior análisis.

---

## 📌 Descripción

Este proyecto realiza:

* Consulta de arribos de colectivos en las paradas definidas.
* Registro de información en un archivo CSV (uno por semana).
* Ejecución continua cada `n` minutos (por defecto, cada 5 min).

Permite construir un **histórico de datos** para analizar:

* Frecuencia de colectivos.
* Tiempos de espera reales.
* Distancias de arribo.
* Patrones de disponibilidad por día y hora.

---

## ⚙️ Configuración

En el script podés ajustar:

```python
PARADAS = ["7881", "5742"]   # IDs de paradas a monitorear
CARPETA_LOGS = "/root/telegram_colectivos/logs"  # Carpeta donde se guardan los CSV
INTERVALO_MINUTOS = 5        # Intervalo entre consultas
```

📌 **Tip:** Podés agregar o quitar IDs de paradas según tus necesidades.
📌 La carpeta de logs se crea automáticamente si no existe.

---

## 📂 Estructura de archivos

Cada archivo CSV se nombra usando el año y el número de semana ISO:

```
colectivos_log_2025_semana-39.csv
```

### Ejemplo de registro:

| fecha      | hora     | parada | linea | identificadorCoche | esAdaptado | tiempo_min | distancia_km |
| ---------- | -------- | ------ | ----- | ------------------ | ---------- | ---------- | ------------ |
| 2025-09-26 | 10:15:00 | 7881   | 115N  | 5678               | False      | 3          | 0.8          |

---

## ▶️ Ejecución

1. Cloná el repositorio:

```bash
git clone git@github.com:ernes2111/log-colectivos-rosario.git
cd log-colectivos-rosario
```

2. Instalá dependencias (requiere Python 3.x):

```bash
pip install requests
```

3. Ejecutá el script:

```bash
python3 logger_colectivos.py
```

El script quedará corriendo indefinidamente y guardará los datos cada `INTERVALO_MINUTOS`.

---

## 🛠 Posible automatización

Podés correr el script en segundo plano o configurar un **servicio del sistema** (ej. `systemd`) para que se ejecute automáticamente al iniciar tu servidor/Raspberry Pi.

---

## 📊 Próximos pasos

* Crear notebooks de análisis en **Jupyter**.
* Generar gráficos de frecuencias y tiempos de espera.
* Publicar dashboards en Power BI o Grafana.

🌐 [Read this in English](README_en.md)
