import os

print(os.cpu_count())

try:
    import nose
    print(nose.__version__)
except ImportError:
    pass
