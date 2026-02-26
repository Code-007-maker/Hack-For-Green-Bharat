import pathway as pw
import numpy as np
import time
import json
from datetime import datetime

# This connector simulates a live stream of segmentation metadata from the Duality AI dataset.
# In production, this would be a real stream from the robot's camera/ML edge processor.

def generate_live_segmentation_masks():
    """
    Simulation of real-time segmentation mask statistics.
    Classes: 0:Tree, 1:Bush, 2:Grass, 3:Rock, 4:Log, 5:Ground, 6:Sky, 7:Other
    """
    while True:
        # Create mock spatial telemetry
        timestamp = datetime.now().isoformat()
        
        # Simulating pixel counts for environmental features
        pixel_stats = {
            "timestamp": timestamp,
            "vegetation_pixels": int(np.random.randint(5000, 15000)),
            "dry_grass_pixels": int(np.random.randint(20000, 40000)),
            "rock_pixels": int(np.random.randint(1000, 5000)),
            "ground_pixels": int(np.random.randint(50000, 100000)),
            "total_pixels": 262144, # 512x512
            "sensor_id": "OFFROAD_CAM_01",
            "location_lat": 28.6139 + np.random.uniform(-0.01, 0.01),
            "location_lon": 77.2090 + np.random.uniform(-0.01, 0.01)
        }
        
        yield pixel_stats
        time.sleep(2) # Stream every 2 seconds

def get_stream_connector():
    # Use Pathway's from_generator to ingest our simulation
    return pw.io.jsonlines.from_generator(generate_live_segmentation_masks())

if __name__ == "__main__":
    # Test connector standalone
    gen = generate_live_segmentation_masks()
    for _ in range(3):
        print(next(gen))
