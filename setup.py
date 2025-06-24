from setuptools import setup, find_packages

setup(
    name="cyrecon",
    version="1.0.4",
    author="Nikhil Bhor",
    author_email="nikhilbhor201@gmail.com",
    description="Automated AI-powered recon toolkit for subdomains, ports, directories and CVE detection",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mrcoder420/cyrecon",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "tqdm",
        "selenium",
        "fpdf",
        "colorama"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
     'console_scripts': [
        'cyrecon=cyrecon.main:main_menu',  # ← ✅ Correct
    ],
},


)
