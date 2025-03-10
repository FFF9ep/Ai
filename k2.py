import base64

decoded_base64 = "S2FsaWJlcns1ZU11QF95NG45X2QxczNtQnVOeTFrQG5fNGtAbl90M3JiMG45azRyX2QzbjlAbl81ZW5kMXIxbnlAfQo="


def decode_base64(text):
    try:
        decoded = base64.b64decode(text).decode('utf-8')
        return decoded
    except Exception as e:
        return f"Terjadi kesalahan saat decoding Base64: {str(e)}"


final_decoded = decode_base64(decoded_base64)

print("Hasil decoded kedua kalinya:", final_decoded)
