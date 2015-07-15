from urllib import urlopen as uo

site = 'http://localhost:8000/' #change localhost number

def write(x):
    response = uo(site + 'write/' + x)
    display(response)


def writecf(x):
    response = uo(site + 'writecf/' + x)
    display(response)


def display(response):
    print 'RESPONSE:', response
    print 'URL: ', response.geturl()
    
    pageread = response.read()
    print 'PAGE: ', pageread
    print 'LENGTH: ', len(pageread)

    headers = response.info()
    print 'DATE: ', headers['date']

    #display x-powered-by, access-control-allow-origin, content-type, content-length, etag, date, connection
    #print 'HEADERS: ', headers

write('test2')
writecf('test3')
