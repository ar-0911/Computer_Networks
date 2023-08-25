import time

no_of_frames = 11#random.randint(10, 15)
print("Total number of frames to be transmitted = " + str(no_of_frames))
window = int(input("Enter Window size: "))
frames = no_of_frames
i = 1
k = 1
flag = 0
start = 0
count = 1
for j in range(1, window + 1):
    print(f"Sending frame {j}")
    time.sleep(1)

while frames > 1:

    if count %5 == 0:
        print(f"\tNo acknowledgement for frame {i}")
        print(f"Retransmitting frame {i}")
        if flag == 0:
            k = i + 1
        flag = 1
        count+=1
        #time.sleep(1)
    else:
        print(f"\tReceived acknowledgement for frame {i}")
        count+=1
        i += 1
        if flag == 0:
            if start == 0:
                k += window
            else:
                k+=1
        else:
            k += window - 1
        frames -= 1
        flag = 0
        #time.sleep(1)
        start=1

    if flag == 1:
        n = window - 1

    else:
        n = 1

    # sending the next frame
    for j in range(0, n):
        if k + j <= no_of_frames:
            print(f"Sending frame {k + j}")
         #   time.sleep(1)

# acknowledge for left over frames after all frames are sent
while i <= no_of_frames:
    print(f"\tReceived acknowledgement for frame {i}")
    i += 1
    #time.sleep(1)

print("\nend of Sliding protocol (Go back N)")