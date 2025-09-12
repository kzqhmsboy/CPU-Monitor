import psutil
import time

THRESHOLD = 80  # CPU usage percentage
CHECK_INTERVAL = 2  # seconds

def monitor_cpu():
    print(f"Monitoring CPU usage... (Warning if above {THRESHOLD}%)")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU Usage: {cpu_usage}%")
            if cpu_usage > THRESHOLD:
                print("WARNING: CPU usage exceeded threshold!")
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_cpu()
