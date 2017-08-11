#!/usr/bin/env python
"""Description: 
Setup script for Haystack -- Epigenetic Variability and Transcription Factor Motifs Analysis Pipeline
@status:  beta
@version: $Revision$
@author:  Luca Pinello
@contact: lpinello@jimmy.harvard.edu
"""
from setuptools import setup

def main():

    setup(
        version="0.5.0",
        name="haystack_bio",
        include_package_data=True,
        packages=["haystack"],
        package_dir={'haystack': 'haystack'},
        package_data={'haystack': ['./haystack_data']},
        entry_points={
            "console_scripts": ['haystack_pipeline = haystack.haystack_pipeline_CORE:main',
                                'haystack_hotspots =  haystack.haystack_hotspots_CORE:main',
                                'haystack_motifs = haystack.haystack_motifs_CORE:main',
                                'haystack_tf_activity_plane = haystack.haystack_tf_activity_plane_CORE:main',
                                'haystack_download_genome = haystack.haystack_download_genome_CORE:main',
                                'haystack_run_test = haystack.haystack_common:run_testdata']
        },
        description="Epigenetic Variability and Transcription Factor Motifs Analysis Pipeline",
        maintainer= 'Luca Pinello , Rick Farouni',
        maintainer_email='lpinello@jimmy.harvard.edu, tfarouni@mgh.harvard.edu',
        author='Luca Pinello, Rick Farouni',
        author_email='lpinello@jimmy.harvard.edu, tfarouni@mgh.harvard.edu',
        url='http://github.com/lucapinello/Haystack',
        classifiers=[
            'Development Status :: 5 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
            'Programming Language :: Python',
        ],
        install_requires=[]
    )

if __name__ == '__main__':
    print("Installing Package")
    main()
   # print("Copying Data")
   # copy_haystack_data()