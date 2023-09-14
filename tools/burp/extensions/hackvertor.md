# Hackvertor (Professional Extension)
https://portswigger.net/bappstore/65033cbd2c344fbabe57ac060b5dd100

```
Hackvertor is a tag-based conversion tool that supports various escapes and encodings including HTML5 entities, hex, octal, unicode, url encoding etc.

    It uses XML-like tags to specify the type of encoding/conversion used.
    You can use multiple nested tags to perform conversions.
    Tags can also have arguments allowing them to behave like functions.
    It has an auto decode feature allowing it to guess the type of conversion required and automatically decode it multiple times.
    Multiple tabs
    Character set conversion
```

GitHub:
https://github.com/hackvertor/hackvertor

Example Raw Payload:

`1 UNION SELECT username || '~' || OR password FROM users`

Hackvertor encoding:

`<@hex_entities>1 UNION SELECT username || '~' || OR password FROM users <@/hex_entities>`

