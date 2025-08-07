# from pipton.runner import run_file
# import sys

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python run_pipton.py <filename.kod>")
#     else:
#         run_file(sys.argv[1])

# from pipton.runner import run_file
# import sys

# def main():
#     if len(sys.argv) < 2:
#         print("⚠️ لطفاً مسیر فایل را بدهید.")
#         return
#     run_file(sys.argv[1])

# if __name__ == "__main__":
#     main()
# run_pipton.py

import sys
from pipton.runner import run_file

def main():
    if len(sys.argv) != 2:
        print("❗ لطفاً مسیر فایل را بدهید")
        return

    filepath = sys.argv[1]
    
    # اگر بخوای فقط .piton بپذیره:
    if not filepath.endswith((".piton",".pipton")):
        print(" Only files with the .piton extension are supported.")
        return

    run_file(filepath)

if __name__ == '__main__':
    main()
