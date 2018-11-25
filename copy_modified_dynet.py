from __future__ import print_function
import sys
import dynet_config

HAVE_CUDA = False

_CONF = dynet_config.get()

# Original:
# if '--dynet-viz' in sys.argv:
#     sys.argv.remove('--dynet-viz')
#     from dynet_viz import *
# else:
#     def print_graphviz(**kwarge):
#         print("Run with --dynet-viz to get the visualization behavior.")
#     from _dynet import *
'''
I cannot find any module named _dynet.py in the site-packages folder and I guess it won't be an easy fix...
ERROR MESSAGE:
Traceback (most recent call last):
  File "C:\ProgramData\Miniconda3\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "C:\ProgramData\Miniconda3\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "C:\Users\Nuan Wen\Desktop\cs190I\open-sesame\sesame\targetid.py", line 8, in <module>
    from dynet import *
  File "C:\ProgramData\Miniconda3\lib\site-packages\dynet.py", line 16, in <module>

    from _dynet import *
ModuleNotFoundError: No module named '_dynet'
'''

# CHANGED TO: (at least open-sesame is running)
from dynet_viz import *


__version__ = "2.0.3"

__gitversion__ = "2.1"

# check HAVE_CUDA
if not HAVE_CUDA:
    ERRMSG = 'DyNet was not installed with GPU support. Please see the installation instructions for how to make it possible to use GPUs.'
    if '--dynet-gpu' in sys.argv or '--dynet-gpus' in sys.argv:
        raise RuntimeError(ERRMSG)
    elif '--dynet-devices' in sys.argv:
        if 'GPU' in sys.argv[sys.argv.index('--dynet-devices')+1]:
            raise RuntimeError(ERRMSG)

if _CONF is None:
    init()
else:
    _params = DynetParams()
    _params.from_config(_CONF)
    _params.init()
