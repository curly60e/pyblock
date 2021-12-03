import os
import typer


def main():
    scriptpath = os.path.join(os.path.dirname(__file__), 'PyBlock.py')
    os.system(f"python3 {scriptpath}")


if __name__ == "__main__":
    typer.run(main)
