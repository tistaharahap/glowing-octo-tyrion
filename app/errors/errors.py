class KlikBCAError(Exception): pass

class HTTPMethodNotImplementedError(KlikBCAError): pass

class ControllerNotFoundError(KlikBCAError): pass

class NoEnvSpecifiedError(KlikBCAError): pass

class ConfigNotFoundError(KlikBCAError): pass
