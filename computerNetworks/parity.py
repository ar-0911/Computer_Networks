def parity_check(count:int, parity_const:int):
    if parity_const == 1 and count % 2 == 0 :
        return False
    elif parity_const == 1 and count % 2 != 0:
        return True
    elif parity_const == 2 and count % 2 != 0:
        return False
    else:
        return True


parity = int(input("Enter 1 for even parity and 2 for odd parity: "))
data = input('Enter data: ')
while len(data) > 8 or len(data) < 8:
    data = input("Enter data of length 8 only: ")

count_1 = data.count('1')
# print(count_1)
error = parity_check(count_1,parity)
if error:
    print("Error detected.")
else:
    print("No error parity matches")

