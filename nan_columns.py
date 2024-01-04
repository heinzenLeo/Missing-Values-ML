def nan_columns(X_train, X_valid):
    import pandas as pd
    import inspect
    
    def retrieve_name(var):
        callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
        return [var_name for var_name, var_val in callers_local_vars if var_val is var]

    input1 = retrieve_name(X_train)[0]
    input2 = retrieve_name(X_valid)[0]

    xs = [X_train, X_valid]
    xs_names = [input1, input2]
    cols_with_missing = []
    z = 0 

    for i in xs:
        missing_val_count_by_col = i.isnull().sum()
        missing = missing_val_count_by_col[missing_val_count_by_col > 0]
        
        if type(missing) != pd.Series:
            print('*error* -->', '|' + xs_names[z] + '|', '--> you may have put a wrong input: only pandas DataFrame types are accepted')

            z += 1
            continue
        
        if missing.empty == True:
            if z == 0:
                print('|' + xs_names[z] + '|', '--> (no missing values)', '\n')
                z += 1
            else:
                print('|' + xs_names[z] + '|', '--> (no missing values)')
            continue
        else:
        
            if z == 0:
                #print('\n')
                print('|' + xs_names[z] + '|', '-->', '(columns w/ nan values, number of missing values):', '\n')
            else:
                print('|' + xs_names[z] + '|', '-->', '(columns w/ nan values, number of missing values):', '\n')
            z += 1
    
            print(missing, '\n')
            print('Number of columns with missing values:' , len(missing), '\n', '-------------------------------------------', '\n')
            
            cols_with_missing.append(missing.index)
            
        try:
            x = cols_with_missing[0]
        except:
            print('')
            continue
            
        try:
            v = cols_with_missing[1]
        except:
            print('')
            continue
        
        difference = x.difference(v)

        if len(difference) == 1:
            for o in difference:
                print(f"Column: |{o}| from {xs_names[0]} has missing values and it is NOT in {xs_names[1]}", '\n')
            
        elif len(difference) > 1:
            list_different_cols = [o for o in difference]
            print(f"{len(difference)} Columns: |{str(list_different_cols)[1:-1]}| from {xs_names[0]} have missing values and they are NOT in {xs_names[1]}", '\n')
    
        difference_2 = v.difference(x)
        
        if len(difference_2) == 1:
            for o in difference_2:
                print(f"Column: |{o}| from {xs_names[1]} has missing values and it is NOT in {xs_names[0]}")
                
        elif len(difference_2) > 1:
            list_different_cols_2 = [o for o in difference_2]
            print(f"{len(difference_2)} Columns: |{str(list_different_cols_2)[1:-1]}| from {xs_names[1]} have missing values and they are NOT in {xs_names[0]}", '\n')
    

        if difference.size == 0 and difference_2.size == 0:
            print(f"--> Both {xs_names[0]} and {xs_names[1]} have nan values in the same columns")