import os

class Config(object):
  
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
