# remove_animation.py
from pathlib import Path
import shutil

def main():

    # get the current working directory (where this script resides)
    cwd = Path().absolute()
    # get the root directory of the repo
    root_dir = Path(__file__).parents[2]
    
    animated_gems_path = root_dir.joinpath("_ark/ui/track/animated_gems")
    shutil.rmtree(animated_gems_path)

if __name__ == "__main__":
    main()