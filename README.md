# istutor
Imaging Spectroscopy Tutorial Materials

This is a sequence of hands-on lab experiences using open source code for imaging spectrometer data analysis.  They introduce the basic concepts behind these instruments, and provide practical experience in visualization, atmospheric correction, and surface property estimation with rigorous uncertainty propagation. 

Course exercises are conducted and submitted as notebook documents. They also rely on the open-source ISOFIT codebase for atmospheric correction. We suggest the WISER project for visualization capability similar to that provided in the ENVI interface.  Consider first getting the following dependencies:

- Python 3.8 with numpy/scipy and scikit-image libraries.  We recommend the anaconda distribution for an easy installation.  It is available at https://www.anaconda.com.
- Project Jupyter (i.e. jupyter notebooks). This comes with the anaconda installation, and will be needed to run the exercises.
- The Isofit python library.  It is easiest to install this library using the pip package manager, which comes bundled with the anaconda distribution.  From the command line (Mac OS) or anaconda prompt (Windows OS), type “pip install isofit” and the library will be downloaded automatically.  Alternatively, you can clone the github repository at https://github.com/isofit/isofit
- Visual C++ runtime (Windows only). This is needed to run the core ISOFIT functions, and can be downloaded at: https://aka.ms/vs/16/release/vc_redist.x64.exe 

Finally, there are a few large binary files that you will need for certain exercises, and are not stored in the repository due to their size.  These are currently posted to ftp://popo.jpl.nasa.gov/pub/DThompson/istutor/ but the location may change in the future.

