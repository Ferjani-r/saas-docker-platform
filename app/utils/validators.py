from datetime import datetime, timezone


def calculate_uptime(started_at: str, status: str) -> str:
    if status != "running" or not started_at:
        return "Stopped"

    try:
        # Docker timestamps may include nanoseconds (9 digits)
        if "." in started_at:
            base, rest = started_at.split(".", 1)
            microseconds = rest[:6]  # keep only 6 digits
            timezone_part = rest[rest.find("+"):] if "+" in rest else "+00:00"
            started_at = f"{base}.{microseconds}{timezone_part}"

        start_time = datetime.fromisoformat(started_at)
        now = datetime.now(timezone.utc)

        delta = now - start_time
        seconds = int(delta.total_seconds())

        minutes, sec = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        if days > 0:
            return f"{days}d {hours}h"
        elif hours > 0:
            return f"{hours}h {minutes}m"
        elif minutes > 0:
            return f"{minutes}m {sec}s"
        else:
            return f"{sec}s"

    except Exception:
        return "N/A"


def is_valid_container_name(name: str) -> bool:
    if not name:
        return False

    return name.replace("-", "").replace("_", "").isalnum()
