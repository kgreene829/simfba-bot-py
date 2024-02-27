input_file = "./logos.js"
output_file = "./logos.py"

with open(input_file, 'r') as js_file, open(output_file, 'w') as py_file:
    py_file.write("logos = {\n")

    for line in js_file:
        if ": " in line:  # Filtering out lines that aren't key-value pairs
            key, value = line.strip().split(": ")
            new_value = value.replace('baseUrl', 'baseurl').replace('`', '"').replace('${baseUrl}', '{baseurl}')
            py_file.write(f"  '{key}': f'{new_value}',\n")

    py_file.write("}\n")