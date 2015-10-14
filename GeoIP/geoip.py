import pygeoip
import sys

class GEOIP:

	def __init__(self,ip):
		self.ip = ip
		self.geolitecity_dat = "GeoLiteCity.dat"
		self.geoip_dat = "GeoIP.dat"
		
	def get_counrty_of_ip(self):
		country = pygeoip.GeoIP(self.geoip_dat)
		return country.country_name_by_addr(self.ip)
		
	def get_city_of_ip(self):
		city = pygeoip.GeoIP(self.geolitecity_dat)	
		return city.time_zone_by_addr(self.ip)

if len(sys.argv) == 2:
	get_geo = GEOIP(sys.argv[1])
	print "IP      = %s\nCountry = %s\nCity    = %s" %(sys.argv[1],get_geo.get_counrty_of_ip(),get_geo.get_city_of_ip())
	


