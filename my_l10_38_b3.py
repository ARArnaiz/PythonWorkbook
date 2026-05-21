
class LogFile:

    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "w")
        # self.file = open(filename, "w") #Also acceptable

text1 = LogFile("test.txt")
text1.file.write("Hello world!\n")
text1.file.close()

class LogFile_c:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "w")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False  # don't suppress exceptions
# Without __exit__, a crash between open() and close() leaks the file handle.
# This is the standard Python pattern for any class that owns a resource.
# Keep self.filename — it costs nothing and pays off the moment the class grows.
# Add __enter__/__exit__ when the spec or exercises introduce context managers
# (likely coming soon in Lerner's progression).

# Usage
with LogFile_c("test4.txt") as log:
    log.file.write("Hello world!\n")
# file is closed automatically here, even if an exception occurs

class LogfileL:
    def __init__(self, filename):
        self.file = open(filename, "w")

text2 = LogfileL("test2.txt")
text2.file.write("Hello world!\n")
text2.file.close()