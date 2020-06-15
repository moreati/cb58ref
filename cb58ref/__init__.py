"""Top-level package for cb58ref."""

__author__ = 'Alex Willmer'
__email__ = 'alex@moreati.org.uk'
__version__ = '0.1.0'

from .base58 import SHA256, b58chars as cb58chars, b58decode, b58encode

__all__ = [
    'cb58chars',
    'cb58checksum',
    'cb58decode',
    'cb58encode',
]


def cb58checksum(v):
    """Return a 32-bit checksum of v, derived from the end of a SHA256 digest.
    """
    h = SHA256.new(v)
    return h.digest()[-4:]


def cb58decode(v):
    """Return the bytes encoded within the CB58 value v.
    """
    result = b58decode(v)
    if result is None:
        return None
    if result[-4:] == cb58checksum(result[:-4]):
        return result[-4:]
    else:
        return None


def cb58encode(v):
    """Return a CB58 encoded representation of v.
    """
    return b58encode(v + cb58checksum(v))
