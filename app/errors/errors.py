class KlikBCAError(Exception): pass

class HTTPMethodNotImplementedError(KlikBCAError): pass

class ControllerNotFoundError(KlikBCAError): pass
