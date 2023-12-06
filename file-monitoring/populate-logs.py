import pandas as pd
from datetime import datetime
from pathlib import Path

import random
import time

log_path = Path(__file__).parent / "logs.csv"

while True:
    status = "status" + str(random.randint(0, 20))
    # Create a new DataFrame with the current time and the random status
    df = pd.DataFrame({"date": [datetime.now()], "status": [status]})

    df.to_csv(log_path, mode="a", header=False, index=False)
    # Wait for a second before the next append operation
    time.sleep(random.randint(1, 5))
