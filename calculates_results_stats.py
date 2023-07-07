def calculates_results_stats(results_dic):
    # Initialize counts
    n_images = len(results_dic)
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0

    # Calculate counts
    for key in results_dic:
        # Correct dog classification
        if results_dic[key][3] == 1 and results_dic[key][4] == 1:
            n_correct_dogs += 1
        # Correct not-a-dog classification
        elif results_dic[key][3] == 0 and results_dic[key][4] == 0:
            n_correct_notdogs += 1
        # Correct breed classification
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            n_correct_breed += 1

    # Calculate percentages
    pct_correct_dogs = (n_correct_dogs / n_images) * 100 if n_images > 0 else 0
    pct_correct_notdogs = (n_correct_notdogs / n_images) * 100 if n_images > 0 else 0
    pct_correct_breed = (n_correct_breed / n_images) * 100 if n_images > 0 else 0

    # Create results statistics dictionary
    results_stats_dic = {
        'n_images': n_images,
        'n_correct_dogs': n_correct_dogs,
        'n_correct_notdogs': n_correct_notdogs,
        'n_correct_breed': n_correct_breed,
        'pct_correct_dogs': pct_correct_dogs,
        'pct_correct_notdogs': pct_correct_notdogs,
        'pct_correct_breed': pct_correct_breed
    }

    return results_stats_dic
