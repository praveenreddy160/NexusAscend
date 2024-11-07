def encrypt(original_text, shift_amount):
  """
  Encrypts a string using the Caesar cipher.

  Args:
    original_text: The text to be encrypted.
    shift_amount: The number of positions to shift each letter.

  Returns:
    The encrypted text.
  """
  encrypted_text = ""
  for char in original_text:
    if char.isalpha():  # it checks if it is only alphabets
      start = ord('a') if char.islower() else ord('A') #  this will get the numerical postion of the a small and capital from ascii table
      shifted_char = chr((ord(char) - start + shift_amount) % 26 + start) # we will get ord(char) from ascii table then minus with start variable number
    else:
      shifted_char = char  # Keep non-letters unchanged
    encrypted_text += shifted_char
  return encrypted_text

# Get user input
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift amount: "))

encrypted_text = encrypt(text, shift)
print("The encrypted text is:", encrypted_text) 