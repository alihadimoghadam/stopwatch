import keyboard
import time


def stopwatch() :
    start_time = None
    elapsed_time = 0

    while True :
        if keyboard.is_pressed('s') and start_time is None :
            start_time = time.time()
            print("Stopwatch started.")

        elif keyboard.is_pressed('s') and start_time is not None :
            elapsed_time += time.time() - start_time
            start_time = None
            print("Stopwatch stopped.")

        elif keyboard.is_pressed('q') :
            break

        if start_time is not None :
            current_time = time.time() - start_time + elapsed_time
            print(f"Elapsed time: {current_time:.2f} seconds")

        time.sleep(0.1)


stopwatch()
