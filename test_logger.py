from my_customLogger import logger

log = logger.get_logger("test_logger")

log.debug("This is a debug message")
log.info("All systems go")
log.warning("Low disk space")
log.error("Something broke")
log.critical("System crash!")