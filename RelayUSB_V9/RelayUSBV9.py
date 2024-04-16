#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Johannes Majer, HQD Lab, USTC
# Created Date: 2024-04-16
# version ='0.2.0'
# ---------------------------------------------------------------------------
""" module to control RelayUSB V9 devices"""

import serial
import serial.tools.list_ports

class RelayUSBV9:

    def __init__(self, port):
        self.ser = serial.Serial(port, 115200)

    def on(self):
        self.ser.write(b'set on\n')

    def off(self):
        self.ser.write(b'set off\n')

    def set(self, newStatus):
        if newStatus == True:
            self.on()
        else:
            self.off()

    @staticmethod
    def listPorts():
        comPorts = serial.tools.list_ports.comports()
        for p in comPorts:
            if p.description == "RelayUSB":
                print(p.device)
                print("    %s" % p.description)
                print(f"     Vendor ID: 0x{p.vid:04X}")
                print(f"    Product ID: 0x{p.pid:04X}")
