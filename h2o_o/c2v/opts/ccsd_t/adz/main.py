import optavc
options = { 
    'program': 'psi4',
    'template_file_path': 'template.dat',
    'energy_regex': r'Stephenergy (-\d*.\d*)',
    'time_limit': '6-20:00:00',
    'queue': 'batch',
    'max_force_g_convergence': 1e-7,
    'nslots': '12',
    'memory': '5GB',
    'name':'h2o'
}
optavc.run_optavc('OPT', options)

