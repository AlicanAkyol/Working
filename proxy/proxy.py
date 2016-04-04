import urllib2

proxy = urllib2.ProxyHandler({'http': 'http://37.46.129.238:8080'})## the ip will be set from proxy ip's websites..
proxy_ssl = urllib2.ProxyHandler({'https': 'https://37.46.129.238:8080'})

auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)

conn = urllib2.urlopen('http://wtfismyip.com/text')
return_str = conn.read()
print(return_str)
