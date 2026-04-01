import typer


def main():
    from PyBlock import main as pyblock_main
    pyblock_main()


if __name__ == "__main__":
    typer.run(main)
