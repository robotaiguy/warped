import os
from typing import List


def get_all_input_files(input_dir: str) -> List[str]:
    filenames = next(os.walk(input_dir), (None, None, []))[2]
    files = filter(lambda f: (f.endswith("yaml") or f.endswith("yml")), filenames)
    return list(files)


def ensure_output_dir(output_dir: str):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


if __name__ == "__main__":
    print("Not meant to be run as script. Aborting")
    exit()
