data = []
for i in range(10):
    data.append(i)
print(f'{"":>3s} {data[0]:>3d} {data[1]:>3d} {data[2]:>3d} {data[3]:>3d} {data[4]:>3d} {data[5]:>3d} {data[6]:>3d} {data[7]:>3d} {data[8]:>3d} {data[9]:>3d}')
separador=str('')#.rjust(3,'-')
print(f'{separador:->44s}')
for i in range(10):
    data = []
    for j in range(10):
        data.append(i*j)
    print(f'{(str(i)+":"):>3s} {data[0]:>3d} {data[1]:>3d} {data[2]:>3d} {data[3]:>3d} {data[4]:>3d} {data[5]:>3d} {data[6]:>3d} {data[7]:>3d} {data[8]:>3d} {data[9]:>3d}')
