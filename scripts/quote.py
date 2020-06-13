#!/usr/bin/env python2

import sys, os, random, tempfile, subprocess

path = os.environ.get('CALIBRE_PYTHON_PATH', u'/usr/lib/calibre')
if path not in sys.path:
    sys.path.insert(0, path)

sys.resources_location = os.environ.get('CALIBRE_RESOURCES_PATH', u'/usr/share/calibre')
sys.extensions_location = os.environ.get('CALIBRE_EXTENSIONS_PATH', u'/usr/lib/calibre/calibre/plugins')
sys.executables_location = os.environ.get('CALIBRE_EXECUTABLES_PATH', '/usr/lib/calibre/bin-py2')

from calibre.library import db

db = db('/home/rixx/lib/books').new_api

import pdb; pdb.set_trace()

ids = db.search('languages:"=English" tags:"=state:read"')
book = random.choice(list(ids))
metadata = db.get_metadata(book)
print("Chosen book: {} by {}".format(metadata.title, ", ".join(metadata.authors)))

path = db.format_abspath(book, list(db.format_files(book).keys())[0])
tmp = tempfile.NamedTemporaryFile(suffix=".txt")

print("Converting ...")
subprocess.check_output(["ebook-convert", path, tmp.name])
print("Converted.")

lines = int(subprocess.check_output(["wc", "-l", tmp.name]).split(" ")[0])
line_no = random.randint(0, lines)
subprocess.check_call([os.environ.get("EDITOR", "vim"), "+{}".format(line_no), tmp.name])
tmp.close()
