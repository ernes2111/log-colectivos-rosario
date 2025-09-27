🌐 [Leer en Español](README.md)

# 🚌 Rosario Bus Log

Python **script** that periodically queries bus arrival times in Rosario and saves the data into **weekly CSV files** for further analysis.

---

## 📌 Description

The idea arose from the need to quickly and easily check arrival times on iOS devices, since the current app available on the Store lacks several features compared to the Android version. 
This script was later implemented to build a solid database for analysis and ultimately reach a conclusion about the quality of public transportation service in Rosario, Santa Fe, Argentina.

This project performs:

* Fetching real-time bus arrival data for the defined stops.
* Logging the data into a CSV file (one per week).
* Continuous execution every `n` minutes (default: every 5 min).

It allows you to build a **historical dataset** to analyze:

* Bus frequency.
* Actual waiting times.
* Arrival distances.
* Availability patterns by day and hour.

---

## ⚙️ Configuration

You can adjust these settings in the script:

```python
PARADAS = ["7881", "5742"]   # Stop IDs to monitor
CARPETA_LOGS = "/root/telegram_colectivos/logs"  # Folder where CSV files will be stored
INTERVALO_MINUTOS = 5        # Time interval between queries
```

📌 You can add or remove stop IDs as needed.
📌 The logs folder will be created automatically if it does not exist.

---

## 📂 File Structure

Each CSV file is named using the ISO year and week number:

```
colectivos_log_2025_week-39.csv
```

### Example record:

| date       | time     | stop | route | busID | accessible | eta_min | distance_km |
| ---------- | -------- | ---- | ----- | ----- | ---------- | ------- | ----------- |
| 2025-09-26 | 10:15:00 | 7881 | 115N  | 5678  | False      | 3       | 0.8         |

---

## ▶️ Usage

1. Clone the repository:

```bash
git clone git@github.com:ernes2111/log-colectivos-rosario.git
cd log-colectivos-rosario
```

2. Install dependencies (requires Python 3.x):

```bash
pip install requests
```

3. Run the script:

```bash
python3 logger_colectivos.py
```

The script will run indefinitely and log data every `INTERVALO_MINUTOS`.

---

## 🛠 Automation

You can run the script in the background or configure a **system service** (e.g., `systemd`) to start it automatically on boot (ideal for servers or Raspberry Pi setups).

---

## 📊 Next Steps

* Create analysis notebooks using **Jupyter**. ⏳ Status: Done ✓
* Generate frequency and waiting time visualizations. ⏳ Status: Done ✓
* Publish dashboards using Power BI or Grafana. ⏳ Status: In progress...

🌐 [Leer en Español](README.md)
