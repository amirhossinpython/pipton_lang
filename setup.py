from setuptools import setup, find_packages

setup(
    name='pipton',  # ✔ مطمئن شو که در PyPI این اسم آزاد باشه!
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    
    entry_points={
        'console_scripts': [
            'pipton = pipton.repl:start_repl',        # ✔ REPL اجرا میشه
            'pipton-run = run_pipton:main',            # ✔ اجرای فایل .kod
        ],
    },

    install_requires=[],  # اگه کتابخونه‌هایی استفاده کردی، اینجا بنویس

    author='AmirhosseinPython',
    author_email='amirhossinpython03@gmail.com',
    
    description='A custom language with Persian-flavored syntax and full Python power',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    
    url='https://github.com/amirhossinpython/pipton_lang',  # ✔ عالیه

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Interpreters",
        "Intended Audience :: Developers",
        "Natural Language :: Persian",
    ],

    python_requires='>=3.6',
)
