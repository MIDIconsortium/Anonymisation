# Anonymisation

This repository contains scripts to anonymise patient DICOM files using the open-source [pydicom package](https://github.com/pydicom/pydicom)

# Usage

To anonymise a single dicom file and save the resulting dicom file, simply run the following command:

`python run.py -i /path/to/dicom/file -o /path/to/saved/dicom/file`

By default, patient age, date of birth, and sex are retained, but patient name, address, hospital ID and hospital accession number are removed. This can be changed by passing additional boolean arguments to run.py:

--keep_age
--keep_sex
--keep_name
--keep_address
--keep_id
--keep_accession

e.g., `python run.py -i /path/to/dicom/file -o /path/to/saved/dicom/file --keep_age False` etc.

This repository is compatible with python 3.6. See requirements.txt for all prerequisites; you can also install them using the following command:

`pip install -r requirements.txt`

# Coming soon 

We will shortly update the repository to enable anonymisation of entire directories of dicom files e.g., from multiple patients/imaging series etc.
