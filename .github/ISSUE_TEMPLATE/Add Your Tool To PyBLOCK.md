def NAMEAPP():
    try:
        clear()
        blogo()
        output = render(
        "TITTLE APP", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('FOLDERAPP'):
            print("...Follow the steps...")
        else:
            os.system("mkdir FOLDERAPP && cd FOLDERAPP && wget YOURAPPGITHUBLINKGZ.gz && tar -xf YOURAPPGZ.gz")
            clear()
            blogo()
            print(output)
        responseC = input("APPPARAMETER1: ")
        responseD = input("APPPARAMETER2: ")
        responseE = input("APPPARAMETER3: ")
        os.system(f"cd FOLDERAPP && ./APP {responseC} {responseD} {responseE}")
        input("\a\nContinue...")
    except:
        pass
