

#TODO: 0 (Timing Code)
# Oisin
# 07/07/2023

from time import time, sleep

start_time = time()

sleep(75)

end_time = time()

tot_time = end_time - start_time

## Prints overall runtime in format hh:mm:ss
print("\nTotal Elapsed Runtime:", str( int( (tot_time / 3600) ) ) + ":" +
          str( int(  ( (tot_time % 3600) / 60 )  ) ) + ":" + 
          str( int(  ( (tot_time % 3600) % 60 ) ) ) ) 

sleep()

#TODO: 1 (Command Line Arguments)
# Oisin
# 07/07/2023




pet_labels = get_pet_labels(in_args.dir)

classify_images(in_args.dir, pet_labels, in_args.arch)

adjust_results4_isadog(in_args.dogfile, pet_labels)

results_stats = calculates_results_stats(pet_labels)
