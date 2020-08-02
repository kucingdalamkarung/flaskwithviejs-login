from datetime import date, datetime
from passlib.hash import pbkdf2_sha256 as hash_256


class Utils:
    @staticmethod
    def json_serial(obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()

        raise TypeError("Type %s not serializable" % type(obj))

    @staticmethod
    def encrypt_pass(passwd):
        return hash_256.hash(passwd)

    @staticmethod
    def decrypt_pass(passwd, pwd_hash):
        return hash_256.verify(passwd, pwd_hash)
