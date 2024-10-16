from setuptools import setup

setup(
    name="llmner",
    version="0.1.0",
    description="# LLMNER: Named Entity Recognition without training data",
    url="https://github.com/plncmm/llmner",
    author="PLN@CMM",
    author_email="fabian.villena@uchile.cl",
    license="BSD 2-clause",
    packages=["llmner"],
    install_requires=[
        "openai",
        "langchain-openai",
        "langchain",
        "nltk",
        "tqdm",
        "setuptools",
    ],
    python_requires=">=3.10",
    extras_require={"dev": ["ipykernel"]},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
