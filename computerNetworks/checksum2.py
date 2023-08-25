data = input("Enter data split by commas: ")
data_list = data.split(',')
checksum = '0'
#10001000,10101010,11110000,11001100          11110000
for item in data_list:
    checksum = bin(int(checksum,2) + int(item,2))
    checksum = str(checksum[2:])

print(checksum)

if len(checksum) > 8:
    extra_len = len(checksum) - 8
    print(extra_len)
    checksum = bin(int(checksum[extra_len:], 2) + int(checksum[:extra_len],2))

print(checksum)
if len(checksum)< 8:
    for i in range(8-len(checksum)):
        checksum = '0' + checksum
print(checksum)
##complementing checksum

checksum_list = list(checksum)
checksum_cpl_list = ['1' if i =='0' else '0' for i in checksum_list]
checksum_cpl = ''.join(checksum_cpl_list)

print(checksum_cpl[2:])

user_data = input("Enter data received by user split by commas: ")
user_dl = user_data.split(',')
user_dl.append(checksum_cpl[2:])

sum = '0'
for item in user_dl:
    sum = bin(int(sum,2)+int(item,2))
    sum = str(sum[2:])
print(sum)
## wrapping sum
if len(sum) > 8:
    extra_sum_len = len(sum) - 8
    sum = bin(int(sum[extra_sum_len:],2) + int(sum[:extra_sum_len],2))
    sum = str(sum[2:])

# complementing sum
sum_list = list(sum)
sum_cpl_list = ['1' if i == '0' else '0' for i in sum_list]
sum_cpl = ''.join(sum_cpl_list)
print(sum_cpl)
error = False
for i in sum_cpl:
    if i == '1':
        error = True
        break

if error:
    print("Error found sum value not 0 after calculation\nSum: "+sum_cpl)
else:
    print("No error\nsum: "+sum_cpl)