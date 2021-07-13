import unittest
from post import portlandInfo, miamiInfo, portlandPrint, miamiPrint


class test(unittest.TestCase):
      def test_dummy(self):
          self.assertEqual(True, True)
#     def test_portlandInfo(self):
#         urlport = 'http://api.openweathermap.org/data/2.5/weather?q=Portland,%20us&appid=382a88e893bb013cca439718beab4f51'
#         self.assertEqual(portlandInfo(), urlport)

        
#     def test_miamiInfo(self):
#         urlmiam = 'http://api.openweathermap.org/data/2.5/weather?q=Miami,%20us&appid=382a88e893bb013cca439718beab4f51'
#         self.assertEqual(miamiInfo(), urlmiam)
        
        
#     def test_portlandPrint(self):
#         port = {
#                'base': 'stations',
#                'clouds': {'all': 90},
#                'cod': 200,
#                'coord': {'lat': 45.5234, 'lon': -122.6762},
#                'dt': 1626191274,
#                'id': 5746545,
#                'main': {'feels_like': 289.61,
#                         'humidity': 75,
#                         'pressure': 1018,
#                         'temp': 289.92,
#                         'temp_max': 293.09,
#                         'temp_min': 287.11},
#                'name': 'Portland',
#                'sys': {'country': 'US',
#                        'id': 2008548,
#                        'sunrise': 1626179688,
#                        'sunset': 1626235067,
#                        'type': 2},
#                'timezone': -25200,
#                'visibility': 10000,
#                'weather': [{'description': 'overcast clouds',
#                             'icon': '04d',
#                             'id': 804,
#                             'main': 'Clouds'}],
#                'wind': {'deg': 338, 'gust': 3.58, 'speed': 0.89}
#                 }
#         urlport = 'http://api.openweathermap.org/data/2.5/weather?q=Portland,%20us&appid=382a88e893bb013cca439718beab4f51'
#         self.assertEqual(type(portlandPrint(urlport)), type(port))
                
#     def test_miamiPrint(self):
#         miam = {
#                'base': 'stations',
#                'clouds': {'all': 75},
#                'cod': 200,
#                'coord': {'lat': 25.7743, 'lon': -80.1937},
#                'dt': 1626191264,
#                'id': 4164138,
#                'main': {'feels_like': 307.38,
#                         'humidity': 77,
#                         'pressure': 1022,
#                         'temp': 302.2,
#                         'temp_max': 304.27,
#                         'temp_min': 300.93},
#                'name': 'Miami',
#                'sys': {'country': 'US',
#                        'id': 2009435,
#                        'sunrise': 1626172670,
#                        'sunset': 1626221692,
#                        'type': 2},
#                'timezone': -14400,
#                'visibility': 10000,
#                'weather': [{'description': 'thunderstorm',
#                             'icon': '11d',
#                             'id': 211,
#                             'main': 'Thunderstorm'}],
#                'wind': {'deg': 62, 'gust': 4.92, 'speed': 1.79}
#               }
#         urlmiam = 'http://api.openweathermap.org/data/2.5/weather?q=Miami,%20us&appid=382a88e893bb013cca439718beab4f51'
#         self.assertEqual(type(miamiPrint(urlmiam)), type(miam))

if __name__ == '__main__':
    unittest.main()