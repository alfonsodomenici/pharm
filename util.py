from datetime import date, datetime, time, timedelta

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date, time)):
        return obj.isoformat()
    elif isinstance(obj, timedelta):
        return obj.__str__()
    raise TypeError (f"Type {type(obj)} not serializable")