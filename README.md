# nucleiHF
This repository provides Skyrme and Relativistic Hartree-Fock calculations for finite nuclei, which are used in the publication:
B. V. Carlson, M. Dutra, O. Lourenço, J. Margueron, 
Low-energy nuclear physics and global neutron star properties,
arXiv:2209.03257 [nucl-th astro-ph.HE]

https://arxiv.org/abs/2209.03257

Optimized for python3.

This README file details how to run the user interactive mode by running the following code: nucleiHF.py

These codes read the following dictionaries:
- data/dict-data.txt
- data/dict-par.txt
- data/dict-res.txt

In the following we details how to run the python3 scripts.

$ python3 nucleiHF.py

  This code reads the dictionaries:
  Data   : dict-data.txt
  Param  : dict-par.txt
  Results: dict-res.txt
  The models are ['SKY', 'RNL', 'RDD']
  The nuclei are ['16O', '34Si', '40Ca', '48Ca', '52Ca', '54Ca', '48Ni', '56Ni',
  '78Ni', '90Zr', '100Sn', '132Sn', '208Pb']
  The code interacts with the user to show results.

More details:

Sets from the following models: ['SKY', 'RNL', 'RDD']

Results for the following nuclei: ['16O', '34Si', '40Ca', '48Ca', '52Ca', '54Ca', '48Ni', '56Ni', '78Ni', '90Zr', '100Sn', '132Sn', '208Pb']

Provide the following data: ['B', 'B_err', 'Rch', 'Rch_err', 'Rp']
