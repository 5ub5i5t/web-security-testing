# assetfinder - 1

assetfinder -subs-only {TARGET} | httpx -silent -timeout 50 -tech-detect -o httpx_results.txt

---

assetfinder -subs-only {TARGET} | anew assetfinder_results.txt

cat assetfinder_results.txt | httpx -silent -timeout 50 -tech-detect -o httpx_results.txt
or
cat assetfinder_results.txt | httpx -sc -cl -ct -td -timeout 50 -no-color -o httpx_results.txt


Send results to Burp
```
cat assetfinder_output.txt | httpx -silent -timeout 50 -http-proxy http://127.0.0.1:8080
```

Get with status codes (file and burp):
```
cat assetfinder_output.txt | httpx -title -tech-detect -status-code -silent -timeout 100 -o httpx_status-code_results.txt -http-proxy http://127.0.0.1:8080
```

Get tech and save to .txt file
```
cat assetfinder_output.txt | httpx -silent -timeout 50 -tech-detect -o httpx_color_output.txt
```

cat httpx_results.txt | awk '{print $1}'
or
cat httpx_results.txt | awk '{print $1}' | xargs -I@ sh -c 'gowitness single @'
