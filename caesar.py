key_lower = 'abcdefghijklmnopqrstuvwxyz'
key_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(text, rot):
    encrypted_message = ''
    turing = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_message = key_lower.find(char)
                encrypted_message += rot
                if encrypted_message < 26:
                    #code = list(alphas_lower.keys())
                    turing += key_lower[encrypted_message]
                else:
                    encrypted_message = encrypted_message % 26
                    #code = list(alphas_lower.keys())
                    turing += key_lower[encrypted_message]
            if char.isupper():
                encrypted_message = key_upper.find(char)
                encrypted_message += rot
                if encrypted_message < 26:
                    #code = list(alphas_upper.keys())
                    turing += key_upper[encrypted_message]
                else:
                    encrypted_message = encrypted_message % 26
                    #code = list(alphas_upper.keys())
                    turing += key_upper[encrypted_message]
        else:
            turing += char
    return turing
