''' Rocket object implementing the modelisation of rockets '''
class Rocket():
    #info : year, country, mission
    #spec : Sn, height, lift_off_mass, payload_mass, si_length, si_diameter, thurst, lsp, m0, mp
    
    def __init__(self, name, info, spec):
        self.name = name
        self.info = info
        self.spec = spec
        
    ''' accessors '''
        
    def get_name(self):
        return self.name
    
    def get_info(self):
        return self.info
        
    def get_spec(self):
        return self.spec
        
    def one_stage(self):
        return True if self.spec[0] == 1 else False
        
''' Check if a Rocket object has physically consistent properties '''
def rocket_consistence(name, info, spec):
	return (spec[0] >= spec[3] + spec[9]) and spec[7] > spec[8] and (spec[9] == 0 or (spec[10] > 0 and spec[11] > 0 and spec[12] > 0 and spec[13] > 0 and spec[14] > 0 and spec[13] > spec[14]))
	
''' Return the list of names of a list of Rockets '''
def get_names(rl):
    rl_names = []
    for i in range(0, len(rl)):
        rl_names.append(rl[i].get_name())
    
    return rl_names
