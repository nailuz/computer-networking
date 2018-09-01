def binary(data):
    ip_array, mask_value = data.split('/')
    ip_array = ip_array.split('.')
    ip = []
    for row in ip_array:
        value = str(bin(int(row))[2:])
        while len(value) != 8:
            value = '0' + value
        ip.append(value)
    mask = []
    aux = ['11111111']*int(int(mask_value)/8)
    mask.extend(aux)
    aux = '1' * int(int(mask_value)%8)
    while len(aux) != 8:
        aux = aux + '0'
    mask.append(aux)
    while len(mask) < 4:
        mask.append('00000000')
    return (ip, mask)

def check_class(binary):
    value = int(binary[0], 2)
    if value <= 127:
        return 'CLASS A'
    if value <= 191:
        return 'CLASS B'
    if value <= 223:
        return 'CLASS C'
    if value <= 239:
        return 'CLASS D'
    if value <= 255:
        return 'CLASS E'

def check_network(ip, mask):
    result = []
    for i in range(len(ip)):
        aux = ''
        for j in range(len(ip[i])):
            if int(ip[i][j]) or int(mask[i][j]):
                if not int(mask[i][j]):
                    aux = aux + '0'
                else:
                    aux = aux + ip[i][j]
            else:
                aux = aux + '0'
        result.append(aux)
                
    return result

def to_string(array):
    result = ''
    for row in array:
        result = result + str(int(row, 2)) + '.'
    return print(result[:-1])

ip = '192.168.0.1/24' 

ip_binary, mask_binary = binary(ip)
print(ip_binary, mask_binary)
to_string(mask_binary)
to_string(ip_binary)
print(check_class(ip_binary))
network = check_network(ip_binary, mask_binary)
to_string(network)