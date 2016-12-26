#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time;  # This is required to include time module.
import datetime;  # This is required to include time module.
import eventos
import unicodedata
import sys

reload(sys) 
sys.setdefaultencoding( "latin-1" )

while True:
     try:
         f = open("traffic.txt", "a");
         while True:
             try:
                  time.sleep(10)
                  today = datetime.datetime.today()
                  todaystr = str(today) + ',' 
                  
                  Notification = eventos.WazeRouteNotification()
                  ticks = time.time()
                  try:
                      rNotification,alerts=Notification.get_notification(ticks)
                  except eventos.WRCError as err:
                      print (err)
                  else:
                       pass
                  #print "%.2f" % alerts
                  if alerts :
                     for key in rNotification:
                     # print key
                     # print key ['type']
                     # print key ['subtype']
                     # print key ['street']
                     # print key ['nearBy']
                     # print key ['location']['x']
                     # print key ['location']['y']
                         try:
                              if key.get('nearBy'):
                                 nearBy = key['nearBy']
                              else:
                                 nearBy = " " 
                              if key.get('street'):
                                 street = key['street']
                              else:
                                 street = " " 
                              if key.get('city'):
                                 city = key['city']
                              else:
                                 city = " " 								 
                              if key.get('pubMillis'):
                                 pubMillis = key['pubMillis']
                              else:
                                 pubMillis = " " 								 
								  
                              if key.get('nThumbsUp'):
                                 nThumbsUp = key['nThumbsUp']
                              else:
                                 nThumbsUp = " " 
								 
                              if key.get('reportRating'):
                                 reportRating = key['reportRating']
                              else:
                                 reportRating = " " 									 
								 
                              if key.get('reliability'):
                                 reliability = key['reliability']
                              else:
                                 reliability = " " 									 
								 
                              if key.get('confidence'):
                                 confidence = key['confidence']
                              else:
                                 confidence = " " 									 
								 
                              if key.get('roadType'):
                                 roadType = key['roadType']
                              else:
                                 roadType = " " 									
								 
#                                        reliability + ',' +
#										 confidence + ',' +
                              #print "Key Get Pass "  
                              Registro = todaystr + city + ',' + street  + ',' + str(nearBy)  + ',' + str(nThumbsUp) + ',' + str(reportRating) + ',' + str(roadType) + ',' + key ['type'] + ',' + key ['subtype']  + ',' + "%.14f" % key ['location']['x']  + ',' + "%.14f" % key ['location']['y'] + ',' + str(pubMillis)
                              #print "Registro Pass " 
                              try:
                                  # if the Registro is a unicode string, normalize it
                                  Registro = unicodedata.normalize('NFKD', Registro).encode('ascii','ignore')
                              except TypeError:
                                  # if it was not a unicode string => OK, do nothing
                                  print ('Error TypeError... unicode Continue')
					   
                              print (Registro)
                              Registro = Registro + '\n'
                              f.write(Registro)
                         except IOError:
                           # if it was not a unicode string => OK, do nothing
				                print ('Error IOError... Rnotification Continue')
                         except TypeError:  
                                print ('Error TypeError... Rnotification Continue')
                         else:
         	                    pass
     							  
             except TypeError:  
                     print ('Error TypeError... InnerLoop Continue')
             except IOError:
                           # if it was not a unicode string => OK, do nothing
				    print ('Error IOError... InnerLoop Continue')					 
             else: 
                     Registro = ''			
     except IOError:
                  # if it was not a unicode string => OK, do nothing
             print ('Error IOError... Outter loop Continue')
     else:
	         pass