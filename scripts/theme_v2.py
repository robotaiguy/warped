import argparse

import yaml

from io_helper import *


def main():
    print("running")
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Updating theme files"
    )
    parser.add_argument(
        "input_dir",
        type=str,
        help="Directory from which to read in all Warp themes.",
    )
    parser.add_argument(
        "output_dir",
        type=str,
        help="Directory to output updated Warp themes.",
    )
    args = parser.parse_args()

    ensure_output_dir(args.output_dir)

    filenames: List[str] = get_all_input_files(args.input_dir)
    filename: str
    for filename in filenames:
        file = open(os.path.join(args.input_dir, filename), "r")
        loaded_theme = yaml.safe_load(file)

        print(loaded_theme)
        print(type(loaded_theme))
        break


if __name__ == "__main__":
    main()
