def classify_images(images_dir, results_dic, model):
    for filename in results_dic:
        # Concatenate images_dir with the filename to get the full path
        image_path = os.path.join(images_dir, filename)

        # Use the classifier function to get the classifier label
        classifier_label = classifier(image_path, model)

        # Convert labels to lowercase and strip whitespace
        pet_label = results_dic[filename][0].lower().strip()
        classifier_label = classifier_label.lower().strip()

        # Check if pet label matches classifier label
        if pet_label in classifier_label:
            # Labels match
            results_dic[filename].extend([classifier_label, 1])
        else:
            # Labels don't match
            results_dic[filename].extend([classifier_label, 0])
