from .core import translate

def run_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
        py_code = translate(code)
        exec(py_code, globals())
    except Exception as e:
        print(f"⛔ خطا در اجرای کد:", e)
