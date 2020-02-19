class STATUS:
    """
    TODO: make the constant truly constants
    """
    OCCUPIED = "occupied"
    EMPTY = "empty"

    OUT_OF_ORDER = "spoilt"

    @staticmethod  # static method does not need self thingy
    def checkStatusValid(status: str) -> bool:
        """Check status validity"""
        status = status.strip().lower()
        if status == STATUS.EMPTY:
            return True
        elif status == STATUS.OCCUPIED:
            return True
        elif status == STATUS.OUT_OF_ORDER:
            return True
        else:
            return False
