from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="cyrecon",
    version="1.0.8",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "cyrecon": ["models/model.onnx"],  # ✅ include model
    },
    install_requires=[
        "requests",
        "tqdm",
        "selenium",
        "fpdf",
        "colorama",
        "onnxruntime",
        "tldextract",
        "numpy"
    ],
    entry_points={
        'console_scripts': [
            'cyrecon=cyrecon.main:main_menu',  # ✅ Full path
        ],
    },
)
