from collections import OrderedDict as od

dict = od([('jimil', '14'), ('Simmi', '18')])

dict.update({'jay':"89"})

dict.move_to_end('jay',last = False )

print(dict)
