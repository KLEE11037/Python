line = '2'*77 + '7'*22
while '727' in line or '777' in line or '222' in line:
    if '222' in line:
        line = line.replace('222', '7')
    else:
        if '777' in line:
            line = line.replace('777', '7')
        else:
            line = line.replace('727', '2')
print(line)