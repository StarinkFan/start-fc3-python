# -*- coding: utf-8 -*-

import logging
import os
from flask import Flask
import pandas
import pycurl

def handler(event, context):
    logger = logging.getLogger()
    logger.info('114514')
    logger.info('1919810')
    logger.info(event)
    return event
