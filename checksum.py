data = input("Enter data(8 bit or 8 bit multiples only) split with commas: ")
# d_list = [data[i:i+8] for i in range(0, len(data), 8)]
d_list = data.split(',')
#print(d_list)
#1011101110
#11111000
checksum = '0'
for item in d_list:
    checksum = bin(int(checksum, 2) + int(item, 2))
print("checksum without wrapping: " + checksum[2:])
print(checksum)
checksum_length = len(str(checksum))
print(len(checksum))
if checksum_length > 10:
    bit_8len = 2+checksum_length-10
    print(bit_8len)
    checksum = bin(int(str(checksum[bit_8len:]), 2) + int(str(checksum[2:bit_8len]), 2))
print('Checksum with wrapping: ' + checksum[2:])
checksum_list = [str(checksum[i]) for i in range(2, len(checksum))]

##adding leading 0's if checksum is not 8 bit
if len(checksum_list) < 8:
    for i in range(8-len(checksum_list)):
        checksum_list = [0] + checksum_list
checksum = ''.join(str(i) for i in checksum_list)
integer_value = int(checksum,2)
print("8 bit checksum: "+ checksum)

##complement of checksum
checksum_1_complement_list = ['0' if i == '1' else '1' for i in checksum_list]
checksum_1_complement = ''.join(str(i) for i in checksum_1_complement_list)
print("1's complement of checksum: "+checksum_1_complement)

#user side
data_from_user = input("Enter data received by user (split data unit with comma): ")
received_d_list = data_from_user.split(',')
received_d_list.append(checksum_1_complement)
sum = '0'
for item in received_d_list:
    sum = bin(int(sum, 2) + int(item, 2))
sum_length = len(str(sum))
if sum_length > 10:
    bit_8len = 2+sum_length-10
    sum = bin(int(str(sum[bit_8len:]), 2) + int(str(sum[2:bit_8len]), 2))
print("8 bit value after adding each data unit and checksum(wrapped): "+sum[2:]+'\n')

##complementing sum
sum_cpl = ''.join(['0' if i == '1' else '1' for i in str(sum)])
print("complemented: "+sum_cpl[2:]+'\n')

##error checking
error = False
for i in str(sum_cpl[2:]):
    if i == '1':
        error = True
        break

if(error):
    print("Checksum Error")
else:
    print("No Error")