import json

galaxies = {}

with open("./simulator/templates/galaxies.data", "r") as file:
    for line in file.readlines():

        if line.startswith('#') or line.startswith("{") or line.startswith("}"):
            continue

        elif line == '':
            continue

        try :
            if line.startswith('Galaxy'):
                galaxie = line.split()[1].replace('"', '').replace(':', '  -----  ')
                galaxies[galaxie] = {}

            elif line.split()[0].startswith('Type'):
                galaxies[galaxie]["Type"] = line.split()[1].replace('"', '')
            
            elif line.split()[0].startswith('RA'):
                galaxies[galaxie]['RA'] = float(line.split()[1])

            elif line.split()[0].startswith('Dec'):
                galaxies[galaxie]['Dec'] = float(line.split()[1])

            elif line.split()[0].startswith('Distance'):
                galaxies[galaxie]['Distance'] = float(line.split()[1])

            elif line.split()[0].startswith('Radius'):
                galaxies[galaxie]['Radius'] = float(line.split()[1])

            elif line.split()[0].startswith('AbsMag'):
                galaxies[galaxie]['AbsMag'] = float(line.split()[1])
        
        except IndexError:
            pass
        
with open("./simulator/templates/galaxies.json", "w") as file :
    json.dump(galaxies, file)        