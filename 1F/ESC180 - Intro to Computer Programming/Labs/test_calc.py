#%%
import lab02

if __name__ == '__main__':
    lab02.initialize()

    if lab02.get_current_value() == 0:
        print('Test 1 passed')
    else:
        print('Test 1 failed')

    lab02.add(5)
    if lab02.get_current_value() == 5:
        print('Test 2 passed')
    else:
        print('Test 2 failed')
    lab02.store()
    
    lab02.multiply(10)
    if lab02.get_current_value() == 50:
        print('Test 3 passed')
    else:
        print('Test 3 failed')
    
    lab02.divide(2)
    if lab02.get_current_value() == 25.0:
        print('Test 4 passed')
    else:
        print('Test 4 failed')

    lab02.undo()
    if lab02.get_current_value() == 50:
        print('Test 5 passed')
    else:
        print('Test 5 failed')
    
    lab02.recall()
    if lab02.get_current_value() == 5:
        print('Test 6 passed')
    else:
        print('Test 6 failed')

# %%
