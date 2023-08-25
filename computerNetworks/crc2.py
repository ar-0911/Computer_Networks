def xor(a,b):
    result = []

    for i in range(1,len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


def mod2div(dividend,divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor,tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick,tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor,tmp)
    else:
        tmp = xor('0' * pick,tmp)
    checkword = tmp
    return checkword

def encode(data,key):
    k_length = len(key)

    appended_data = data + '0'*(k_length-1)
    crc = mod2div(appended_data,key)
    print("Appended with n-1 zeroes: "+appended_data)
    return crc

data = input("Enter data: ")
key = input("Enter divisor: ")
CRC = encode(data,key)
print("CRC : "+CRC)
input_data = input("Enter recieved data: ")
## appending crc
appendedInputData = input_data+CRC
print("Appended received data = "+appendedInputData)
remainder = mod2div(appendedInputData,key)
if int(remainder) == 0:
    print("Remaninder = "+remainder+"\nno error")
else:
    print("Error\n remainder ="+ remainder)