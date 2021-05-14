# vim: set expandtab shiftwidth=4 softtabstop=4:

from chimerax.core.commands import CmdDesc, StringArg
from chimerax.core.commands import run
from chimerax.core.commands import all_objects
from numpy.linalg import norm
# from chimerax.core.commands import measure


def capsid_image(session, pdb, path_to_save):
    # All command functions are invoked with ``session`` as its
    # first argument.  Useful session attributes include:
    #   logger: chimerax.core.logger.Logger instance
    #   models: chimerax.core.models.Models instance
    run(session, 'open ' + pdb)
    run(session, 'sym #1 assembly 1 copies true')
    run(session, 'close #1')  # close pdb so that it doesn't interfere in calculations

    # lattice alignment courtesy of Meghan
    # run(session, 'hkcage 1 0')
    #modelCenter = run(session, 'measure center #2')  # measuring center of model
    # cageCenter = run(session, 'measure center #3')  # measuring center of cage
    # center of mass measurement from ChimeraX tutorial
    atoms = all_objects(session).atoms  # getting atom list
    coords = atoms.scene_coords  # getting atom coords
    modelCenter = coords.mean(axis=0)  # calculate center of mass
    print(modelCenter)
    if modelCenter.any:
        print('Aligning Models')
        run(session, 'hkcage 1 0')
        modelX, modelY, modelZ = modelCenter
        run(session, 'move x ' + str(-1*modelX) + ' coordinateSystem #1 models #2')  # adjust x coordinates
        run(session, 'move y ' + str(-1 * modelY) + ' coordinateSystem #1 models #2')  # adjust y coordinates
        run(session, 'move z ' + str(-1 * modelZ) + ' coordinateSystem #1 models #2')  # adjust z coordinates
        run(session, 'close #3')
    else:
        print('Models Already Aligned')

    atoms = all_objects(session).atoms  # getting atom list
    coords = atoms.scene_coords  # getting atom coords
    radius = norm(coords,axis=1).max()
    run(session, 'hkcage 1 0 alpha hexagonal-dual radius ' + str(radius))

    #run(session, 'surface #2 resolution 10')
    #run(session, 'view orient')
    #run(session, 'save "' + path_to_save + pdb + '.png"')

# CmdDesc contains the command description.  For the
# "hello" command, we expect no arguments.


capsid_image_desc = CmdDesc( required=[('pdb', StringArg), ('path_to_save', StringArg)])
