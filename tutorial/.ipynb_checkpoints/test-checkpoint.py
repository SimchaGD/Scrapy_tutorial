import pandas as pd
from tqdm import tqdm

pbar = tqdm(total = 1000)
for i in range(1000):
    a = i
    pbar.update()