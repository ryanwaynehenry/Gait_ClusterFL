import pandas as pd

def combine_rows(input_file, output_file):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Prepare a new DataFrame for the output
    combined_rows = []

    # Process in batches of 100 rows
    for start in range(0, len(df), 100):
        batch = df.iloc[start:start+100]
        # Flatten the batch into a single row
        wide_row = batch.values.flatten()
        # Pad the row if it has fewer than 600 columns
        padded_row = list(wide_row) + [None] * (600 - len(wide_row))
        combined_rows.append(padded_row)

    # Create a DataFrame from the combined rows
    output_df = pd.DataFrame(combined_rows)

    # Write to the output CSV file
    output_df.to_csv(output_file, index=False)

# Example usage
combine_rows('serverTestX.csv', 'server/serverTestX.csv')
