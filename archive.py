from datetime import date, timedelta
import urllib.request as urlrequest
import os
import time

# dates for #dvn
sdate1 = date(2012, 12, 8)
edate1 = date(2014, 6, 24)

delta1 = edate1 - sdate1

# archive #dataverse
for i in range(delta1.days + 1):
    day = str(sdate1 + timedelta(days=i))
    print(day)
    time.sleep(1)
    url = 'http://irclog.iq.harvard.edu/dvn/' + day
    response = urlrequest.urlopen(url)
    content = response.read().decode(response.info().get_param('charset') or 'utf-8')
    daydir = 'dvn/' + day
    os.makedirs(daydir, exist_ok=True)
    with open(daydir + '/index.html', 'w') as indexfile:
        indexfile.write(content)

# get index page for #dvn
url1 = 'http://irclog.iq.harvard.edu/dvn/'
response1 = urlrequest.urlopen(url1)
content1 = response1.read().decode(response.info().get_param('charset') or 'utf-8')
chandir1 = 'dvn/'
os.makedirs(chandir1, exist_ok=True)
with open(chandir1 + '/index.html', 'w') as indexfile:
    indexfile.write(content1)

# dates for #dataverse
sdate2 = date(2014, 6, 24)
edate2 = date(2021, 6, 4)

delta2 = edate2 - sdate2

# archive #dataverse
for i in range(delta2.days + 1):
    day = str(sdate2 + timedelta(days=i))
    print(day)
    time.sleep(1)
    url = 'http://irclog.iq.harvard.edu/dataverse/' + day
    response = urlrequest.urlopen(url)
    content = response.read().decode(response.info().get_param('charset') or 'utf-8')
    daydir = 'dataverse/' + day
    os.makedirs(daydir, exist_ok=True)
    with open(daydir + '/index.html', 'w') as indexfile:
        indexfile.write(content)

# get index page for #dataverse
url2 = 'http://irclog.iq.harvard.edu/dataverse/'
response2 = urlrequest.urlopen(url2)
content2 = response2.read().decode(response.info().get_param('charset') or 'utf-8')
chandir2 = 'dataverse/'
os.makedirs(chandir2, exist_ok=True)
with open(chandir2 + '/index.html', 'w') as indexfile:
    indexfile.write(content2)
