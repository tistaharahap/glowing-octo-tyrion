class CoreModel(object):

    def __init__(self, **kwargs):
        for (k, v) in kwargs.iteritems():
            if not hasattr(self, k):
                raise KeyError('This model has no attribute called %s' % k)

            setattr(self, k, v)