{'application':{'type':'Application',
          'name':'Widget Control',
    'backgrounds': [
    {'type':'Background',
          'name':'bgControlMobo',
          'title':'Widget Control Tool',
          'size':(917, 371),

         'components': [

{'type':'StaticText', 
    'name':'BoardType', 
    'position':(15, 21), 
    'size':(175, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'Board Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxBoard', 
    'position':(10, 55), 
    'size':(100, -1), 
    'items':[u'none', u'widget', u'usbi2s', u'usbdac', u'test'], 
    'text':'board', 
    },

{'type':'StaticText', 
    'name':'ImageType', 
    'position':(144, 21), 
    'size':(175, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'Image Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxImage', 
    'position':(132, 55), 
    'size':(135, -1), 
    'items':[u'flashyblinky', u'uac1_audio', u'uac1_dg8saq', u'uac2_audio', u'uac2_dg8saq', u'hpsdr', u'test'], 
    'text':'Image', 
    },

{'type':'StaticText', 
    'name':'InType', 
    'position':(307, 22), 
    'size':(175, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'IN Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxIn', 
    'position':(287, 55), 
    'size':(100, -1), 
    'items':[u'normal', u'swapped'], 
    'text':'IN Type', 
    },

{'type':'StaticText', 
    'name':'OutType', 
    'position':(425, 21), 
    'size':(175, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'OUT Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxOut', 
    'position':(416, 55), 
    'size':(100, -1), 
    'items':[u'normal', u'swapped'], 
    'text':'OUT Type', 
    },

{'type':'StaticText', 
    'name':'AdcType', 
    'position':(29, 127), 
    'size':(175, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'ADC Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxAdc', 
    'position':(12, 154), 
    'size':(100, -1), 
    'items':[u'none', u'ak5394a'], 
    'text':'ADC Type', 
    },

{'type':'StaticText', 
    'name':'DacType', 
    'position':(155, 127), 
    'size':(175, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'DAC Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxDac', 
    'position':(148, 154), 
    'size':(100, -1), 
    'items':[u'none', u'cs4344', u'es9022'], 
    'text':'DAC Type', 
    },

{'type':'StaticText', 
    'name':'LCDType', 
    'position':(281, 127), 
    'size':(175, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'LCD Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxLCD', 
    'position':(271, 154), 
    'size':(100, -1), 
    'items':[u'none', u'hd44780', u'ks0073'], 
    'text':'LCD Type', 
    },

{'type':'StaticText', 
    'name':'LogType', 
    'position':(419, 127), 
    'size':(175, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 12}, 
    'text':'Log Type:', 
    },

{'type':'ComboBox', 
    'name':'ComboBoxLog', 
    'position':(413, 154), 
    'size':(100, -1), 
    'items':[u'none', u'125ms', u'250ms', u'500ms', u'1sec', u'2sec', u'4sec'], 
    'text':'log', 
    },

{'type':'StaticBox', 
    'name':'readFromFirmware', 
    'position':(29, 281), 
    'size':(175, 43), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Read From Firmware', 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(534, 19), 
    'size':(98, 90), 
    'alignment':'center', 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'style': 'bold', 'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 16}, 
    'text':'Control Widget', 
    },

{'type':'StaticBox', 
    'name':'staticboxFirmware', 
    'position':(728, 180), 
    'size':(175, 86), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Firmware Control', 
    },

{'type':'StaticText', 
    'name':'FirmwareSdisplay', 
    'position':(811, 199), 
    'size':(87, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'text':'FirmwareSdisplay', 
    },

{'type':'StaticText', 
    'name':'serialNumber', 
    'position':(734, 199), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'text':'Serial Number:', 
    },

{'type':'StaticText', 
    'name':'FirmwareVdisplay', 
    'position':(812, 215), 
    'size':(87, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'text':'FirmwareVdisplay', 
    },

{'type':'StaticText', 
    'name':'stFirmwareV', 
    'position':(735, 216), 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'text':'Version........:', 
    },

{'type':'StaticLine', 
    'name':'StaticLine11', 
    'position':(387, 430), 
    'size':(107, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'layout':'horizontal', 
    },

{'type':'StaticLine', 
    'name':'StaticLine1', 
    'position':(387, 344), 
    'size':(107, -1), 
    'backgroundColor':(240, 235, 226, 255), 
    'layout':'horizontal', 
    },

{'type':'StaticText', 
    'name':'stAuthor', 
    'position':(546, 92), 
    'size':(82, 22), 
    'alignment':'center', 
    'backgroundColor':(240, 235, 226, 255), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 6}, 
    'text':'V 001 2011-03-11 9V1AL', 
    },

{'type':'Image', 
    'name':'Image1', 
    'position':(659, 10), 
    'size':(245, 156), 
    'backgroundColor':(240, 235, 226, 255), 
    'file':'Po_SWR_board_beta.JPG', 
    },

{'type':'Button', 
    'name':'btnReset', 
    'position':(516, 300), 
    'size':(86, 25), 
    'command':'btnReset', 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Reset', 
    },

{'type':'Button', 
    'name':'btnFactoryReset', 
    'position':(624, 300), 
    'size':(86, 25), 
    'command':'btnFactoryReset', 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Factory Reset', 
    },

{'type':'Button', 
    'name':'btnStartUSB', 
    'position':(732, 300), 
    'size':(75, 25), 
    'command':'USB', 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Start USB', 
    },

{'type':'Button', 
    'name':'btnRefresh', 
    'position':(33, 300), 
    'size':(83, 27), 
    'command':'Refresh', 
    'default':1, 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Read', 
    },

{'type':'Button', 
    'name':'btnQuit', 
    'position':(821, 300), 
    'size':(75, 25), 
    'command':'Exit', 
    'font':{'faceName': u'FreeSans', 'family': 'sansSerif', 'size': 8}, 
    'label':'Quit', 
    },

] # end components
} # end background
] # end backgrounds
} }
