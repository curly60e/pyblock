import os
import subprocess
import typer


def main():
    scriptpath = os.path.join(os.path.dirname(__file__), 'PyBlock.py')
    subprocess.Popen(['python', scriptpath])


if __name__ == "__main__":
    typer.run(main)
