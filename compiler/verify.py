"""
This is a module that will import the correct DRC/LVS/PEX 
module based on what tools are found. It is a layer of indirection
to enable multiple verification tool support.

Each DRC/LVS/PEX tool should implement the functions run_drc, run_lvs, and
run_pex, repsectively. If there is an error, they should abort and report the errors.
If not, OpenRAM will continue as if nothing happened!
"""

import debug
from globals import OPTS


if OPTS.drc_exe == None:
    pass
elif "calibre" in OPTS.drc_exe:
    from calibre import run_drc
elif "assura" in OPTS.drc_exe:
    from assura import run_drc
elif "magic" in OPTS.drc_exe:
    from magic import run_drc
else:
    debug.warning("Did not find a supported DRC tool.")

if OPTS.lvs_exe == None:
    pass
elif "calibre" in OPTS.lvs_exe:
    from calibre import run_lvs
elif "assura" in OPTS.lvs_exe:
    from assura import run_lvs
elif "netgen" in OPTS.lvs_exe:
    from magic import run_lvs
else:
    debug.warning("Did not find a supported LVS tool.")


if OPTS.pex_exe == None:
    pass
elif "calibre" in OPTS.pex_exe:
    from calibre import run_pex
elif "magic" in OPTS.pex_exe:
    from magic import run_pex
else:
    debug.warning("Did not find a supported PEX tool.")
    
