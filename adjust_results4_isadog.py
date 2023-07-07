def adjust_results4_isadog(dogfile, results_dic):
    # Read dog names from dogfile and store in a dictionary
    dog_names = {}
    with open(dogfile, 'r') as file:
        for line in file:
            dog_name = line.strip()
            if dog_name not in dog_names:
                dog_names[dog_name] = 1
            else:
                print(f"Warning: Duplicate dog name found: {dog_name}")

    # Adjust the results dictionary to indicate if labels are dogs
    for key in results_dic:
        # Check if pet image label is a dog
        is_dog_label = 1 if results_dic[key][0] in dog_names else 0
        # Check if classifier label is a dog
        is_dog_classifier = 1 if results_dic[key][1] in dog_names else 0
        # Extend the results dictionary with the new values
        results_dic[key].extend([is_dog_label, is_dog_classifier])
