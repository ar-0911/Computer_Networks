no_frames = int(input("Enter number of frames to transmit: "))
window = int(input("Enter window size: "))
i = 1
k = 1
current = 1
total_transmission = 0
count = 1
frames = no_frames
for j in range(1,window+1):
    print("Sending frame: ",j)
    current += 1
    total_transmission+=1

while frames > 0:
    if count % 5 == 0:
        print("ERROR Retransmitting frame ",k)
        total_transmission += 1
        count += 1
        # for num in range(k+1,k+window):
        #     if num <= no_frames:
        #         print("Sending frame: ",num)
        #         count += 1
        #         total_transmission += 1

    if i <= no_frames:
        print("received acknowledgement for frame: ",i)
    frames -= 1
    i += 1
    k += 1
    if current <= no_frames:
        print("Sending frame: ",current)
        total_transmission += 1
    count += 1
    print(f"Current window :",end=" ")
    for num in range(k,k+window):
        if num <= no_frames:
            print(num,end=" ")
    print('\n')

    current += 1

print("Total transmission: ",total_transmission)