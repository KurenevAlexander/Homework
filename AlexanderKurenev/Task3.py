from string import ascii_lowercase


class Crypto:
    def __init__(self, key_word):
        self.__coder, self.__decoder = self.create_code_tables(key_word)

    @staticmethod
    def create_code_tables(key_word):
        if not key_word.isalpha():
            raise TypeError("Bad operand type for create_code_tables()")
        code = {}
        decode = {}
        letter_code = 97
        for i in key_word.lower() + ascii_lowercase:
            if i not in decode:
                decode[i] = chr(letter_code)
                code[chr(letter_code)] = i
                letter_code += 1
        return code, decode

    def encode(self, encode_string):
        out = []
        for i in encode_string:
            if i.isalpha():
                if i.isupper():
                    out.append(self.__coder[i.lower()].upper())
                else:
                    out.append(self.__coder[i])
            else:
                out.append(i)
        return ''.join(out)

    def decode(self, decode_string):
        out = []
        for i in decode_string:
            if i.isalpha():
                if i.isupper():
                    out.append(self.__decoder[i.lower()].upper())
                else:
                    out.append(self.__decoder[i])
            else:
                out.append(i)
        return ''.join(out)


cipher = Crypto('crypto')
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))

