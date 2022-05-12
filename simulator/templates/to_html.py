import json

with open('./simulator/templates/galaxies.json') as json_file:
    galaxies = json.load(json_file)

my_text = ''

for galaxie in galaxies:
    my_text += f'''                <tr>
                        <td>{galaxie}</td>
                        <td>{galaxies[galaxie]['Type']}</td>
                        <td>{galaxies[galaxie]['RA']}</td>
                        <td>{galaxies[galaxie]['Dec']}</td>
                        <td>{galaxies[galaxie]['Distance']}</td>
                        <td>{galaxies[galaxie]['Radius']}</td>
                        <td>{galaxies[galaxie]['AbsMag']}</td>
                    </tr>
'''

with open('./simulator/templates/html.txt', 'w') as file :
    file.write(my_text)