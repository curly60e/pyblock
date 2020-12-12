import configparser
import logging
import os
import time

from logging.handlers import RotatingFileHandler

from connections import test_tor
from welcome import logo
from dashboard import main_dashboard

from ansi_management import (warning, success, error, info, clear_screen, bold)
from dependencies.yaspin import yaspin

# Main Variables
basedir = os.path.abspath(os.path.dirname(__file__))
debug_file = os.path.join(basedir, 'debug.log')


def load_config(quiet=False):
    # Load Config
    config_file = os.path.join(basedir, 'config.ini')
    CONFIG = configparser.ConfigParser()
    if quiet:
        CONFIG.read(config_file)
        return (CONFIG)

    with yaspin(text="Loading config.ini", color="cyan") as spinner:

        # Check that config file exists
        if os.path.isfile(config_file):
            CONFIG.read(config_file)
            spinner.ok("✅ ")
            spinner.write(success("    Config Loaded [Success]"))
            print("")
            return (CONFIG)
        else:
            spinner.fail("💥 ")
            spinner.write(
                warning("    Config file could not be loaded [ERROR]"))
            print(error("    WARden requires config.ini to run. Quitting..."))
            exit()


def launch_logger():
    # Config of Logging
    formatter = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    logging.basicConfig(handlers=[
        RotatingFileHandler(filename=debug_file,
                            mode='w',
                            maxBytes=120000,
                            backupCount=0)
    ],
                        level=logging.INFO,
                        format=formatter,
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info("Starting main program...")


def create_tor():
    # ----------------------------------------------
    #                 Test Tor
    # ----------------------------------------------
    with yaspin(text="Testing Tor", color="cyan") as spinner:
        tor = test_tor()
        if tor['status']:
            logging.info("Tor Connected")
            spinner.ok("✅ ")
            spinner.write(success("    Tor Connected [Success]"))
            print("")
            return (tor)
        else:
            logging.error("Could not connect to Tor")
            spinner.fail("💥 ")
            spinner.write(warning("    Tor NOT connected [ERROR]"))
            print(
                error(
                    "    Could not connect to Tor. WARden requires Tor to run. Quitting..."
                ))
            exit()


if __name__ == '__main__':
    clear_screen()
    logo()
    print("")
    launch_logger()
    config = load_config()
    tor = create_tor()
    with yaspin(text="Launching Dashboard. Please Wait...",
                color="cyan") as spinner:
        main_dashboard(config, tor, spinner)
