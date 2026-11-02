import socket
import time

base_ip = '192.168.45.'
rtsp_port = 9000
camera_path = '#cam1'

def create_rtsp_url(ip):
    return f"rtsp://{ip}:{rtsp_port}/{camera_path}"

def check_rtsp_connection(ip):
    rtsp_url = create_rtsp_url(ip)
    start_time = time.time()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, rtsp_port))
            end_time = time.time()
            duration = (end_time - start_time) * 1000
            print(f"Connected to {rtsp_url}..........({duration:.2f}ms)")
    except (socket.timeout, socket.error):
        print(f"Failed to connect to {rtsp_url}")
        
for i in range(1, 255):
    ip = f"{base_ip}{i}"
    check_rtsp_connection(ip)