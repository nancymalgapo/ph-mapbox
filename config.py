import os

from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """ Base config """
    DOWNLOADS_FOLDER = str(Path.home() / "Downloads")
    FILES_FOLDER = "files"
    TEMPLATES_FOLDER = "templates"
