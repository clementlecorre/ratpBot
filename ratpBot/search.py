#!/usr/bin/env python

import getopt
import sys
import ratp

# Emojis icon
metro = u'\U0001F689'
flag = u'\U0001F6A9'
CRYINGFACE = u'\U0001F622'
CLOCK = u'\U0001F556'

def extractInformation(transport,
    line,
    station, direction):
  if station is not None and station != "":
    times = ratp.getNextStopsAtStation(transport, line, station, direction)
    stops = ""
    resultat = ""
    for time, direction, stationname in times:
      station = stationname
      if direction:
        stops += ("\n%s—%s: %s direction %s;" % (metro, station, time, direction))
      else:
        stops += ("\n%s—%s: %s;" % (CLOCK, station, time))
    if len(stops) > 0:
      resultat += ("%s Prochains passages du %s ligne %s à l'arrêt %s : %s \n" % (flag, transport, line, stationname, stops))
    else:
      resultat += ("La station `%s' ne semble pas exister sur le %s ligne %s." % (station, transport, line))
  else:
    stations = ratp.getAllStations(transport, line)
    if len(stations) > 0:
      s = ""
      for name in stations:
        s += "\n— " + name + " ;"
      resultat = ("%s Stations : %s" % (metro,s))
    else:
      resultat = ("%s Sorry, Aucune station trouvée." % (CRYINGFACE))
  return resultat


def getDisturbance(cause, type_transp):
    if cause == '':
        return None
    else:
        return ratp.getDisturbance(cause, type_transp)
