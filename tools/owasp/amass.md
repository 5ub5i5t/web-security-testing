# amass

Example Usage
```
amass enum -brute -active -d {target} -o amass-output.txt
```

Check amass results for active endpoints with httprobe by TomNomNom
```
cat amass-output.txt | httprobe -p http:81 -p http:3000 -p https:3000 -p http:3001 -p https:3001 -p http:8000 -p http:8080 -p https:8443 -c 50 | tee online-domains.txt
```

Check for new domains
```
cat new-output.txt | anew old-output.txt | httprobe
```

More thorough check with dnsgen
```
cat amass-output.txt | dnsgen - | httprobe
```