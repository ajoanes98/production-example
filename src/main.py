"""Minimal checkout ops stub for the production readiness workshop track."""


def health() -> dict:
    return {"status": "ok", "service": "checkout-ops"}


if __name__ == "__main__":
    print(health())
