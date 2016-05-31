class CryptoMessage(object):

    def __init__(self, plain_text: str, key: str) -> None:

        self.plain_text = plain_text
        self.key = key

    def encrypt(self):
        raise NotImpletedError('Subclasses should implement this!')

    def decrypt(self):
        raise NotImpletedError('Subclasses should implement this!')
