
def get_resp_codes(filename) -> set:
    with open("../apache_logs.txt") as f:
        return {line.strip().split()[8] for line in f}

print(get_resp_codes("../apache_logs.txt"))

# Here’s what those HTTP response codes mean:
# 200 — OK: the request succeeded.
# 206 — Partial Content: the server returned only part of the resource, usually for range requests.
# 301 — Moved Permanently: the resource has a new permanent URL.
# 304 — Not Modified: the resource hasn’t changed since the client’s cached version.
# 403 — Forbidden: the server understood the request but won’t allow access.
# 404 — Not Found: the requested resource doesn’t exist at that URL.
# 416 — Range Not Satisfiable: the requested byte range can’t be fulfilled.
# 500 — Internal Server Error: the server hit an unexpected problem.
# A quick grouping:
# 2xx = success.
# 3xx = redirects or cache-related responses.
# 4xx = client-side request/access problems.
# 5xx = server-side failures.