__all__ = [
    "SERVICE_BROKER_IP",
    "SERVICE_BROKER_PORT",
    "SERVICE_BROKER_PATH",
]

SERVICE_BROKER_IP: str = "localhost"
SERVICE_BROKER_PORT: int = 27072
SERVICE_BROKER_PATH: str = f"http://{SERVICE_BROKER_IP}:{SERVICE_BROKER_PORT}"
