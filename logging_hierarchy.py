import logging

abc_logger = logging.getLogger("a.b.c")
ab_logger = logging.getLogger("a.b")
a_logger = logging.getLogger("a")

print(abc_logger.parent)
print(ab_logger.parent)
print(a_logger.parent)
