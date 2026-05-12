import odrive
import time
import csv
from datetime import datetime

# Record one data point every second
LOG_INTERVAL_SECONDS = 1

# Create a timestamped CSV filename
csv_filename = f"odrive_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

print("Looking for ODrive over USB...")
odrv = odrive.find_any()
print("ODrive connected.")

with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)

    # CSV header row
    writer.writerow([
        "timestamp",
        "elapsed_time_s",
        "current_a",
        "position_turns",
        "velocity_turns_per_s"
    ])

    start_time = time.time()

    print(f"Recording data every {LOG_INTERVAL_SECONDS} second(s).")
    print(f"Saving to: {csv_filename}")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            timestamp = datetime.now().isoformat(timespec="seconds")
            elapsed_time = time.time() - start_time

            # Read values from ODrive
            current = odrv.axis0.foc.Iq_measured
            position = odrv.axis0.pos_estimate
            velocity = odrv.axis0.vel_estimate

            # Write one row to CSV
            writer.writerow([
                timestamp,
                round(elapsed_time, 3),
                current,
                position,
                velocity
            ])

            # Save immediately so data is not lost if stopped
            file.flush()

            print(
                f"{timestamp} | "
                f"current={current:.4f} A | "
                f"position={position:.4f} turns | "
                f"velocity={velocity:.4f} turns/s"
            )

            time.sleep(LOG_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("\nLogging stopped.")
        print(f"Data saved to: {csv_filename}")