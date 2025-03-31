#!/usr/bin/python3

import socket
import time

def send_udp_data(data, target_ip, target_port, timeout=5, expect_response=True):
    """Sends UDP data and listens for a response on the same port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        sock.bind(("", target_port))  # Bind to the target port
        sock.sendto(data.encode(), (target_ip, target_port))
        print(f"Sent: {data} to {target_ip}:{target_port}")

        sock.settimeout(timeout)  # Set timeout for receiving

        if expect_response is True:
            print("Waiting for response")
            try:
                response, addr = sock.recvfrom(1024)  # Receive up to 1024 bytes
                print(f"Received response from {addr}: {response.decode()}")
            except socket.timeout:
                print("Timeout waiting for response.")
            except Exception as e:
                print(f"Error receiving response: {e}")
        else:
            print("Not waiting for response")
        sock.close()

    except Exception as e:
        print(f"Error sending/receiving UDP data: {e}")

if __name__ == "__main__":
    target_ip = "10.10.100.254"  # Replace with the target IP address
    target_port = 48899
    message = "HF-A11ASSISTHREAD"  # Replace with the data you want to send

    send_udp_data(message, target_ip, target_port, 48899)
    time.sleep(1)
    print("Sleeping")
    send_udp_data("+ok", target_ip, target_port, 48899, False)
    time.sleep(1)
    send_udp_data("AT+WSSSID=wifi_ssid_goes_here\r", target_ip, target_port, 48899)
    send_udp_data("AT+WSKEY=WPA2PSK,AES,super_secret_password_goes_here\r", target_ip, target_port, 48899)
    send_udp_data("AT+WMODE=STA\r”", target_ip, target_port, 48899)
    send_udp_data("AT+Z\r", target_ip, target_port, 48899, False)
