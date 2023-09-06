import sys

# Check for the command-line argument
if len(sys.argv) != 2:
    print("Usage: python split_sql_blocks.py input_file.sql")
    sys.exit(1)

input_file_name = sys.argv[1]
fileNameWithoutExt = input_file_name.split('.')[0]
fileNameExt = input_file_name.split('.')[1]

# Read the input file
with open(input_file_name, 'r') as file:
    sql_blocks = file.read().split(';\n/\n')

# Split the SQL blocks into pairs
sql_block_pairs = [sql_blocks[i:i+1000] for i in range(0, len(sql_blocks), 1000)]

# Write each pair of SQL blocks to separate files
for i, pair in enumerate(sql_block_pairs):
    with open(f'{fileNameWithoutExt}_{i + 1}.{fileNameExt}', 'w') as output_file:
        output_file.write(';\n/\n'.join(pair, ))
        output_file.write(';\n/\ncommit;\nexit;\n')

# Process the last pair without appending "/ commit; exit;"
last_pair = sql_block_pairs[-1]
output_file_name = f'{fileNameWithoutExt}_{len(sql_block_pairs)}.{fileNameExt}'
with open(output_file_name, 'w') as output_file:
    output_file.write(';\n/\n'.join(last_pair))
    
    
print("Files extracted successfully.")
