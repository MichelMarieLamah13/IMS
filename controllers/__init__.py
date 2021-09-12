# == Email Config
import binascii
import hashlib
import os
import random
import string

email = {
    'user': 'lamahmichelmarie@gmail.com',
    'password': 'twzd swvc oltm fhza'
}

# == Emails
text_new_user = {
    'en': """
Account Creation
Hi {name}, your account has been created with the credentials, below
Id: {uid}
Password: {pwd}
Copyright @ 2021, SAT
""",
    'fr': """
Création de Compte
Salut {name}, votre compte a été créé avec les informations ci-dessous
Id: {uid}
Mot de passe: {pwd}
Copyright @ 2021, SAT
"""
}
html_new_user = {
    'en': """
<html>
    <body>
        <h1>Account Creation</h1>
        <div>
            Hi {name}, your account have been created with the credentials, below<br/>
            <strong>Id</strong>: {uid}<br/>
            <strong>Password</strong>: {pwd}<br/>
        </div>
        <div>
            Copyright @ 2021, SAT
        </div>
    </body>
</html>
""",
    'fr': """
<html>
    <body>
        <h1>Création de Compte</h1>
        <div>
            Salut {name}, votre compte a été créé avec les informations ci-dessous<br/>
            <strong>Id</strong>: {uid}<br/>
            <strong>Mot de passe</strong>: {pwd}<br/>
        </div>
        <div>
            Copyright @ 2021, SAT
        </div>
    </body>
</html>
"""}

text_fgpwd_user = {
    'en': """
Update Password
Hi {name}, to update your password, use the otp code below
OTP: {otp}
Copyright @ 2021, SAT
""",
    'fr': """
Modification de mot de passe
Hi {name}, to update your password, use the otp code below
OTP: {otp}
Copyright @ 2021, SAT
"""
}
html_fgpwd_user = {
    'en': """
<html>
    <body>
        <h1>Password Update</h1>
        <div>
            Hi {name}, to update your password, use the otp code below<br/>
            <strong>OTP</strong>: {otp}<br/>
        </div>
        <div>
            Copyright @ 2021, SAT
        </div>
    </body>
</html>
""",
    'fr': """
<html>
    <body>
        <h1>Modification de mot de passe</h1>
        <div>
            Salut {name}, pour modifier votre mot de passe, utiliser le code ci-dessous<br/>
            <strong>CODE</strong>: {otp}<br/>
        </div>
        <div>
            Copyright @ 2021, SAT
        </div>
    </body>
</html>
"""}


# == Functions
def required_field(fieldname, value):
    if not value:
        raise ValueError(f"The field {fieldname} is required")
    else:
        return value


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def get_random_string(length=8):
    # choose from all letters and digits
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
