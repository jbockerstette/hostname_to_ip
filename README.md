# Hostname to IP

Python script to find the ip addresses of a list of hostnames. The script will handle unknown host names as well.

Usage: hostname_to_ip.py in_file out_file

    in_file: The filename that contains a list of hostnames with 1 hostname per line.
    out_file: The filename where you want to output to go. The output will be in the form of
    hostname, ip per line. 

```python hostname_to_ip.py test.txt results.txt```

test.txt contents:
```
google.com
asdlfjlsdasfasdfasf.com
yahoo.com
localhost
```

results.txt contents:
```
google.com, 172.217.9.142
asdlfjlsdasfasdfasf.com, Unknown host
yahoo.com, 206.190.36.45
localhost, 127.0.0.1

```