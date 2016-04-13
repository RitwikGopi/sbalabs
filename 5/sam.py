from pylab import *
from time import *
from random import *
from socket import *
from sys import *
from select import *

r = [0 for i in xrange(20)]
g = [0 for i in xrange(20)]
b = [0 for i in xrange(20)]

ip = ''
port = 4000

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((ip, port))

while True:
    select_r, select_w, select_x = select([sock], [], [])
    for s in select_r:
	r = r[-20:]
	g = g[-20:]
	b = b[-20:]
	dat, addr = s.recvfrom(1024)
	print ord(dat[0]), ord(dat[1]), ord(dat[2])
	r.append(ord(dat[0]))
	g.append(ord(dat[1]))
	b.append(ord(dat[2]))
	fig = figure(figsize = (20,10))
	ylim([0,300])
	plot(r, 'r')
	plot(g, 'g')
	plot(b, 'b')
	savefig("/var/www/html/fig")
	close(fig)
