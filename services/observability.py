import logging

logger = logging.getLogger('sehatsaathi')
logger.setLevel(logging.INFO)

def log_event(event_type: str, **kwargs):
    logger.info({'event': event_type, **kwargs})
