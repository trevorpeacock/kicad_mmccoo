# this file is here to make the external plugins of this repo available from the pcbnew menu.
# to make these plugins available in your kicad, you'll need to have then be available here:
# ~/ubuntu/.kicad_plugins/
#in other worked ~/ubuntu/.kicad_plugins/kicad_mmccooo

# for these particular plugins, you'll need dxfgrabber, numpy, scipy, shapely.
# note that kicad is still on python 2.7.
# sudo python2.7 -m ensurepip --default-pip
#  or
# sudo apt install python-pip


# sudo pip2 install --upgrade pip
# sudo pip2 install dxfgrabber
# sudo pip2 install numpy
# sudo pip2 install scipy
# sudo pip2 install shapely

import pcbnew

print("initializing mmccoo_kicad")

import os

activate_this_file = os.path.join(os.path.dirname(__file__), 'venv/bin/activate_this.py')
exec(compile(open(activate_this_file, "rb").read(), activate_this_file, 'exec'), dict(__file__=activate_this_file))

from . import gen_border
from . import dxf_stuff
from . import place_by_sch
from . import instantiate_footprint
from . import toggle_visibility

# I don't think it's possible to control ratsnets for individual nets.
# It used to be possible, but not since the new connectivity algorithm.
# import ratnest

from . import utils
from . import svg2border
print("done adding mmccoo_kicad")
