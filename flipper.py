from __future__ import print_function
from datetime import datetime, timedelta

from decimal import Decimal
from enum import Enum, unique
from functools import partial

from http.client import HTTPException
from os import listdir
from os.path import isfile, join
from pathlib import Path

from random import choice
from socket import timeout
from statistics import median_low
import argparse

# import colorama
import inspect
import json

import os
import os.path

import pprint as pp
import random
import re

import socket
import subprocess
import sys
import time
import traceback

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from RPA.Desktop.keywords import keyword
from RPA.Desktop import Desktop

desktop = Desktop()

import datetime
import os
from RPA.Windows import Windows


class Flipper:
    def __init__(self):
        self.desktop = Desktop()
        self.windows = Windows()

    def open_proton_vpn(self):
        print("Launching ProtonVPN")
        self.windows.windows_run(
            "C:\\Program Files (x86)\\Proton Technologies\\ProtonVPN\\ProtonVPN.exe"
        )
        pp.pprint(self.windows.__dict__)
        time.sleep(13)
        print("WINDOW LIST:")
        pp.pprint(self.windows.list_windows())
        proton_win = self.windows.control_window("type:WindowControl name:ProtonVPN")
        print("ProtonVPN WINDOW Details:")
        pp.pprint(proton_win.__dict__)

        time.sleep(3)
        self.windows.send_keys(keys="{WIN}{UP}")
        time.sleep(3)
        print("ProtonVPN Button Details:")
        buttons = self.windows.get_elements("type:Button")
        for button in buttons:
            pp.pprint(button.__dict__)

    def connect(self):
        print("Connecting to Random IP")
        desktop.move_mouse('ocr:"Random"')
        time.sleep(1)
        desktop.move_mouse("offset:175,0")
        time.sleep(1)
        desktop.click()
        time.sleep(13)

    def minimize(self):
        print("Minimizing ProtonVPN")
        self.windows.send_keys(keys="{ALT}{ESC}")
        time.sleep(3)
        # self.windows.close_current_window()

    def automate_proton_vpn(self):
        self.open_proton_vpn()
        self.connect()
        self.minimize()


if __name__ == "__main__":
    flipper = Flipper()
    flipper.automate_proton_vpn()