def xor(a, b):
    # initialize result
    result = []

    # Traverse all bits, if bits are
    # same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def mod2div(dividend, divisor):
    # Number of bits to be XORed at a time.
    pick = len(divisor)
    tmp = dividend[0: pick]

    while pick < len(dividend):

        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]

        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]

        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


def encodedata(data, key):
    l_key = len(key)

    # Appends n-1 zeroes at end of data
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)

    # Append remainder in the original data
    # codeword = data + remainder
    print("CRC : ", remainder)
    # print("Encoded Data (Data + Remainder) : ", codeword)
    return remainder


sent_data = str(input("Enter data to be sent: "))
key = str(input("Enter key: "))
remainder = encodedata(sent_data, key)
received_data = str(input("Enter data received: "))

# appending remainder to received data
received_data += remainder
print("Recieved date along with crc: "+received_data)
final_remainder = mod2div(received_data, key)
if int(final_remainder) == 0:
    print("No error detected")
else:
    print("Error detected")
