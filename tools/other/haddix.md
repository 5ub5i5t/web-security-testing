# Tools recommended by Jason Haddix

Application Analysis v1
https://www.youtube.com/watch?v=HmDY7w8AbR4


## Wordlists

assetnote
https://wordlists.assetnote.io/

Download all:
```
wget -r --no-parent -R "index.html*" https://wordlists-cdn.assetnote.io/data/ -nH -e robots=off
```


## Content Discovery

feroxbuster
https://github.com/epi052/feroxbuster

Install (kali:
```
sudo apt update && sudo apt install -y feroxbuster
```

Install (ubuntu):
```
sudo snap install feroxbuster
```

xnLinkFinder
https://github.com/xnl-h4ck3r/xnLinkFinder

Install:
```
git clone https://github.com/xnl-h4ck3r/xnLinkFinder.git
cd xnLinkFinder
sudo python setup.py install
```

## Spidering Tools

gospider: 
https://github.com/jaeles-project/gospider

Install:
```
go install github.com/jaeles-project/gospider@latest
```

hakrawler: 
https://github.com/hakluke/hakrawler

Install:
```
go install github.com/hakluke/hakrawler@latest
```

## Burp Extension

Error Message Check
https://github.com/portswigger/error-message-checks
https://github.com/augustd/burp-suite-error-message-checks

Flow
https://github.com/portswigger/flow

GAP
https://github.com/xnl-h4ck3r/GAP-Burp-Extension

Scavenger
https://github.com/0xDexter0us/Scavenger


