from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

setup(
    name="meu_pacote_processamento_imagens", # Escolha um nome único
    version="0.0.1",
    author="Seu Nome",
    author_email="seu_email@email.com",
    description="Pacote para processamento de imagens (Desafio de Projeto)",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu_usuario/seu_repositorio", # Link do seu GitHub
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy",
        "scikit-image>=0.16.1"
    ],
    python_requires='>=3.8',
)