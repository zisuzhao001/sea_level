import xarray as xr

# RAPID-MOCHA dataset on NCAR server (example)
url = "https://psl.noaa.gov/thredds/dodsC/Datasets/rapid-mocha/transport_yearmonth.nc"

# Open dataset
ds = xr.open_dataset(url)
print(ds)

# Select AMOC transport variable
amoc = ds['amoc_trans']  # variable name may differ, check ds
amoc_df = amoc.to_dataframe().reset_index()

# Save to CSV
amoc_df.to_csv("amoc_transport.csv", index=False)
print(amoc_df.head())
