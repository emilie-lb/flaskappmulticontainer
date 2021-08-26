#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
# import create_db as create_db

logging.basicConfig(level=logging.DEBUG)


def liste_stations():
    liste_stations = ['MOSSON', 'BELVEDERE', 'ODYSSEUM']
    liste_stations = sorted(list(liste_stations))
    # print(liste_stations)
    return liste_stations
