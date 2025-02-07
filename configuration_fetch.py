
# f=open("sample_configuration_file","r")
# print(f.readline(1))

with open("sample_configuration_file") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
    print(lines)