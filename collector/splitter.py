import os
from math import ceil


def split_and_export(configs, parts=3, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)

    total = len(configs)
    chunk_size = ceil(total / parts)

    for i in range(parts):
        start = i * chunk_size
        end = start + chunk_size
        chunk = configs[start:end]

        filename = os.path.join(output_dir, f"raw_part_{i+1}.txt")

        with open(filename, "w", encoding="utf-8") as f:
            for c in chunk:
                f.write(c.strip() + "\n")

    print(f"Split into {parts} files (~{chunk_size} configs each)")
