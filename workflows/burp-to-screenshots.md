# Burp to Screenshots

Commands used:
- cat
- grep
- sort
- uniq
- sed
- awk
- xargs
- sh

Tools used:
- anew
- Burp Suite
- httpx
- jq
- gowitness

Extract scope from burp:
```
jq '.[].id' target_assets.json | sort | uniq | sed -e 's/^"//' -e 's/"$//' | anew jq_id_output.txt
```

Find tech and send to burp:
```
cat target-in-scope.txt| httpx -title -tech-detect -status-code -silent -timeout 100 -o httpx_status-code_results.txt -http-proxy http://127.0.0.1:8080
```

Remove Burp Suite Professional:
```
cat httpx_status-code_results.txt| grep -v "Burp Suite Professional" | anew httpx_status-code_noBurp_results.txt
```

Take screenshots:
```
cat httpx_status-code_noBurp_results.txt | awk '{print $1}' | xargs -I@ sh -c 'gowitness single @'
```
