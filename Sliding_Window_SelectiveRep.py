import random
import time


def transmit_frames(frames, window_size):
    total_frames = len(frames)
    remaining_frames = total_frames
    next_seq_num = 0
    window_start = 0
    window_end = min(window_size, total_frames)
    retransmitted_frames = []
    while window_start < total_frames:
        frames_to_transmit = frames[window_start:window_end]
        no_error = True
        for i, frame in enumerate(frames_to_transmit):
            print(f"Transmitting frame {frame}...")
        for j, frame in enumerate(frames_to_transmit):
            if random.randint(1, 1000) % 2 == 0 and no_error:
                print(f"Error in transmitting frame {frame}.")
                time.sleep(1)
                remaining_frames += 1
                retransmitted_frames.append(frame)
                no_error = False
            else:
                print(f"Acknowledgement received for frame {frame}.")
                time.sleep(1)
                remaining_frames -= 1
        if remaining_frames > 0:
            if retransmitted_frames:
                print("Retransmitting frames with errors:")
                time.sleep(1)
                for retransmitted_frame in retransmitted_frames:
                    print(f"Retransmitting frame {retransmitted_frame}...")
                    time.sleep(0.5)
                    print(f"Acknowledgement received for frame {retransmitted_frame}")
                    time.sleep(1)
                retransmitted_frames = []
            else:
                print("No frames to retransmit.")
            time.sleep(2)

        window_start = window_end
        window_end = min(window_start + window_size, total_frames)

        current_window_size = window_end - window_start

        print(f"Current window size: {current_window_size}")

    print("All frames transmitted. Program stopped.")


total_frames = 8#random.randint(10, 20)
print(f"Total frames = {total_frames}")

window_size = int(input("Enter the window size:"))
frames = [f"Frame {i}" for i in range(total_frames)]
current_window_size = min(window_size, total_frames)


print(f"Total frames: {total_frames}")
print(f"Window size: {window_size}")
print(f"Current window size: {current_window_size}")
transmit_frames(frames, window_size)
print(" says:\n Sliding window successfully executed ")

# transmit_frames(frames, window_size)