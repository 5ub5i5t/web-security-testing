# jq - 1

```
jq '.[].id' target_assets.json | sort | uniq | sed -e 's/^"//' -e 's/"$//' | anew jq_id_output.txt
```
- json to jq
- get specific item from json
- sort
- uniq
- remove double quotes
- anew to new txt

```
cat jq_id_output.txt | awk '{print "/resource/"$1".json"}' | anew meg_paths_resource.txt
```
- use the list of id from above
- awk a custom string that uses the id
- add to meg_paths_resource.txt


Create full paths:
```
cat jq_id_output.txt | awk '{print "https[TARGET]/resource/"$1".json"}' | anew full_paths_resource.txt
```

Find '200' responses with information:
```
cat full_paths_resource.txt| httpx -sc -cl -ct -td -mc 200 -timeout 50
```

Find '200' and output endpoints only:
```
cat full_paths_resource.txt| httpx -mc 200 -timeout 50 | anew httpx_200_output.txt
```

Convert to 'paths' for meg:
```
cat httpx_200_output.txt | awk '{ FS = "/" }; {print "/"$4"/"$5}' | anew httpx_200_paths_output.txt
```

meg:
```
meg --verbose httpx_200_paths_output.txt meg_hosts.txt
```
