import sys, os

def main():
    filename = sys.argv[1]
    f=open(filename,'w')
    f.write('')
    f.close()
    print("[+] Finished running. Accidentally deleted everything.")

if __name__ == "__main__":
    main()