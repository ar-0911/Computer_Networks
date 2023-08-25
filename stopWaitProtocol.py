import random
import time

no_of_frames = random.randint(1,15)
print("Total number of frames to be transmitted = " + str(no_of_frames))
frames = no_of_frames
i = 1
while frames > 0:
    print("Sending frame " + str(i))
    time.sleep(2)
    print("Waiting for acknowledgment")
    time.sleep(2)
    # checking if frame is received
    x1 = random.randint(1,1000)
    if x1 % 2 == 0:
        print("Error while receiving frame")
        time.sleep(1)
        print("Waiting for 1 second")
        time.sleep(1)
        print("Retransmitting frame "+str(i))
        time.sleep(2)
    print("Acknowledgement for frame " + str(i))
    frames -= 1
    i += 1
    time.sleep(1)
print("\nAll frames transmitted\n\nEnd of stop and wait protocol")
