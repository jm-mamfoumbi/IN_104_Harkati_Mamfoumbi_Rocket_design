class Rocket():
    #info : year, country, mission
    #spec : Sn, height, lift_off_mass, payload_mass, si_length, si_diameter, thurst, lsp, m0, mp
    
    def __init__(self, name, info, spec):
        self.name = name
        self.info = info
        self.spec = spec
        
    def get_name(self):
        return self.name
    
    def get_info(self):
        return self.info
        
    def get_spec(self):
        return self.spec
        
    def one_stage(self):
        return True if self.spec[0] == 1 else False
        
def rocket_consistence(name, info, spec):
   	return True
    
def get_names(rl):
    rl_names = []
    for i in range(0, len(rl)):
        rl_names.append(rl[i].get_name())
    
    return rl_names
