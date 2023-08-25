no_frames = int(input("Enter frames: "))
window = int(input("Enter window size: "))
i=1
k=1
count=1
current=1
total = 0
frames = no_frames
while frames>0:
    if count % 5 == 0:
        print(f"\nERROR RECIEVING ACK FOR {k}\n\nRetransmitting frame: {k}")
        count+=1
        total+=1
        for num in range(k+1,k+window):
            if num<=no_frames:
                print("Sending frame: ",num)
                count+=1
                total+=1
    print("Waiting for ack")
    print("Recieved ack for frame: ",i)
    i+=1
    if current <= no_frames:
        print("Sending frame: ",current)
        total+=1
    count+=1
    k+=1
    print("Current window: ",end="")
    for num in range(k,k+window):
        if num<=no_frames:
            print(num,end=" ")
    print()
    current+=1
    frames-=1
print("Total number of transmissions: ",total)