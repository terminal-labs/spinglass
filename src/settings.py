from spinglass.derived_settings import APPDIR, SETUPFILEDIR, TESTDIR, MEMTEMPDIR, SITEPACKAGESPATH

NAME = "spinglass"

VERSION = "0.0.8"
PRINT_VERBOSITY = "high"
EXCLUDED_DIRS = [".DS_Store"]
SETUP_NAME = NAME
PROJECT_NAME = SETUP_NAME.replace("_", "").replace("-", "")
EGG_NAME = SETUP_NAME.replace("_", "-")
TEMPDIR = "/tmp"
TEXTTABLE_STYLE = ["-", "|", "+", "-"]
DIRS = [f"{TEMPDIR}/{PROJECT_NAME}"]
MINIMUM_PYTHON_VERSION = (3, 6, 0)
COVERAGERC_PATH = f"{APPDIR}/.coveragerc"
PAYLOADPATH = SITEPACKAGESPATH
