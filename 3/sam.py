from time import *
from socket import *
from sys import *
from select import *
from subprocess import *

ip = ''
port = 4000

c = "xdotool getwindowfocus windowmove".split()

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((ip, port))

while True:
    select_r, select_w, select_x = select([sock], [], [])
    for s in select_r:
	dat, addr = s.recvfrom(1024)
	print ord(dat)
	#call(c + [str(2.5 * ord(dat[0])),str( 1.5 * ord(dat[1]))])
