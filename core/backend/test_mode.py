def is_test_mode():
    import os
    return os.getenv("TEST_MODE", "false").lower() == "true"
