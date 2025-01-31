import numpy as np
import socket
import time


low_freq = 1        
high_freq = 100     
sampling_rate = 200  
duration = 2        

np.set_printoptions(threshold=200)

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

low_freq_signal = np.sin(2 * np.pi * low_freq * t)  
high_freq_signal = np.sin(2 * np.pi * high_freq * t)  


low_freq_signal_uint8 = np.uint8(127 * (low_freq_signal + 1))   
high_freq_signal_uint8 = np.uint8(127 * (high_freq_signal + 1))  

udp_ip = "192.168.1.101"  
udp_port = 25000  

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    sock.sendto(low_freq_signal_uint8.tobytes(), (udp_ip, udp_port))
    print(low_freq_signal_uint8)
    print("Sending Low-Frequency Signal")
    time.sleep(10)
    sock.sendto(high_freq_signal_uint8.tobytes(), (udp_ip, udp_port))
    print(high_freq_signal_uint8)
    print("Sending High-Frequency Signal")
    time.sleep(10)


