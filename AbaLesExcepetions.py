class AbaloneException(Exception):

    def missing_values(self, msg):
        return ValueError(msg)
