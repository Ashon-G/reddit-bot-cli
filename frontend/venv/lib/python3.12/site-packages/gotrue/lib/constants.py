from typing import Any, Dict


GOTRUE_URL = "http://localhost:9999"
AUDIENCE = ""
DEFAULT_HEADERS: Dict[str, str] = {}
EXPIRY_MARGIN = 60 * 1000
STORAGE_KEY = "supabase.auth.token"
COOKIE_OPTIONS: Dict[str, Any] = {
    "name": "sb:token",
    "lifetime": 60 * 60 * 8,
    "domain": "",
    "path": "/",
    "sameSite": "lax",
}
