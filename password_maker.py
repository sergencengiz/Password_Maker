import random
import string

def generate_password(length=6):
    # Şifrede kullanılacak karakter setleri (boşluklar hariç) / Character sets to be used in the password (excluding spaces)
    characters = string.ascii_letters + string.digits + string.punctuation.replace(' ', '')
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

password_length = 6  # Şifrenin uzunluğunu 6 olarak belirleyin / Set the password length to 6
generated_password = generate_password(password_length)
print("Oluşturulan Şifre:", generated_password)
