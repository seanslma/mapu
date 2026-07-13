from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version('mapu')
except PackageNotFoundError:
    __version__ = '0.0.0'  # Fallback for development
