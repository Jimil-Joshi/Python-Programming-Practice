test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}


final = dict(zip(test_dict['month'],test_dict['name']))
print(final)
