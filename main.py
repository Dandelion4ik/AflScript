import os

if __name__ == '__main__':
    
    command ='~/workspace/AFLplusplus/afl-fuzz -i ~/workspace/afl-demo/testcases -o ~/workspace/output ~/workspace/afl-demo/main.o @@'
    os.system(command)