import zlib
import base64


def test_compress(text):
    code = base64.b64encode(zlib.compress(text.encode("utf-8"),9))
    # code = (zlib.compress(text.encode("utf-8"),9))
    print(code)
    print(len(code), len(text))


test_compress(
    '/Users/Shared/personalbook/roles/The Manager of Projects/Cataloging Completed Projects/Prioritiy Voting System.md'
)
test_compress('hello/'*25)
