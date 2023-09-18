# Unauthenticated Web Testing
Basically test for everything but IDORs (in general)...

Enum
- Look for pages that shouldn't be available to the 'public'
- Check 'HTTP' for every 'HTTPS' route
- Try 403 bypass on anything that returns a 403

Auth
- Look for creds
- Look for API keys in JavaScript chunk files

Injection
- All types of injection testing on every possible input vector

Prototype Pollution
- Hit every endpoint with client-side proto pollution tool called Green_Energy

Misc
- Infrastructure testing
- Abusing hop headers
- host header poisoning
- CORS
- request smuggling
- known CVEs
