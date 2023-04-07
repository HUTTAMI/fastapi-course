from passlib.context import CryptContext

pwt_context = CryptContext(schemes=["bcrypt"])

class Hasher():
    @staticmethod
    def verify_password(plin_password,hashed_password):
        return pwt_context.verify(plin_password,hashed_password)
    
    @staticmethod
    def get_password_hash(plain_password):
        return pwt_context.hash(plain_password)