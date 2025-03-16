"""Hash service."""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes="bcrypt", deprecated="auto")


class HashService:
    """Hash service."""

    @staticmethod
    def bcrypt(password: str) -> str:
        """Encrypt the password."""
        return pwd_context.hash(password)

    @staticmethod
    def verify(hashed_password: str, plain_password: str) -> bool:
        """Verify if the provided password is correct."""
        return pwd_context.verify(plain_password, hashed_password)
