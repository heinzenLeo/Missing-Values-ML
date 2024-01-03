# input your X_train and X_valid data (preferably in that order)
# the code will show you, in detail, everything about columns with nan values
# !notice! you must have pandas and also inspect installed on your coding environment, elements such as pd.Series and .currentframe() are needed
# !warning! X_train and X_valid must be DataFrame type

def nan_columns(X_train, X_valid):
    import pandas as pd
    import inspect
    
    def retrieve_name(var):
        callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
        return [var_name for var_name, var_val in callers_local_vars if var_val is var]

    input1 = retrieve_name(X_train)[0]
    input2 = retrieve_name(X_valid)[0]

    xs = [X_train, X_valid] # getting a list with both X_train and X_valid, so that we're able to run a loop here
    xs_names = [input1, input2] # the actual names of each input (ex: nan_columns(X_valid, X_train) instead of X_train and X_valid)
    cols_with_missing = [] # a list that we'll add columns with nan valus from X_train and X_valid
    z = 0 # just for fancier output

    for i in xs:
        missing_val_count_by_col = i.isnull().sum() # looks column by column
        missing = missing_val_count_by_col[missing_val_count_by_col > 0] # missing is the variable that keeps only what we want: the columns with nan values
        
        if type(missing) != pd.Series:
            print('*error* -->', '|' + xs_names[z] + '|', '--> you may have put a wrong input: only pandas DataFrame types are accepted')
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
            # again, the code above is just for fancier output
    
            print(missing, '\n')
            print('Number of columns with missing values:' , len(missing), '\n', '-------------------------------------------', '\n')
            
            #print(type(missing_val_count_by_col)) type of missing_val_count_by_col == pd.Series
            
            cols_with_missing.append(missing.index) # adding only the columns' names to the list
            
        try: # try and except because there could be no missing values in any column, and in this case, the output would be an error message
            x = cols_with_missing[0] # here we're dividing the cols_with_missing into two parts (cols_with_missing[0] or x, which represents the X_train columns with missing values)
            # x = 1st input
        except:
            print('')
            continue # continue (restarts the loop) so that it looks at the second variable (X_valid_full)
        try:
            v = cols_with_missing[1] # here we're dividing the cols_with_missing into two parts (cols_with_missing[1] or y, which represents the X_valid columns with missing values)
            # v = 2nd input
        except:
            print('')
            continue # continue (restarts the loop), so there will be no error message
        
        difference = x.difference(v) # taking the different elements that are in x but not in y

#'Column:', '|' + o + '|', "from {}, has missing values and it isn't in s%" % (xs_names[0], xs_names[1])
    
        
            # here we're comparing the 1st input (xs_names[0] --> first variable name, xs[0] --> first dataframe (content)) with the 2nd input (xs_names[1] --> second variable name, xs[1] --> second dataframe (content))
            # since differece = x.differece(v) -> x = 1st input / v = 2nd input
            # the same applies to the second loop **
        if len(difference) == 1: # just for fancier output
            for o in difference:
                print(f"Column: |{o}| from {xs_names[0]} has missing values and it is NOT in {xs_names[1]}", '\n')
            
        elif len(difference) > 1:
            list_different_cols = [o for o in difference]
            print(f"{len(difference)} Columns: |{str(list_different_cols)[1:-1]}| from {xs_names[0]} have missing values and they are NOT in {xs_names[1]}", '\n')
    
        difference_2 = v.difference(x) # taking the different elements that are in y but not in x
        # second loop **
        # here you're comparing the 2nd input with the 1st input
        # it works the same as the above loop, but it is just inversed
        
        if len(difference_2) == 1: # just for fancier output, again
            for o in difference_2:
                print(f"Column: |{o}| from {xs_names[1]} has missing values and it is NOT in {xs_names[0]}")
                
        elif len(difference_2) > 1:
            list_different_cols_2 = [o for o in difference_2]
            print(f"{len(difference_2)} Columns: |{str(list_different_cols_2)[1:-1]}| from {xs_names[1]} have missing values and they are NOT in {xs_names[0]}", '\n')
    

        if difference.size == 0 and difference_2.size == 0: # checking if both difference and difference_2 have 0 differences, and if so, it'll print the following output
            print(f"--> Both {xs_names[0]} and {xs_names[1]} have nan values in the same columns")