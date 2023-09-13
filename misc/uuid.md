# UUID

UUID
UUID.fromString("00000000-0000-0000-0000-000000000000")

Potential 'custom' check for a UUID
https://stackoverflow.com/questions/37320870/is-there-a-uuid-validator-annotation
```
@Target(ElementType.FIELD)
@Constraint(validatedBy={})
@Retention(RUNTIME)
@Pattern(regexp="^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$", message = "Not a valid UUID")
public @interface UUID {
    String message() default "{invalid.uuid}";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}
```
