from setuptools import find_packages, setup

setup(
    name="TeleMedicineApp",
    version="0.1.0",
    author="Prasoon Pathak",
    author_email="prasoon7pathak@gmail.com",
    description="A telemedicine application with chatbot, multilingual support, and low-bandwidth optimization",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/TeleMedicineApp",  # replace with your repo
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "sentence-transformers==2.2.0",
        "langchain",
        "flask",
        "pypdf",
        "python-dotenv",
        "pinecone-client[grpc]",   # ✅ correct way (PyPI package is pinecone-client, not pinecone)
        "langchain-pinecone",
        "langchain-community",
        "langchain-openai",
        "langchain-experimental",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
