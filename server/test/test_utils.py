import unittest
from libs.utils import Utils

class UtilsTest(unittest.TestCase):
    def test_verity_passwd(self):
        isTrue = Utils.decrypt_pass('fkm1396', '$pbkdf2-sha256$29000$PmeMESKEEOI85xzDWMsZQw$xgcduZr/aDwwWdbnbNF.vYZs23wdVfpbNXp6qdzk3.U')
        assert isTrue == True