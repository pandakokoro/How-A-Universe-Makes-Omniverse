
import ctypes
import logging
import os
import platform
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Iterable, List, Optional, Set

# Prevents _pycache_ directory creation during execution (keeps repo clean without .gitignore)
sys.dont_write_bytecode = True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [HOSTS-GUARD] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("HostsGuard")

BLOCK_IPV4 = "0.0.0.0"
BLOCK_IPV6 = "::"
BLOCK_MARKER_START = "# --- [HOSTS GUARD MANAGED BLOCK START] ---"
BLOCK_MARKER_END = "# --- [HOSTS GUARD MANAGED BLOCK END] ---"
EOL = "\r\n" if platform.system() == "Windows" else "\n"

# RFC 1123 compliant domain validation pattern
DOMAIN_REGEX = re.compile(
    r"^(?![0-9]+$)(?!-)[a-z0-9-]{1,63}(?<!-)"
    r"(\.(?![0-9]+$)(?!-)[a-z0-9-]{1,63}(?<!-))*$"
)
