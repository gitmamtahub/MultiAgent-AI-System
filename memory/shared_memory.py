class SharedMemory:
    def __init__(self):
        self.memory_log = []

    def log_event(self, event):
        from datetime import datetime
        event["timestamp"] = datetime.now().isoformat()
        self.memory_log.append(event)

    def get_logs(self):
        return self.memory_log
