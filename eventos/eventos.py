# -*- coding: utf-8 -*-
"""Waze route calculator"""

import json
import logging
import urllib


class WRCError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

			
class WazeRouteNotification():
    """Calculate actual route time and distance with waze api"""

    def get_notification(self, ticks):
        """Get route data from waze"""		
        Url = "https://www.waze.com/row-rtserver/web/TGeoRSS?ma=400&mj=100&mu=100&left=-79.855&right=-78.863&bottom=8.801&top=9.229&_=" + str(int(ticks))
        #print Url 
        rnotification = urllib.urlopen(Url).read()
        rnotification_json = json.loads(rnotification)
        
        if rnotification_json.get("error"):
           raise WRCError(rnotification_json.get("error"))
        if rnotification_json.get("alerts"):
            return rnotification_json['alerts'], 1
        if rnotification_json.get("users"):
           return rnotification_json['users'], 0
