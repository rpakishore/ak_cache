import base64
import pickle
from pathlib import Path
from typing import Any

import ak_file
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Cache:
    def __init__(
        self, filepath: Path = Path("Cache.pkl"), password: str | None = None
    ) -> None:
        self.filepath: Path = Path(str(filepath))
        self.file: ak_file.File = ak_file.File(str(filepath))
        self._create_cache_file(overwrite_existing=False)
        if password:
            self.f = _generate_key(password=password)
        else:
            self.f = None

        self._cache_content: Any = None

    def __str__(self) -> str:
        return f"Cache class located at {self.filepath}"

    def __repr__(self) -> str:
        return f"Cache(filepath={self.filepath})"

    def _create_cache_file(self, overwrite_existing: bool = False) -> Path:
        if (not self.file.exists()) or overwrite_existing:
            with open(self.filepath, "wb"):
                pass
        return self.filepath

    def write(self, data: Any) -> Path:
        self._create_cache_file(overwrite_existing=False)
        byte_data: bytes = pickle.dumps(data)
        if self.f:
            byte_data = self.f.encrypt(byte_data)
        _write_bytes_to_file(data=byte_data, filepath=self.filepath)
        self._cache_content: Any = data
        return self.filepath

    @property
    def value(self):
        if self._cache_content is None:
            self._cache_content: Any = self.read()

        return self._cache_content

    def read(self) -> Any:
        byte_data: bytes = _read_bytes_from_file(self.filepath)
        if self.f:
            byte_data = self.f.decrypt(byte_data)
        try:
            return pickle.loads(byte_data)
        except pickle.UnpicklingError:
            raise Exception(
                "Cannot Unpickle. Are you sure this is not an encrypted cache file?"
            )


def _write_bytes_to_file(data: bytes, filepath: Path) -> None:
    with open(filepath, "wb") as f:
        f.write(data)


def _read_bytes_from_file(filepath: Path) -> bytes:
    with open(filepath, "rb") as f:
        return f.read()


def _generate_key(password: str) -> Fernet:
    """
    Generates a key from the given password and returns it.
    """
    password_bytes = bytes(password, "utf-8")
    salt = b"salt_^h.W#(e6-OHplcig:?6@+((8{_f2skE"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    return Fernet(key)
