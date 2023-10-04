import socket
import threading
import pickle
import json
import ServoCmd 
from queue import Queue

def socket_thread(queue_data):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 8000)
    server_socket.bind(server_address)

    server_socket.listen(1)

    print("socket start")
    watch_socket, watch_address = server_socket.accept()
    while True:
        try:
            data_json = watch_socket.recv(8192).decode('utf-8')
            data = json.loads(data_json)
            # print(data)
            print(f"socket:   linear_x: {-data['yAxis']}, angular_z: {data['zAxis']}")
            queue_data.put(data)
            
        except json.decoder.JSONDecodeError:
            pass
        except socket.error:
            server_socket.close()

# def handle_watch_message(watch_socket):
#     while True:
#         try:
#             data_json = watch_socket.recv(8192).decode('utf-8')
#             data = json.loads(data_json[:data_json.index('}') + 1])
#             print(f"linear_x: {data['xAxis']}, angular_z: {data['rzAxis']}")
            
#         except json.decoder.JSONDecodeError:
#             pass

def control_thread(queue_data):
    while True:
        # print("1")
        if queue_data != None:
            cmd_vel = queue_data.get()
            queue_data.queue.clear()
        if cmd_vel != None and cmd_vel != {'xAxis': 0.0, 'yAxis': 0.0, 'zAxis': 0.0, 'rzAxis': 0.0}:
            
            if cmd_vel['yAxis'] == -0.0:
                print(f"ctrl :     {cmd_vel}")
                ServoCmd.move_joystick(linear_x=-cmd_vel['yAxis'], angular_z=-cmd_vel['zAxis'])
            else:
                
                ServoCmd.move_joystick(linear_x=-cmd_vel['yAxis'], angular_z=-cmd_vel['zAxis']*0.5)


if __name__ == "__main__":
    q = Queue()
    threads = []
    threads.append(threading.Thread(target = control_thread, args = (q,)))
    threads.append(threading.Thread(target = socket_thread, args = (q,)))
    threads[0].start()
    threads[1].start()