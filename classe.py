import pandas as pd
class Fusee:
            """To create a rocket item two possibilites
         either the name exist in the database then it is the only argument necessary
         it takes the parameters from the database
         or you want to create a rocket which doesn't exist 
         you have to enter the 19 parameters in the right order
         it returns an error if the name exists and you enter other parameters"""
    def __init__(self, name, data_fusee=[]):


        db = pd.read_csv('rocket_database.csv', sep=',')
        self.config_type = dict(zip(db.columns, range(20)))

        if data_fusee:
            assert(name not in db.Name.values), 'Rocket already in the database'
            assert (len(data_fusee) == 19), 'Some capabilities are missing'
            new_row = dict(zip(db.columns, [name] + data_fusee))
            new_db = db.append(dict([key, str(value)] for key, value in new_row.items()),
                               ignore_index=True)
            new_db.to_csv('rocket_database.csv', sep=',')
        else:
            data_fusee = db.loc[db.Name == name].values[0][1:]

        self.configuration = [name]
        for elt in data_fusee:
            self.configuration.append(elt)
        self.configuration[self.config_type['Name']]


class Badtype(Exception):
    pass

class Badvalue(Exception):
    pass








































