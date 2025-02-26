# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///

from __future__ import annotations

import shutil
import tarfile
import urllib.request
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from http.client import HTTPResponse


def main() -> None:
    url = "https://files.pythonhosted.org/packages/64/65/af6d57da2cb32c076319b7489ae0958f746949d407109e3ccf4d115f147c/cattrs-24.1.2.tar.gz"
    name_with_version = "cattrs-24.1.2"
    name = "cattrs"

    downloads_dir = Path("downloads")
    expected_dir = downloads_dir / name

    response: HTTPResponse
    with TemporaryDirectory() as temp_dir:
        with (
            urllib.request.urlopen(url) as response,
            tarfile.open(fileobj=response, mode="r:gz") as tar,
        ):
            tar.extractall(temp_dir, filter="data")

        predicted_dir = Path(temp_dir, name_with_version)
        if not predicted_dir.is_dir():
            raise FileNotFoundError

        if expected_dir.exists():
            shutil.rmtree(expected_dir)

        expected_dir.parent.mkdir(parents=True, exist_ok=True)
        predicted_dir.rename(expected_dir)

    print(f"Downloaded {name_with_version} to {expected_dir}")


if __name__ == "__main__":
    main()
