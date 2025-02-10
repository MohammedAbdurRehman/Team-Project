import time
import date

def monitor_log(file_path, keywords):
    """Monitor a log file for specific keywords and alert if found."""
    with open(file_path, "r") as file:
        file.seek(0, 2)  # Move to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  # Wait for new lines
                continue
            for keyword in keywords:
                if keyword in line:
                    print(f"ALERT: '{keyword}' found in log -> {line.strip()}")

if __name__ == "__main__":
    log_file_path = "server.log"  # Replace with your log file
    error_keywords = ["ERROR", "CRITICAL", "FAILURE"]  # Keywords to watch for
    print(f"Monitoring {log_file_path} for {error_keywords}...")
    monitor_log(log_file_path, error_keywords)

