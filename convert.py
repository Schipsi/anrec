import csv
import json

# Open the CSV
f = open( 'data.csv', 'rU' )
# Change each fieldname to the appropriate field name.
reader = csv.DictReader( f, fieldnames = ( "nom","adresse","lattitude","longitude", "id","image" ))
# Parse the CSV into JSON
out = json.dumps( [ row for row in reader ] )
print "JSON parsed!"
# Save the JSON
f = open( 'archi-strasbourg.json', 'w')
f.write(out)
print "JSON saved!"
