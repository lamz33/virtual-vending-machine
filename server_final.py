import socket
import pickle
import csv

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind

server.bind(('localhost', 9998))
server.listen(1)
print("waiting for connection")

socket_client,(host, port) = server.accept()
print(f'Received connection from {host} ({port})\n')
print(f'Connection Established., Connected from: {host}')

#reading csv file
f = open('stock.csv', 'r')
reader = csv.reader(f)


dictionary = {}
#placing csv contents into a dictionary
for row in reader:
    dictionary[row[0]] = {'code':row[0], 'drink':row[1], 'price':float(row[2]), 'quantity':int(row[3])}


while True:
    #sending stock to client
    pickle_obj = pickle.dumps(dictionary)
    socket_client.send(pickle_obj)

    #receiving user order transaction from client
    recv_data2 = socket_client.recv(1024)
    pickle_transaction = pickle.loads(recv_data2)

    with open('user_order.txt', 'w') as f:
        for x in pickle_transaction:
            f.write(str(x))

    #receving updated stock from client
    r_data = socket_client.recv(1024)
    pickle_obj = pickle.loads(r_data)


    new_list = []
    #reading unpicked content as a list
    for i in pickle_obj:
        new_list.append(i)

    #print(new_list)

    #overwriting Stock csv with new updated numbers
    with open('Stock.csv', 'w') as file:
        for i in new_list:
            code = i.get('code')
            drink = i.get('drink')
            price = i.get('price')
            quantity = i.get('quantity')
            file.write(f"{code},{drink},{price},{quantity}\n")


socket_client.close()

