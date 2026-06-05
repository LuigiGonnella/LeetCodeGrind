# Maximum number of Characters that can be removed

- Given a string `abade` denoting a machine, the type of the machine is its first character `a` and last character `e`. So in this case, the type is `ae`.
- In one operation, you can remove as many characters as you want from either the start or the end of the string, as long as the type doesn't change.
- For example, for the string `abade`, we can remove `ab` from start to form `ade` which still has type `ae`.
- A string `a` has type `aa`.
- Return the maximum number of characters that can be removed while keeping the type same.