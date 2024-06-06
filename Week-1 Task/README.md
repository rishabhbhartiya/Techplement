### Password Generator Documentation

This password generator allows you to create a secure password based on various user-defined preferences, including the use of uppercase letters, lowercase letters, digits, and special characters.

#### Functions

##### `generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True)`

Generates a password of a specified length with the option to include uppercase letters, lowercase letters, digits, and special characters.

**Parameters:**
- `length` (int): The desired length of the password.
- `use_uppercase` (bool): Include uppercase letters if set to `True`. Default is `True`.
- `use_lowercase` (bool): Include lowercase letters if set to `True`. Default is `True`.
- `use_digits` (bool): Include digits if set to `True`. Default is `True`.
- `use_special` (bool): Include special characters if set to `True`. Default is `True`.

**Returns:**
- `str`: A randomly generated password based on the specified criteria.

**Example:**
```python
password = generate_password(12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True)
print(password)
```

#### How to Run the Script

1. Ensure you have Python installed on your system.
2. Copy the script into a Python file (e.g., `password_generator.py`).
3. Run the script using a Python interpreter (e.g., `python password_generator.py`).

#### User Inputs

When you run the script, it will prompt you to enter the following details:

- **Desired password length:** Enter an integer value for the length of the password.
- **Include uppercase letters?** Enter 'y' for Yes or 'n' for No.
- **Include lowercase letters?** Enter 'y' for Yes or 'n' for No.
- **Include digits?** Enter 'y' for Yes or 'n' for No.
- **Include special characters?** Enter 'y' for Yes or 'n' for No.

#### Example Execution

```shell
$ python password_generator.py
Enter desired password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): y
Generated password: A2!b7@c8#D9e
```

#### Error Handling

The script includes basic error handling for invalid inputs:

- If you enter a non-integer value for the password length, it will print an error message: "Invalid input. Please enter a valid integer for password length."

This basic script ensures that at least one character from each selected category is included in the generated password, enhancing its security and randomness.
