# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""Python interface to C++ nonlinear, multidimensional root finding routines"""


from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_rootfind')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_rootfind')
    _rootfind = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_rootfind', [dirname(__file__)])
        except ImportError:
            import _rootfind
            return _rootfind
        try:
            _mod = imp.load_module('_rootfind', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _rootfind = swig_import_helper()
    del swig_import_helper
else:
    import _rootfind
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def setFTolerance(tolf):
    """
    setFTolerance(double tolf)



    Sets the termination threshold for the change in f.  

    """
    return _rootfind.setFTolerance(tolf)

def setXTolerance(tolx):
    """
    setXTolerance(double tolx)



    Sets the termination threshold for the change in x.  

    """
    return _rootfind.setXTolerance(tolx)

def setVectorField(pVFObj):
    """
    setVectorField(PyObject * pVFObj) -> int



    Sets the vector field object.  

    Returns:  

        status (int): 0 if pVFObj = NULL, 1 otherwise.  

    See vectorfield.py for an abstract base class that can be overridden to produce
    one of these objects.  

    """
    return _rootfind.setVectorField(pVFObj)

def findRoots(startVals, iter):
    """
    findRoots(PyObject * startVals, int iter) -> PyObject *



    Performs unconstrained root finding for up to iter iterations  

    Returns:  

        status,x,n (tuple of int, list of floats, int): where status indicates
            the return code, as follows:

                - 0: convergence reached in x
                - 1: convergence reached in f
                - 2: divergence
                - 3: degeneration of gradient (local extremum or saddle point)
                - 4: maximum iterations reached
                - 5: numerical error occurred

            and x is the final point and n is the number of iterations used  

    """
    return _rootfind.findRoots(startVals, iter)

def findRootsBounded(startVals, boundVals, iter):
    """
    findRootsBounded(PyObject * startVals, PyObject * boundVals, int iter) -> PyObject *



    Same as findRoots, but with given bounds (xmin,xmax)  

    """
    return _rootfind.findRootsBounded(startVals, boundVals, iter)

def destroy():
    """
    destroy()



    destroys internal data structures  

    """
    return _rootfind.destroy()
# This file is compatible with both classic and new-style classes.


