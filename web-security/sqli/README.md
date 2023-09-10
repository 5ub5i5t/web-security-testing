# SQL Injection (sqli)

## Types of SQL Injections:

_[OWASP Web Security Testing Guide]([https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection)_

`Union`: Use with a SELECT statement to combine two queries into a single result or result set.

`Boolean`: Use boolean (true/false) to test certain conditions.

`Error based`: Force the database to create an error to try to gain more information or even to get the results of a query output into an error message.

`Out-of-band`: This is where data is retrieved by using a different channel (i.e., HTTP connection that sends the results to a web server).
    
`Time delay`: Use database commands (i.e. sleep) to test certain conditions based on how long it takes for a query to run.



