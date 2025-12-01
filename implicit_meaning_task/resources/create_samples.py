import json, argparse

def extract_n_samples(input_filepath: str, n: int, groups: int) -> None:

    with open(input_filepath, 'r') as infile:
        data = json.load(infile)
    
    sampled_dict = {}
    j = 0
    for i, (k, v) in enumerate(data.items()):
        sampled_dict[i+1] = v
        sampled_dict[i+1]['grouping'] = j
        if (i + 1) % n == 0:
            j += 1
        if len(sampled_dict) >= (groups * n):
            break

    insert_attention_checks(
        sampled_dict,
        attention_checks_filepath="attention_checks.json",
        groups=groups,
        output_filepath="current_samples.json"
        )



def return_dict_with_idx_keys(input_dict: dict) -> dict:
    """
    Convert a dictionary to have stringified integer keys based on the enumeration of its items.
    :param input_dict: The original dictionary.
    :return: A new dictionary with stringified integer keys."""
    return {str(idx+1): value for idx, (key, value) in enumerate(input_dict.items())}

def insert_attention_checks(annotations: dict, attention_checks_filepath: str, groups: int, output_filepath: str) -> None:
    """
    Insert attention check samples into the annotation samples at specified positions.

    :param annotation_filepath: Path to the JSON file containing annotation samples.
    :param attention_checks_filepath: Path to the JSON file containing attention check samples.
    :param output_filepath: Path to save the new JSON file with attention checks inserted.
    """
    

    with open(attention_checks_filepath, 'r') as acf:
        attention_checks = json.load(acf)

    new_samples = {}
    # Insert attention checks into annotations
    for i in list(range(groups)):
        j = 0
        for key, sample in annotations.items():
            if sample["grouping"] == i:
                j += 1
                new_samples[key] = sample
                if j == 15:
                    new_samples[str(i)+"0"] = attention_checks[str(i)+"0"]
                elif j == 30:
                    new_samples[str(i)+"1"] = attention_checks[str(i)+"1"]
    
    new_annotations = return_dict_with_idx_keys(new_samples)

    # Save the new annotations with attention checks
    with open(output_filepath, 'w') as of:
        json.dump(new_annotations, of, indent=4)

if __name__ == "__main__":

    argument_parser = argparse.ArgumentParser(description='Extract samples and insert attention checks.')
    argument_parser.add_argument('input_filepath', type=str, help='Path to the input JSON file containing samples.')
    argument_parser.add_argument('-n', '--n_samples', type=int, default=36, help='Number of samples to extract.')
    argument_parser.add_argument('-g', '--groups', type=int, default=4, help='Number of groups to divide samples into.')   
    args = argument_parser.parse_args()

    if args.n_samples and args.groups:
        extract_n_samples(
            input_filepath=args.input_filepath,
            n=args.n_samples,
            groups=args.groups
        )
    else:
        with open(args.input_filepath, 'r') as af:
            annotations = json.load(af)
        insert_attention_checks(
        annotations,
        attention_checks_filepath="attention_checks.json",
        groups=4,
        output_filepath="current_samples.json"
        )