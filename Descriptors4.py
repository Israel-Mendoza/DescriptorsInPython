from datetime import datetime


class UTCTime:

    def __get__(self, instance, owner):
        """
        Returns the descriptor instance if called from a class.
        Returns the current UTC datetime in ISO format if called
            from a class instance.
        """
        if instance is None:
            return self
        else:
            return datetime.utcnow().isoformat()


class Logger:

    current_time = UTCTime()


logger = Logger()

print(type(Logger.current_time))
print(type(logger.current_time))
