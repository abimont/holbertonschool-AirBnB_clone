#!/usr/bin/python3
"""
File ``__init__``
Import Settings
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
