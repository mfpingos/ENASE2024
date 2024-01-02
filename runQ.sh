#!/bin/bash

# File to store cumulative /usr/bin/time output, row counts, and execution times
OUTPUT_FILE="100_lv2_100.txt"

# Clear previous data in the file
> $OUTPUT_FILE

# Array to store execution times
execution_times=()

# Loop to run the script 100 times
for i in {1..100}
do
    echo "Run number: $i" >> $OUTPUT_FILE

    # Measure execution time in milliseconds and also capture CPU and memory usage
    start_time=$(date +%s%N) # Start time in nanoseconds

    # Execute ARQ and append resource usage to the same file
    /usr/bin/time -a -o $OUTPUT_FILE -f "Run $i\nCPU Usage:\nUser Time: %U seconds\nSystem Time: %S seconds\nTotal Time: %E\nMemory Usage: %M KB" \
    arq --data ./EUROPEANA/europeana_lvl6/100/variety_language_format_type_of_object_rights_theme_folder/unstructured_subfolder/de_subfolder/audio/mp3_subfolder/3d_subfolder/http:/creativecommons.org/licenses/by-nc/3.0/_subfolder/manuscript_subfolder/theme_level_sources.ttl --query europeana_query.sparql > query_output_$i.txt
    
    end_time=$(date +%s%N)   # End time in nanoseconds
    current_execution_time=$(( (end_time - start_time) / 1000000 )) # Current execution time in milliseconds
    execution_times+=($current_execution_time) # Store execution time in array

    # Append execution time to the output file
    echo "Execution time for run $i: ${current_execution_time} milliseconds" >> $OUTPUT_FILE

    # Count the number of rows returned by the query (excluding headers if any)
    row_count=$(tail -n +2 query_output_$i.txt | wc -l)
    echo -e "Run $i: $row_count rows\n" >> $OUTPUT_FILE

    # Clean up query output
    rm query_output_$i.txt
done

# Calculate and display average execution time
total_time=0
for time in "${execution_times[@]}"
do
    total_time=$((total_time + time))
done
average_time=$((total_time / 100))

echo "Average execution time: ${average_time} milliseconds"
echo "Average execution time: ${average_time} milliseconds" >> $OUTPUT_FILE


