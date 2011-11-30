"""Provides an object representing the current 'version' or 'release'
of Py as a whole.  Individual classes, such as the shell, filling and
interpreter, each have a revision property based on the CVS Revision."""

__author__ = "Patrick K. O'Brien <pobrien@orbtech.com>"
__cvsid__ = "$Id: version.py 63480 2010-02-14 05:34:39Z RD $"
__revision__ = "$Revision: 63480 $"[11:-2]

VERSION = '0.9.8'