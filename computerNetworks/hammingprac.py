def calcRedundantBit(m):
    for i in range(m):
        if 2**i >= m+i+1:
            return i

def postRedundantBits(data,r):
    m=len(data)
    j=0
    k=1
    res=''
    for i in range(1,m+r+1):
        if i==2**j:
            res=res+'0'
            j+=1
        else:
            res += data[-1*k]
            k+=1
    return res[::-1]

def calcParityBit(data,r):
    m=len(data)
    for i in range(r):
        val=0
        for j in range(1,m+1):
            if j & (2**i) == 2**i:
                val = val ^ int(data[-1*j])
        data=data[:m-2**i] + str(val) + data[m-2**i+1:]
    return data

def detectError(data,r):
    m=len(data)
    res=0
    for i in range(r):
        val=0
        for j in range(1,m+1):
            if j & (2**i)==2**i:
                val = val^int(data[-1*j])
        res+=val*(10**i)
    return int(str(res),2)

data = '1011001'

m = len(data)
r = calcRedundantBit(m)
print(m,r)
arr = postRedundantBits(data, r)
print(arr)
arr = calcParityBit(arr,r)

# Data to be transferred
print("Data transferred is " + arr)

# Stimulate error in transmission by changing
# a bit value.
# 10101001110 -> 11101001110, error in 10th position.

arr = '11101001110'
print("Error Data is " + arr)
correction = detectError(arr, r)
print(correction)
if (correction == 0):
    print("There is no error in the received message.")
else:
    print("The position of error is ", len(arr) - correction + 1, "from the left")
