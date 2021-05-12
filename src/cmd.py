# vim: set expandtab shiftwidth=4 softtabstop=4:

from chimerax.core.commands import CmdDesc, StringArg
from chimerax.core.commands import run


def capsid_image(session, pdb, path_to_save):
    # All command functions are invoked with ``session`` as its
    # first argument.  Useful session attributes include:
    #   logger: chimerax.core.logger.Logger instance
    #   models: chimerax.core.models.Models instance
    run(session, 'open ' + pdb)
    run(session, 'sym #1 assembly 1')
    run(session, 'surface #2 resolution 10')
    run(session, 'view orient')
    run(session, 'save "' + path_to_save + pdb + '.png"')

# CmdDesc contains the command description.  For the
# "hello" command, we expect no arguments.


capsid_image_desc = CmdDesc( required=[('pdb', StringArg), ('path_to_save', StringArg)])
