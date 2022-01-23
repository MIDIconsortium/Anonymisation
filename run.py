import argparse
import anonymisation
import pydicom as dcm

def str2bool(v):
    return v.lower() in ("true", "1")

if __name__ == '__main__':
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="DICOM Anonymisation"
    )

    parser.add_argument(
        "-i",
        type=str,
        default=None,
        help="Input path",
    )

    parser.add_argument(
        "-o",
        type=str,
        default=None,
        help="Output path",
    )

    parser.add_argument(
        "--keep_age",
        type=str2bool,
        default=True,
        help="Whether to retain patient age",
    )

    parser.add_argument(
        "--keep_dob",
        type=str2bool,
        default=True,
        help="Whether to retain patient date of birth",
    )

    parser.add_argument(
        "--keep_name",
        type=str2bool,
        default=False,
        help="Whether to retain patient name",
    )

    parser.add_argument(
        "--keep_address",
        type=str2bool,
        default=False,
        help="Whether to retain patient address",
    )

    parser.add_argument(
        "--keep_sex",
        type=str2bool,
        default=True,
        help="Whether to retain patient sex",
    )

    parser.add_argument(
        "--keep_id",
        type=str2bool,
        default=False,
        help="Whether to retain patient ID",
    )

    parser.add_argument(
        "--keep_accession",
        type=str2bool,
        default=False,
        help="Whether to retain patient accession number",
    )


    args = parser.parse_args()
    
    DCM = dcm.dcmread(args.i)
    
    if not args.keep_age and hasattr(DCM, 'PatientAge'):
        DCM.PatientAge = 'anon'

    if not args.keep_dob and hasattr(DCM, 'PatientBirthDate'):
        DCM.PatientBirthDate = 'anon'

    if not args.keep_address and hasattr(DCM, 'PersonAddress'):
        DCM.PersonAddress = 'anon'

    if not args.keep_sex and hasattr(DCM, 'PatientSex'):
        DCM.PatientSex = 'anon'

    if not args.keep_id and hasattr(DCM, 'PatientID'):
        DCM.PatientID = 'anon'

    if not args.keep_accession and hasattr(DCM, 'AccessionNumber'):
        DCM.AccessionNumber = 'anon'

    if not args.keep_name and hasattr(DCM, 'PatientName'):
        DCM.PatientName = 'anon'

    dcm.dcmwrite(args.o, DCM)



    

