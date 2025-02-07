import psutil

def monitor_cpu_usage():
    try:
        while True:
            curr_usage=psutil.cpu_percent(interval=1)
            threshold=80
            if curr_usage > threshold:
                print("Alert! CPU usage exceeds threshold: ",curr_usage)
    except KeyboardInterrupt:
            print("Session intruppted by the user")
            
        
monitor_cpu_usage()
