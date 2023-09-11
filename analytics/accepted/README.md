# Accepted

## Analyze .json file(s) from analyze-accepted.py

```jq '. | select(.[].status=="fixed") |= sort_by(.created_at)' all.json```

