#!/bin/python
# -*- coding: utf-8 -*-
#__author__ = "Kevin Van den Brande"
#check if there is an active internet connection

import socket
import os

REMOTE_SERVER = "www.google.com"

def is_connected():
  try:
  # see if we can resolve the host name -- tells us if there is
  # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
  # connect to the host -- tells us if the host is actually
  # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
    pass
    return False
