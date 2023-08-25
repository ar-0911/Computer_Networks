no_frames = int(input("Enter number of frames: "))
window = int(input("Enter window size: "))
i = 1
current = 1
k = 1
count = 1
total_transmission = 0
frames = no_frames
retransmitted = -1
for j in range(1, window + 1):
    print("Sending frame: ", j)
    current += 1
    total_transmission += 1

while frames > 0:
    if count % 2 == 0:
        print("ERROR\nRetransmitting frame: ", k)
        print("\n")
        total_transmission += 1
        count += 1

    if i <= no_frames:
        print("Received ack for frame: ", i)
    i += 1
    k += 1
    if current <= no_frames:
        print("Sending frame: ", current)
        total_transmission += 1
    count += 1
    print("Current window:", end=" ")
    for num in range(k, k + window):
        if num <= no_frames:
            print(num, end=" ")
    print("\n")
    current += 1
    frames -= 1

print("Total transmission: ", total_transmission)
