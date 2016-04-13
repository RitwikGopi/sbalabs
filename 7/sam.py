from time import *
from socket import *
from sys import *
from select import *
from subprocess import *
import pylab

ip = ''
port = 4000
a = []


sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((ip, port))

count = 0

while True:
    select_r, select_w, select_x = select([sock], [], [])
    for s in select_r:
	dat, addr = s.recvfrom(1024)
	print ord(dat)
