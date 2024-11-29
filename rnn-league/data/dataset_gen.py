import numpy as np
import pandas as pd

# Base sequences from your data
base_sequences = [
    # Paris
    {
        'sequence': [[10, 25, 60], [13, 10, 80], [9, 5, 90], [7, 0, 100]],
        'target': 110
    },
    # Berlin
    {
        'sequence': [[25, 20, 30], [26, 24, 50], [28, 20, 80], [22, 3, 110]],
        'target': 125
    },
    # London
    {
        'sequence': [[15, 10, 60], [25, 20, 65], [35, 10, 75], [36, 15, 70]],
        'target': 75
    }
]

# Function to generate a synthetic sequence
def generate_synthetic_sequence(base_sequence):
    sequence = np.array(base_sequence['sequence'], dtype=np.float32)
    target = base_sequence['target']

    # Add random noise to simulate variability
    sequence_noise = np.random.normal(0, 5, sequence.shape)
    target_noise = np.random.normal(0, 5)

    synthetic_sequence = sequence + sequence_noise
    synthetic_target = target + target_noise

    return synthetic_sequence.flatten(), synthetic_target

# Generate 1000 synthetic entries
data = []
for _ in range(1000):
    # Randomly select a base sequence
    base_sequence = np.random.choice(base_sequences)
    seq_features, seq_target = generate_synthetic_sequence(base_sequence)
    data.append(np.append(seq_features, seq_target))

# Define column names
columns = []
for day in range(1, 5):
    columns.extend([f'day{day}_temp', f'day{day}_speed', f'day{day}_pollution'])
columns.append('day5_pollution')

# Create DataFrame and save to CSV
df = pd.DataFrame(data, columns=columns)
df.to_csv('synthetic_dataset.csv', index=False)

print("Dataset created and saved to 'synthetic_dataset.csv'.")
