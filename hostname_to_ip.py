import sys
import socket

# Take in a list of hostnames with one host name per line and create a list of hostname, ips one per line.
# usage: python hostname_to_ip.py my_hostnames.txt my_results.txt
#        The first argument is the file name that contains your list of hostnames. (my_hostnames.txt)
#        The second argument is the name of the file where you want to store the results. (my_results.txt)

try:
    hostnames_file = sys.argv[1]
    hostname_and_ip_file = sys.argv[2]
    out = open(hostname_and_ip_file, 'w')

    with open(hostnames_file, "r") as ins:
        for line in ins:
            hostname = line.strip().replace('\n', '')
            ip = socket.gethostbyname(hostname)
            try:
                socket.gethostbyaddr(ip)
            except Exception as e:
                msg = e.args[0]
                ip = e.args[1]
            outline = hostname + ', ' + ip
            print outline
            out.write(outline + '\n')
except IndexError as e:
    print 'Usage error: This python script requires 2 arguments like so: python hostname_to_ip.py hostnames.txt ' \
          'results.txt\n' \
          'Where hostnames.txt is the file with the list of hostnames and results.txt will contain your results.\n'
except Exception as e:
    print e
