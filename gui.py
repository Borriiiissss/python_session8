import data_load_save
def user_request():
    
    print (' 1 - find info')
    print (' 2 - add info')    
    print (' 3 - delete info')
    print (' 4 - import info')
    print (' 5 - export info')
    print (' 6 - change info')
    print (' 7 - about salary')
    print (" 8 - about employee's age")
    
    match (int(input(''))):
        case 1:
            data_load_save.find_info()
        case 2:
            data_load_save.add_info()
        case 3:
            data_load_save.delete_info()
        case 4:
            data_load_save.import_info()
        case 5:
            data_load_save.export_info()
        case 6:
            data_load_save.change_info()
        case 7:
            data_load_save.salary_info()
        case 8:
            data_load_save.age_info()
    return

