import socket
import json
import time

other_switch_id_list = ("0000000000000002","0000000000000003")

sockets = {}

print(other_switch_id_list)

for switch_id in other_switch_id_list:
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    switch_index = switch_id[15]
    print(socket_client.bind(("127.0.0.1", 10000+int(switch_index))))
    sockets[switch_index] = socket_client

print(sockets)
    

