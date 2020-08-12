from Bio import SeqIO
import argparse


def get_cds(gb_file, qual, q_id):

    for record in SeqIO.parse(gb_file, 'genbank'):
        for feature in record.features:
            if feature.type == 'CDS' and qual in feature.qualifiers:
                if feature.qualifiers[qual][0] == q_id:
                    print(feature.qualifiers['protein_id'][0])


def main():
    parser = argparse.ArgumentParser(description='Filter and return specific protein id')
    parser.add_argument('-f', '--file', type=str, required=True, help='genbank file containing seqs')
    parser.add_argument('-q', '--qualifier', type=str, required=True, help='genbank qualifier to filter')
    parser.add_argument('-g', '--gene', type=str, required=True, help='specific qualifier value to find')
    args = parser.parse_args()

    get_cds(args.file, args.qualifier, args.gene)


if __name__ == '__main__':
    main()
