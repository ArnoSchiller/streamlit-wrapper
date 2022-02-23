import setuptools

setuptools.setup(
    name="streamlit_wrapper",
    version="0.0.1",
    author="Arno Schiller",
    author_emaipyl="info@byschiller.de",
    description="Streamlit Wrapper",
    long_description="This package combines various public Streamlit projects and custom components.",
    long_description_content_type="text/plain",
    url="https://github.com/ArnoSchiller/streamlit-wrapper",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.8",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 1.5.1",

        "streamlit-img-label >= 0.1.1",
        "pascal_voc_writer"
    ],
)