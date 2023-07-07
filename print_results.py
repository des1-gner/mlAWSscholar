#TODO: 6

def print_results(results_dic, results_stats_dic, model, print_incorrect_dogs=False, print_incorrect_breed=False):
    # Print model architecture
    print(f"\n{'#'*60}")
    print(f"{'#':<22} Summary of Results - {model.upper()} Model {'#':>22}")
    print(f"{'#'*60}")

    # Print overall counts
    print(f"\n{'-'*60}")
    print("         Total Images:", results_stats_dic['n_images'])
    print("       Dog Images:", results_stats_dic['n_correct_dogs'])
    print(" Not-a-Dog Images:", results_stats_dic['n_correct_notdogs'])
    print(f"{'-'*60}")

    # Print percentages
    print(f"\n{'-'*60}")
    print(f"{'% Correct Dogs:':<30}{results_stats_dic['pct_correct_dogs']:.1f}%")
    print(f"{'% Correct Breed:':<30}{results_stats_dic['pct_correct_breed']:.1f}%")
    print(f"{'% Correct "Not-a" Dog:':<30}{results_stats_dic['pct_correct_notdogs']:.1f}%")

    # Optional: Print misclassifications
    if print_incorrect_dogs:
        print(f"{'% Incorrect Dogs:':<30}{100 - results_stats_dic['pct_correct_dogs']:.1f}%")

    if print_incorrect_breed:
        print(f"{'% Incorrect Breed:':<30}{100 - results_stats_dic['pct_correct_breed']:.1f}%")

    print(f"{'-'*60}")

    # Optional: Print misclassified dogs
    if print_incorrect_dogs and results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']:
        print("\nMisclassified Dogs:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print(f"Pet Image: {key:<30}  Classifier Label: {results_dic[key][1]:<26}")

    # Optional: Print misclassified breeds
    if print_incorrect_breed and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print("\nMisclassified Dog Breeds:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print(f"Pet Image: {key:<30}  Classifier Label: {results_dic[key][1]:<26}")
                print(f"    Pet Label: {results_dic[key][0]:<30}  Match: {results_dic[key][2]:<5}")

    print("\n")
