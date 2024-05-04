import socket
import pandas as pd
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S") 

data1 = {
  "time": [],
  "depth": []
  }


serverAddress = ('192.168.1.142', 2222)
bufferSize = 1600000 
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with open('receiveFile.txt','w') as f:
    f.write('')
while True:
    cmd=input('data start or fat or final data?'+'\n')
    cmd=cmd.encode('utf-8')
    UDPClient.sendto(cmd, serverAddress)
    margin_output=input("Enter a margin of error: ")
    margin_output=margin_output.encode('utf-8') 
    UDPClient.sendto(margin_output, serverAddress)
    data,address=UDPClient.recvfrom(bufferSize)
    data=data.decode('utf-8')
    with open('receiveFile.txt','w') as f:
        f.write(data)
        
    f=open('receiveFile.txt','r')
    content = f.read()
    print(content)
    print(current_time)
    data1['depth'].append(content)
    data1['time'].append(current_time)
    df = pd.DataFrame(data1)
    df.to_csv('receiveFile.csv', index=False)
    f.close()
