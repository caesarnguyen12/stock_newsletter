from .Model import Model




class UserModel(Model):
    ALLOWED = {
        "email": str,
        "isValidated": bool
    }
