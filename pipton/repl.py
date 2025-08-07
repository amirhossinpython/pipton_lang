import sys
from .core import translate

def start_repl():
    print(" Pipton REPL interactive environment | Exit with the 'exit' command'")
    code_lines = []
    while True:
        try:
            line = input(">>> ").strip()
            if line.lower() in ("exit", "quit"):
                print("Exiting the REPL")
                break

            if line == "":
                continue

            code_lines.append(line)
            joined = '\n'.join(code_lines)

            try:
                py_code = translate(joined)
                exec(py_code, globals())
                code_lines = []  # پاک کردن بعد اجرای موفق
            except Exception as e:
                if "بلاک‌ها" in str(e):
                    # یعنی هنوز بلاک کامل نشده
                    continue
                print(f"⛔ erorr: {e}")
                code_lines = []  # پاک کردن بعد ارور
        except KeyboardInterrupt:
            print("\nExit with Ctrl+C")
            break
        except Exception as e:
            print(f"⛔ erorr REPL: {e}")
