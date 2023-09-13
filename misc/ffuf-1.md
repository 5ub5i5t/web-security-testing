# ffuf - 1

Find Directories and send to Burp:
```
ffuf -w /SecLists/Discovery/Web-Content/raft-large-directories.txt -u https://{TARGET}/FUZZ -o ffuf-output.json -replay-proxy http://127.0.0.1:8080
```

Find Directories (RATE LIMIT) and send to Burp:
```
ffuf -w ./SecLists/Discovery/Web-Content/raft-large-directories.txt -u https://{TARGET}/FUZZ -o ffuf-output.json -replay-proxy http://127.0.0.1:8080 -t 5 -p 0.1-2.0 -rate 1
```

Find Subdomains:
```
ffuf -w /SecLists/Discovery/DNS/subdomains-top1million-110000.txt -t 10 -u http://FUZZ.{TARGET} -o ffuf-output.json -replay-proxy http://127.0.0.1:8080
```

