# REPLACE WITH FILE TO CLEAN
FILE = "13b_14infinite.csv"

# Open the report file
report = open( "reports/" + FILE, "r" )

# Get the lines of the file
text = report.read()
lines = text.splitlines()

# Define an array for the output
newlines = []

# Clean the lines
for l in range( len( lines ) ):
	# Skip the first 2 lines
	if l > 2:
		# Split the CSV line
		line = lines[ l ].split( "," )
		# Disregard any malformed lines
		if len( line ) == 6:
			name = line[ 0 ].strip()
			folder = line[ 1 ].strip()
			result = line[ 2 ].lower()
			# Only report files with differences
			if result.find( "identical" ) == -1:
				if result.find( "folder" ) == -1:
					name += "\n"
					if len( folder ) == 0:
						newlines.append( name )
					else:
						newlines.append( folder + "\\" + name )

# Sort the output
newlines.sort()

# Write the cleaned file
clean = open( "txt/" + FILE[ 0 : -4 ] + ".txt", "w" )
clean.writelines( newlines )

# Properly close the files
report.close()
clean.close()