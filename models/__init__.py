#!/usr/bin/python3
"""Instantiates an object of class FileStorage
BaseModel contractur
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
