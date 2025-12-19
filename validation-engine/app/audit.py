import datetime
import json

AUDIT_LOG = []

def record_audit(event: dict):
    event["timestamp"] = datetime.datetime.utcnow().isoformat()
    AUDIT_LOG.append(event)

def get_audit_log():
    return AUDIT_LOG