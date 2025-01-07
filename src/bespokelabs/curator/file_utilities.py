# https://stackoverflow.com/questions/845058/how-to-get-the-line-count-of-a-large-file-cheaply-in-python
# https://stackoverflow.com/a/68385697
def _file_gen(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)


# Instead of requiring counting lines, we can store metadata file that has the number of requests in each file
def count_lines(filename):
    f = open(filename, "rb")
    f_gen = _file_gen(f.raw.read)
    return sum(buf.count(b"\n") for buf in f_gen)