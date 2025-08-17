import os

try :
    
    from pipton.repl import start_repl
    from pipton.run_pipton import run_file
except ImportError :
    os.system("python -m pip install pipton")
    
import pipton
from pipton.repl import start_repl
from pipton.run_pipton import run_file

def main():
    while True:
        print("\n=== Pipton CLI Menu ===")
        print("1. Start REPL")
        print("2. Run Pipton file")
        print("Type 'exit' to quit")
        
        command = input("Enter the command: >> ").strip()
        
        if command == "1":
            print("Starting Pipton REPL...")
            try:
                start_repl()
            except Exception as e:
                print(f"Error starting REPL: {e}")
                
        elif command == "2":
            file = input("Enter the filename (e.g., test.pipton):> ").strip()
            if os.path.isfile(file):
                try:
                    run_file(file)
                except Exception as e:
                    print(f"Error running file: {e}")
            else:
                print(f"File '{file}' not found. Please check the filename.")
        
        elif command.lower() == "exit":
            print("Exiting Pipton CLI. Bye!")
            break
        
        else:
            print(f"\nPipton info:\nVersion: {pipton.__version__}\nAuthor: {pipton.__author__}\nEmail: {pipton.__email__}")

if __name__ == '__main__':
    main()
