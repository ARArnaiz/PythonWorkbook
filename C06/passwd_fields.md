The `/etc/passwd` file is a colon-delimited (`:`) text file with **7 fields** per line. Here they are in order:

| # | Field | Description |
|---|-------|-------------|
| 1 | **Username** | The login name (e.g., `root`, `reuven`) |
| 2 | **Password** | Historically the password, now typically `x` (meaning the actual password is stored in `/etc/shadow`) or `*` (account disabled/no login) |
| 3 | **UID** | User ID — a numeric identifier. `0` = root/superuser |
| 4 | **GID** | Primary Group ID — numeric identifier of the user's default group |
| 5 | **GECOS / Comment** | Free-form info field, often the user's full name and contact info (e.g., `Reuven M. Lerner,,,`) |
| 6 | **Home Directory** | Absolute path to the user's home directory (e.g., `/home/reuven`) |
| 7 | **Shell** | The user's default login shell (e.g., `/bin/bash`). `/usr/sbin/nologin` or `/bin/false` means the account cannot be used for interactive login |

### Example line breakdown

```
reuven:x:1001:1001:Reuven M. Lerner,,,:/home/reuven:/bin/bash
  │     │  │    │         │                  │            │
  │     │  │    │         │                  │            └─ Shell
  │     │  │    │         │                  └─ Home directory
  │     │  │    │         └─ GECOS (full name / comment)
  │     │  │    └─ GID
  │     │  └─ UID
  │     └─ Password placeholder
  └─ Username
```


> **Note:** The GECOS field is sometimes empty (you'll just see `::` in the line), and the commas within it traditionally separated sub-fields like full name, office, phone number — though these are rarely used today.