from chimerax.core.commands import run

run(session,'open 2xgk')
run(session,'sym #1 assembly 1')
run(session,'save \'2xgk.png\' ')
