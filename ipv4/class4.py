def binary(data):
    ip_array, mask_value = data.split('/')
    ip_array = ip_array.split('.')
    ip = []
    for row in ip_array:
        value = str(bin(int(row))[2:])
        while len(value) != 8:
            value = '0' + value
        ip.append(value)
    mask = make_network_mask(int(mask_value))
    return (ip, mask)

def make_network_mask(number):
    mask = []
    aux = ['11111111']*(number//8)
    mask.extend(aux)
    aux = '1'*int(number%8)
    while len(aux) != 8:
        aux = aux + '0'
    mask.append(aux)
    while len(mask) < 4:
        mask.append('00000000')
    return mask

def reverse_mask(mask):
    rev_mask = []
    for i in range(len(mask)):
        aux = ''
        for j in range(len(mask[i])):
            if int(mask[i][j]):
                aux = aux + '0'
            else:
                aux = aux + '1'
        rev_mask.append(aux)
    return rev_mask

def check_class(binary):
    value = int(binary[0], 2)
    if value <= 127:
        return 'A', 8
    if value <= 191:
        return 'B', 16
    if value <= 223:
        return 'C', 24
    if value <= 239:
        return 'D', 28
    if value <= 255:
        return 'E', 30

def check_network(ip, mask):
    result = []
    for i in range(len(ip)):
        aux = ''
        for j in range(len(ip[i])):
            if int(ip[i][j]) and int(mask[i][j]):
                aux = aux + '1'
            else:
                aux = aux + '0'
        result.append(aux)
                
    return result

def broadcast(network, mask):
    mask_host = reverse_mask(mask)
    broadcast = []
    for i in range(len(network)):
        aux = ''
        for j in range(len(network[i])):
            if int(network[i][j]) or int(mask_host[i][j]):
                aux = aux + '1'
            else:
                aux = aux + '0'
        broadcast.append(aux)
    return broadcast

def check(network, mask):
    index_h, index_s = search(mask)
    rev_mask = reverse_mask(mask)
    num_hosts = 255 ** (4 - index_h)
    gap = int(rev_mask[index_h] , 2)

    return 2**index_s, gap,  num_hosts

def search(mask):
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if not int(mask[i][j]):
                index_h = i
                index_s = j
                return index_h, index_s

def to_string(array):
    result = ''
    for row in array:
        result = result + str(int(row, 2)) + '.'
    return result[:-1]

ip = '192.168.0.1/23' 

ip_binary, mask_binary = binary(ip)
clas = check_class(ip_binary)
default_mask = make_network_mask(clas[1])
network = check_network(ip_binary, mask_binary)
broad = broadcast(network, default_mask)
num_gap, len_gap, hosts = check(ip_binary, mask_binary)
print('IP BINARY: ', ip_binary, '\nMASK BINARY: ', mask_binary)
print('IP DECIMAL: ', to_string(ip_binary))
print('MASK DECIMAL: ', to_string(mask_binary))
print('CLASS: ', clas[0])
print('NETWORK DEFAULT: ', to_string(network))
print('BROADCAST DEFAULT: ', to_string(broad))
print('GAP QUANTITY: ', num_gap, '/ GAP LENGTH: ', len_gap, '/ HOSTS QUANTIY: ', hosts)