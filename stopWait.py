no_of_frames = int(input("Enter number of frames to be sent: "))
count = 1
i=0
frames = no_of_frames
total_frames_transmitted = 0
while count <= frames:
    print("Sending frame: ",str(count))
    total_frames_transmitted += 1
    i += 1
    print("Waiting for acknowledgement")
    if i == 4:
        print("Error")
        print("Retransmitting frame: ",str(count))
        total_frames_transmitted += 1
        i += 1
    print("Acknowledgement received for frame: ",str(count))
    count += 1
    i %= 5

print("\nTotal frames Transmitted: ",total_frames_transmitted)
