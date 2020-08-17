from pysimm import system, lmps, forcefield
from pysimm.apps.random_walk import random_walk_tacticity
from pysimm.models.monomers.dreiding.ps_tacticity import monomer as PS_tacticity

def run(test=False):
    # we'll make a polystyrene monomer from the pysimm models database
    A = PS_tacticity()
    
    # we'll instantiate a Dreiding forcefield object for use later
    f = forcefield.Dreiding()
    
    # the monomers do not have any charges, so we will derive partial charges using the gasteiger algorithm
    A.apply_charges(f, charges='gasteiger')
    
    # the buckingham potential isn't great at small distances, and therefore we use the LJ potential while growing the polymer
    A.pair_style = 'lj/cut'
    
    # run the polymer random walk tacticity method with 10 total repeat units
    polymer = random_walk_tacticity(A, 100, forcefield=f,capped=True,tacticity='isotactic',errorChecking=True)

    # write a few different file formats
    polymer.write_xyz('polymer.xyz')
    polymer.write_yaml('polymer.yaml')
    polymer.write_lammps('polymer.lmps')
    polymer.write_chemdoodle_json('polymer.json')
    
if __name__ == '__main__':
    run()
