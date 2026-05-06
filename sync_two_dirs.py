from pathlib import Path
import shutil
import logging
from dataclasses import dataclass, field

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class SyncStats:
    copied: int = 0
    skipped: int = 0
    errors: int = 0

    def __iadd__(self, other: "SyncStats") -> "SyncStats":
        self.copied += other.copied
        self.skipped += other.skipped
        self.errors += other.errors
        return self


def sync_two_dirs(
        dominant_dir: str | Path,
        passive_dir: str | Path,
        ignore_list: set[str] | None = None,
        *,
        _root: bool = True,
) -> SyncStats:
    """Synchronize files from dominant_dir into passive_dir, ignoring any
    file/directory names listed in ignore_list.

    - Files present in dominant_dir are copied to passive_dir (overwriting if
      they already exist).
    - Subdirectories are synced recursively; missing target subdirectories are
      created automatically.
    - Symlinks are skipped to avoid unexpected recursion or dangerous copies.
    - Copy errors are logged and skipped so the rest of the sync can continue.
    - Passive_dir is created automatically if it does not exist.

    :param dominant_dir: Source directory whose contents are authoritative.
    :param passive_dir:  Destination directory to be updated.
    :param ignore_list:  Names (not paths) of files/directories to skip.
    :param _root:        Internal flag; do not pass explicitly. Controls
                         whether top-level logging and summary are emitted.
    :returns:            SyncStats with total counts of copied/skipped/errors.
    :raises ValueError:  If dominant_dir is not a valid directory, or if
                         passive_dir exists but is not a directory, or if
                         passive_dir is a subdirectory of dominant_dir.
    """
    d = Path(dominant_dir).resolve()
    if not d.is_dir():
        raise ValueError(f"dominant_dir '{dominant_dir}' is not a valid directory.")

    p = Path(passive_dir).resolve()
    if p.exists() and not p.is_dir():
        raise ValueError(f"passive_dir '{passive_dir}' exists but is not a directory.")

    # Guard against infinite recursion when passive_dir is inside dominant_dir
    if p.is_relative_to(d):
        raise ValueError(
            f"passive_dir '{p}' is a subdirectory of dominant_dir '{d}'. "
            "This would cause infinite recursion."
        )

    p.mkdir(parents=True, exist_ok=True)

    ignore: set[str] = set(ignore_list) if ignore_list is not None else set()

    if _root:
        logger.info("Syncing '%s' → '%s'", d, p)

    stats = SyncStats()

    for item in d.iterdir():
        if item.name in ignore:
            logger.debug("Skipping ignored item: '%s'", item.name)
            stats.skipped += 1
            continue

        if item.is_symlink():
            logger.warning("Skipping symlink: '%s'", item)
            stats.skipped += 1
            continue

        target = p / item.name

        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            stats += sync_two_dirs(item, target, ignore, _root=False)
        else:
            try:
                action = "Overwriting" if target.exists() else "Copying"
                shutil.copy2(item, target)
                logger.info("%s '%s' → '%s'", action, item.name, target)
                stats.copied += 1
            except OSError as exc:
                logger.error("Failed to copy '%s' to '%s': %s", item, target, exc)
                stats.errors += 1

    if _root:
        logger.info(
            "Sync complete: %d copied, %d skipped, %d error(s).",
            stats.copied, stats.skipped, stats.errors,
        )

    return stats


ignore_list_PythonWorkbook = {".venv", "pyproject.toml", "uv.lock", ".idea", "__pycache__"}
sync_two_dirs("C:/Users/ARA/Projects/PythonWorkbook",
              "C:/Users/ARA/OneDrive/Workspace/Projects/PythonWorkbook",
              ignore_list_PythonWorkbook)

"""qwen2.5-coder:7b - review
The provided code snippet is a Python function `sync_two_dirs` designed to synchronize files from one directory
(`dominant_dir`) into another (`passive_dir`). It handles various scenarios such as ignoring certain files,
copying files and directories, and logging the progress. Below is a detailed review of the code:

### Key Features:
1. **Logging**: The function uses Python's `logging` module to log information about the sync process.
2. **Ignore List**: It allows an optional list of file and directory names to be ignored during the sync.
3. **Symlink Handling**: Symlinks are skipped to avoid infinite recursion or dangerous copies.
4. **Error Handling**: Copy errors are logged, but the sync continues.
5. **Directory Creation**: The function ensures that target directories are created automatically if they do not
exist.

### Code Structure:
1. **Data Class `SyncStats`**:
   - This class is used to keep track of statistics during the sync process (copied files, skipped items, errors).
   - It includes a method `__iadd__` to add two instances of `SyncStats`.

2. **Function `sync_two_dirs`**:
   - **Parameters**: The function takes paths for `dominant_dir`, `passive_dir`, and an optional `ignore_list`.
   - **Validation**: It checks if the directories are valid and prevents infinite recursion.
   - **Directory Creation**: Ensures that the target directory exists.
   - **Iteration**: Iterates over items in the dominant directory, copying or skipping them based on the rules.

### Potential Improvements:
1. **Error Handling**:
   - The current implementation logs errors but continues the sync. Consider adding more robust error handling,
such as retrying operations or stopping the sync if too many errors occur.
2. **Performance**:
   - For large directories, the function may be slow due to the overhead of logging and file copying. Consider
optimizing the function for better performance.
3. **Flexibility**:
   - The `ignore_list` parameter is currently a list of names. Consider making it more flexible to accept patterns
(e.g., using glob or regex).
4. **Security**:
   - Ensure that the function does not allow unintended access to sensitive files by carefully validating paths.

### Example Usage:
The example usage at the end demonstrates how to call the `sync_two_dirs` function with specific parameters,
including an ignore list for a Python project.

```python
ignore_list_PythonWorkbook = [".venv", "pyproject.toml", "uv.lock", ".idea", "__pycache__"]
sync_two_dirs("C:/Users/ARA/Projects/PythonWorkbook", "C:/Users/ARA/OneDrive/Workspace/Projects/PythonWorkbook",
ignore_list_PythonWorkbook)
```

This function is a useful tool for keeping two directories synchronized, especially when working with projects
that need to be shared or backed up."""