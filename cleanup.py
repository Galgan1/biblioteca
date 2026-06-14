import os
import shutil
import tempfile
from pathlib import Path

target = os.environ.get("BOOK_SKILL_WORKDIR", Path(tempfile.gettempdir()) / "book_skill_work")
try:
    shutil.rmtree(target, ignore_errors=True)
    print(f"Cleaned up {target}")
except Exception as e:
    print(e)
