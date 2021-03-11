import optavc
cfour_grad_regex = r"\s*Molecular\s*gradient\s*-+\s*([A-Z]+\s#[0-9]+\s[xyz]\s*-?\d+\.\d+\s*)+"
options = { 
    'program': 'cfour@2.0~mpi',
    'template_file_path': 'template.dat',
    'energy_regex': r'\s*Total\sCCSDT\senergy\s\[au\]:\s*(-?\d*\.\d*)',
    'gradient_regex': cfour_grad_regex,
    'time_limit': '26-20:00:00',
    'dertype': 'gradient',
    'queue': 'batch_30d',
    'max_force_g_convergence': 1e-7,
    'nslots': '12',
    'memory': '40GB'
}
optavc.run_optavc('OPT', options)
