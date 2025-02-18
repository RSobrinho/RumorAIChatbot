def is_timeout(slot_value):
    if slot_value == 'EXTERNAL: EXTERNAL_reminder':
        return True
    return False


def deactivate_by_timeout():
    return {"requested_slot": None, "was_timeout": True}