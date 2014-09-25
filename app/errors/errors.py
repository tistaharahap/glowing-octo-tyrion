class GlowingOctoTyrionError(Exception): pass

class HTTPMethodNotImplementedError(GlowingOctoTyrionError): pass

class ControllerNotFoundError(GlowingOctoTyrionError): pass

class NoEnvSpecifiedError(GlowingOctoTyrionError): pass

class ConfigNotFoundError(GlowingOctoTyrionError): pass
