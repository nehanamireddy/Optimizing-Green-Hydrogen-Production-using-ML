# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from windrose import WindroseAxes
# import seaborn as sns

# # 1) FILE MAPPING BY LOCATION & YEAR
# file_map = {
#     'Austin': {
#         2019: 'austin_2019.xlsx',
#         2020: 'austin_2020.xlsx'
#     },
#     'Corpus Christi': {
#         2019: 'cc_2019_data.xlsx',
#         2020: 'cc_dataa.xlsx'
#     },
#     'Houston': {
#         2019: 'houston_2019.xlsx',
#         2020: 'wrel_dataset.xlsx'
#     }
# }

# # All possible heights in your dataset
# available_heights = [10, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 250, 300, 500, 1000]

# def load_data_no_cache(location, year):
#     """
#     Loads the Excel file for the selected location and year, 
#     creates a timestamp index, sorts, returns DataFrame.
#     (No caching)
#     """
#     file_path = file_map[location][year]
#     df = pd.read_excel(file_path)
#     df['timestamp'] = pd.to_datetime(df[['Year','Month','Day','Hour','Minute']])
#     df = df.set_index('timestamp').sort_index()
#     return df

# def main():
#     st.title("Watt-A-Coog!")
#     st.title("Wind Data Analytics Dashboard")
#     # Sidebar: location, year, height
#     st.sidebar.title("Filters")
#     location = st.sidebar.radio("Select Location", ("Austin", "Corpus Christi", "Houston"))
#     year = st.sidebar.selectbox("Select Year", (2019, 2020))
#     selected_height = st.sidebar.selectbox("Select Turbine Height (m)", available_heights, index=available_heights.index(100))

#     # Load data (no caching)
#     data = load_data_no_cache(location, year)

#     st.write(f"### Data for: **{location}, {year}** at **{selected_height}m**")

#     # Construct column names
#     wind_speed_col = f"wind speed at {selected_height}m (m/s)"
#     wind_dir_col   = f"wind direction at {selected_height}m (deg)"
#     tke_col        = f"turbulent kinetic energy at {selected_height}m (m2/s2)"  # if it exists

#     # Check if columns exist
#     missing_cols = [col for col in [wind_speed_col, wind_dir_col, tke_col] if col not in data.columns]
#     if missing_cols:
#         st.error(f"Missing columns for {location}, {year} at {selected_height}m: {missing_cols}")
#         return

#     # --- Descriptive Statistics ---
#     st.subheader("Descriptive Statistics")
#     st.write("**Wind Speed (m/s)**")
#     st.dataframe(data[wind_speed_col].describe())

#     st.write("**Wind Direction (deg)**")
#     st.dataframe(data[wind_dir_col].describe())

#     if tke_col in data.columns:
#         st.write("**Turbulent Kinetic Energy (m²/s²)**")
#         st.dataframe(data[tke_col].describe())
#     else:
#         st.info("TKE data not available for this height or dataset.")

#     # --- Windrose Plot ---
#     st.subheader("Windrose Plot")
#     fig_windrose = plt.figure(figsize=(8, 8))
#     ax = WindroseAxes.from_ax(fig=fig_windrose)
#     wind_direction = data[wind_dir_col]
#     wind_speed     = data[wind_speed_col]
#     ax.contourf(wind_direction, wind_speed, bins=8, normed=True, cmap=plt.get_cmap('viridis'))
#     ax.set_legend(title="Wind Speed (m/s)", loc="lower right", bbox_to_anchor=(1, 0))
#     st.pyplot(fig_windrose)

#     # --- Diurnal Analysis ---
#     st.subheader("Diurnal Analysis (Hourly Average)")
#     if 'hour' not in data.columns:
#         data['hour'] = data.index.hour

#     diurnal_avg = data.groupby('hour')[wind_speed_col].mean()
#     fig_diurnal, ax_diurnal = plt.subplots(figsize=(10, 4))
#     ax_diurnal.bar(diurnal_avg.index, diurnal_avg.values, color='skyblue')
#     ax_diurnal.set_xlabel("Hour of Day")
#     ax_diurnal.set_ylabel("Avg Wind Speed (m/s)")
#     ax_diurnal.set_title("Diurnal Wind Speed Pattern")
#     st.pyplot(fig_diurnal)

#     # --- Seasonal (Monthly) Analysis ---
#     st.subheader("Seasonal Analysis (Monthly Average)")
#     if 'month' not in data.columns:
#         data['month'] = data.index.month

#     monthly_avg = data.groupby('month')[wind_speed_col].mean()
#     fig_monthly, ax_monthly = plt.subplots(figsize=(10, 4))
#     ax_monthly.bar(monthly_avg.index, monthly_avg.values, color='lightgreen')
#     ax_monthly.set_xlabel("Month")
#     ax_monthly.set_ylabel("Avg Wind Speed (m/s)")
#     ax_monthly.set_title("Monthly Wind Speed Pattern")
#     st.pyplot(fig_monthly)

#     # Optional: Show raw data
#     with st.expander("Show Raw Data"):
#         st.dataframe(data.head(20))

# if __name__ == "__main__":
#     main()
#---------------------------------------------------------------------------------------

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from windrose import WindroseAxes
# import seaborn as sns

# # --- File mapping: adjust file paths as needed ---
# file_map = {
#     'Austin': {
#         2019: 'austin_2019.xlsx',
#         2020: 'austin_2020.xlsx'
#     },
#     'Corpus Christi': {
#         2019: 'cc_2019_data.xlsx',
#         2020: 'cc_dataa.xlsx'
#     },
#     'Houston': {
#         2019: 'houston_2019.xlsx',
#         2020: 'wrel_dataset.xlsx'
#     }
# }

# # List of all available heights (in meters)
# available_heights = [10, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 250, 300, 500, 1000]

# # Function to load data (no caching)
# def load_data(location, year):
#     file_path = file_map[location][year]
#     df = pd.read_excel(file_path)
#     df['timestamp'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])
#     df = df.set_index('timestamp').sort_index()
#     return df

# def main():
#     st.title("Wind Data Analytics Dashboard")
    
#     # Sidebar: Select filters
#     st.sidebar.title("Filters")
#     location = st.sidebar.radio("Select Location", ("Austin", "Corpus Christi", "Houston"))
#     year = st.sidebar.selectbox("Select Year", (2019, 2020))
#     selected_height = st.sidebar.selectbox("Select Turbine Height (m)", available_heights, index=available_heights.index(100))
    
#     # Let user select one or more parameters to analyze
#     parameter_options = ["Wind Speed", "Wind Direction", "TKE"]
#     selected_params = st.sidebar.multiselect("Select Parameters to Analyze", parameter_options, default=["Wind Speed"])
    
#     # Load data for chosen location and year
#     data = load_data(location, year)
    
#     st.write(f"### Data for: {location}, {year} at {selected_height}m")
    
#     # Construct column names dynamically
#     wind_speed_col = f"wind speed at {selected_height}m (m/s)"
#     wind_dir_col   = f"wind direction at {selected_height}m (deg)"
#     tke_col        = f"turbulent kinetic energy at {selected_height}m (m2/s2)"
    
#     # Verify columns exist
#     missing_cols = [col for col in [wind_speed_col, wind_dir_col, tke_col] if col not in data.columns]
#     if missing_cols:
#         st.error(f"Missing columns in the dataset for {location}, {year} at {selected_height}m: {missing_cols}")
#         return
    
#     # --- Descriptive Analysis with Box Plots ---
#     st.subheader("Descriptive Analysis")
#     fig_box, ax_box = plt.subplots(figsize=(10, 5))
#     plot_data = []
#     labels = []
    
#     if "Wind Speed" in selected_params:
#         plot_data.append(data[wind_speed_col])
#         labels.append("Wind Speed (m/s)")
#     if "Wind Direction" in selected_params:
#         plot_data.append(data[wind_dir_col])
#         labels.append("Wind Direction (deg)")
#     if "TKE" in selected_params:
#         plot_data.append(data[tke_col])
#         labels.append("TKE (m²/s²)")
    
#     ax_box.boxplot(plot_data, labels=labels, showfliers=True)
#     ax_box.set_title("Box Plots of Selected Parameters")
#     ax_box.set_ylabel("Values")
#     st.pyplot(fig_box)
    
#     # --- Diurnal Analysis (Hourly Average) ---
#     if "Wind Speed" in selected_params:
#         st.subheader("Diurnal Analysis (Hourly Average - Wind Speed)")
#         if 'hour' not in data.columns:
#             data['hour'] = data.index.hour
#         diurnal_avg = data.groupby('hour')[wind_speed_col].mean()
#         fig_diurnal, ax_diurnal = plt.subplots(figsize=(10, 4))
#         ax_diurnal.bar(diurnal_avg.index, diurnal_avg.values, color='skyblue')
#         ax_diurnal.set_xlabel("Hour of Day")
#         ax_diurnal.set_ylabel("Average Wind Speed (m/s)")
#         ax_diurnal.set_title("Hourly Wind Speed Pattern")
#         st.pyplot(fig_diurnal)
    
#     # --- Seasonal Analysis (Monthly Average) ---
#     if "Wind Speed" in selected_params:
#         st.subheader("Seasonal Analysis (Monthly Average - Wind Speed)")
#         if 'month' not in data.columns:
#             data['month'] = data.index.month
#         monthly_avg = data.groupby('month')[wind_speed_col].mean()
#         fig_monthly, ax_monthly = plt.subplots(figsize=(10, 4))
#         ax_monthly.bar(monthly_avg.index, monthly_avg.values, color='lightgreen')
#         ax_monthly.set_xlabel("Month")
#         ax_monthly.set_ylabel("Average Wind Speed (m/s)")
#         ax_monthly.set_title("Monthly Wind Speed Pattern")
#         st.pyplot(fig_monthly)
    
#     # --- Windrose Plot (only if both Wind Speed and Wind Direction are selected) ---
#     if "Wind Speed" in selected_params and "Wind Direction" in selected_params:
#         st.subheader("Windrose Plot")
#         fig_windrose = plt.figure(figsize=(8, 8))
#         ax = WindroseAxes.from_ax(fig=fig_windrose)
#         ax.contourf(data[wind_dir_col], data[wind_speed_col], bins=8, normed=True, cmap=plt.get_cmap('viridis'))
#         ax.set_legend(title="Wind Speed (m/s)", loc="lower right", bbox_to_anchor=(1, 0))
#         st.pyplot(fig_windrose)
    
#     # --- Option: Toggle Raw Data ---
#     if st.sidebar.checkbox("Show Raw Data", value=False):
#         st.subheader("Raw Data Sample")
#         st.dataframe(data.head(20))
        
# if __name__ == "__main__":
#     main()
#-------------------date below------------


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from windrose import WindroseAxes
# import seaborn as sns
# import datetime

# # --- File mapping: adjust file paths as needed ---
# file_map = {
#     'Austin': {
#         2019: 'austin_2019.xlsx',
#         2020: 'austin_2020.xlsx'
#     },
#     'Corpus Christi': {
#         2019: 'cc_2019_data.xlsx',
#         2020: 'cc_dataa.xlsx'
#     },
#     'Houston': {
#         2019: 'houston_2019.xlsx',
#         2020: 'wrel_dataset.xlsx'
#     }
# }

# # List of all available heights (in meters)
# available_heights = [10, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 250, 300, 500, 1000]

# def load_data(location, year):
#     file_path = file_map[location][year]
#     df = pd.read_excel(file_path)
#     df['timestamp'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])
#     df = df.set_index('timestamp').sort_index()
#     return df

# def main():
#     st.title("Wind Data Analytics Dashboard")
    
#     # Sidebar: Select filters
#     st.sidebar.title("Filters")
#     location = st.sidebar.radio("Select Location", ("Austin", "Corpus Christi", "Houston"))
#     year = st.sidebar.selectbox("Select Year", (2019, 2020))
#     selected_height = st.sidebar.selectbox("Select Turbine Height (m)", available_heights, index=available_heights.index(100))
    
#     # Let user select one or more parameters to analyze
#     parameter_options = ["Wind Speed", "Wind Direction", "TKE"]
#     selected_params = st.sidebar.multiselect("Select Parameters to Analyze", parameter_options, default=["Wind Speed"])
    
#     # Load data for chosen location and year
#     data = load_data(location, year)
#     st.write(f"### Data for: {location}, {year} at {selected_height}m")
    
#     # Construct column names dynamically
#     wind_speed_col = f"wind speed at {selected_height}m (m/s)"
#     wind_dir_col   = f"wind direction at {selected_height}m (deg)"
#     tke_col        = f"turbulent kinetic energy at {selected_height}m (m2/s2)"
    
#     # Verify columns exist
#     missing_cols = [col for col in [wind_speed_col, wind_dir_col, tke_col] if col not in data.columns]
#     if missing_cols:
#         st.error(f"Missing columns in the dataset for {location}, {year} at {selected_height}m: {missing_cols}")
#         return
    
#     # --- Descriptive Analysis with Box Plots ---
#     st.subheader("Descriptive Analysis")
#     fig_box, ax_box = plt.subplots(figsize=(10, 5))
#     plot_data = []
#     labels = []
    
#     if "Wind Speed" in selected_params:
#         plot_data.append(data[wind_speed_col])
#         labels.append("Wind Speed (m/s)")
#     if "Wind Direction" in selected_params:
#         plot_data.append(data[wind_dir_col])
#         labels.append("Wind Direction (deg)")
#     if "TKE" in selected_params:
#         plot_data.append(data[tke_col])
#         labels.append("TKE (m²/s²)")
    
#     ax_box.boxplot(plot_data, labels=labels, showfliers=True)
#     ax_box.set_title("Box Plots of Selected Parameters")
#     ax_box.set_ylabel("Values")
#     st.pyplot(fig_box)
    
#     # --- Diurnal Analysis (Hourly Average) ---
#     if "Wind Speed" in selected_params:
#         st.subheader("Diurnal Analysis (Hourly Average - Wind Speed)")
#         if 'hour' not in data.columns:
#             data['hour'] = data.index.hour
#         diurnal_avg = data.groupby('hour')[wind_speed_col].mean()
#         fig_diurnal, ax_diurnal = plt.subplots(figsize=(10, 4))
#         ax_diurnal.bar(diurnal_avg.index, diurnal_avg.values, color='skyblue')
#         ax_diurnal.set_xlabel("Hour of Day")
#         ax_diurnal.set_ylabel("Average Wind Speed (m/s)")
#         ax_diurnal.set_title("Hourly Wind Speed Pattern")
#         st.pyplot(fig_diurnal)
    
#     # --- Seasonal Analysis (Monthly Average) ---
#     if "Wind Speed" in selected_params:
#         st.subheader("Seasonal Analysis (Monthly Average - Wind Speed)")
#         if 'month' not in data.columns:
#             data['month'] = data.index.month
#         monthly_avg = data.groupby('month')[wind_speed_col].mean()
#         fig_monthly, ax_monthly = plt.subplots(figsize=(10, 4))
#         ax_monthly.bar(monthly_avg.index, monthly_avg.values, color='lightgreen')
#         ax_monthly.set_xlabel("Month")
#         ax_monthly.set_ylabel("Average Wind Speed (m/s)")
#         ax_monthly.set_title("Monthly Wind Speed Pattern")
#         st.pyplot(fig_monthly)
    
#     # --- Windrose Plot (only if both Wind Speed and Wind Direction are selected) ---
#     if "Wind Speed" in selected_params and "Wind Direction" in selected_params:
#         st.subheader("Windrose Plot")
#         fig_windrose = plt.figure(figsize=(8, 8))
#         ax = WindroseAxes.from_ax(fig=fig_windrose)
#         ax.contourf(data[wind_dir_col], data[wind_speed_col], bins=8, normed=True, cmap=plt.get_cmap('viridis'))
#         ax.set_legend(title="Wind Speed (m/s)", loc="lower right", bbox_to_anchor=(1, 0))
#         st.pyplot(fig_windrose)
    
#     # --- Time vs. Wind Speed (Line Plot with Date Range) ---
#     if "Wind Speed" in selected_params:
#         st.subheader("Time vs. Wind Speed (Line Plot)")
#         # Let user pick a date range
#         # We'll get the min/max date from the dataset to define a sensible range
#         min_date = data.index.min().date()
#         max_date = data.index.max().date()
        
#         st.write("Select a start and end date to visualize wind speed over time.")
#         date_range = st.date_input("Select Date Range", [min_date, min_date], min_value=min_date, max_value=max_date)
        
#         # Ensure the user picks exactly 2 dates (start, end)
#         if len(date_range) == 2:
#             start_date, end_date = date_range
#             if start_date > end_date:
#                 st.warning("Start date must be before end date.")
#             else:
#                 # Filter data by the chosen date range
#                 data_range = data.loc[str(start_date):str(end_date)]
                
#                 if not data_range.empty:
#                     fig_line, ax_line = plt.subplots(figsize=(10, 5))
#                     ax_line.plot(data_range.index, data_range[wind_speed_col], marker="o", linestyle="-", color="blue", label=f"{selected_height}m Wind Speed")
#                     ax_line.set_title(f"Wind Speed at {selected_height}m from {start_date} to {end_date}")
#                     ax_line.set_xlabel("Time")
#                     ax_line.set_ylabel("Wind Speed (m/s)")
#                     plt.xticks(rotation=45)
#                     ax_line.legend()
#                     st.pyplot(fig_line)
#                 else:
#                     st.warning("No data in this date range.")
    
#     # --- Option: Toggle Raw Data ---
#     if st.sidebar.checkbox("Show Raw Data", value=False):
#         st.subheader("Raw Data Sample")
#         st.dataframe(data.head(20))

# if __name__ == "__main__":
#     main()

#---------------------date and time below---------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes
import seaborn as sns
import datetime

# --- File mapping: adjust file paths as needed ---
file_map = {
    'Austin': {
        2019: 'austin_2019.xlsx',
        2020: 'austin_2020.xlsx'
    },
    'Corpus Christi': {
        2019: 'cc_2019_data.xlsx',
        2020: 'cc_dataa.xlsx'
    },
    'Houston': {
        2019: 'houston_2019.xlsx',
        2020: 'wrel_dataset.xlsx'
    }
}

# List of all available heights (in meters)
available_heights = [10, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 250, 300, 500, 1000]

def load_data(location, year):
    file_path = file_map[location][year]
    df = pd.read_excel(file_path)
    df['timestamp'] = pd.to_datetime(df[['Year','Month','Day','Hour','Minute']])
    df = df.set_index('timestamp').sort_index()
    return df

def main():
    st.title("Watt-A-Coog")
    st.title("Wind Data Analytics Dashboard")
    
    # Sidebar: Select filters
    st.sidebar.title("Filters")
    location = st.sidebar.radio("Select Location", ("Austin", "Corpus Christi", "Houston"))
    year = st.sidebar.selectbox("Select Year", (2019, 2020))
    selected_height = st.sidebar.selectbox("Select Turbine Height (m)", available_heights, index=available_heights.index(100))
    
    # Let user select one or more parameters to analyze
    parameter_options = ["Wind Speed", "Wind Direction", "TKE"]
    selected_params = st.sidebar.multiselect("Select Parameters to Analyze", parameter_options, default=["Wind Speed"])
    
    # Load data
    data = load_data(location, year)
    st.write(f"### Data for: {location}, {year} at {selected_height}m")
    
    # Construct column names
    wind_speed_col = f"wind speed at {selected_height}m (m/s)"
    wind_dir_col   = f"wind direction at {selected_height}m (deg)"
    tke_col        = f"turbulent kinetic energy at {selected_height}m (m2/s2)"
    
    # Check columns
    missing_cols = [col for col in [wind_speed_col, wind_dir_col, tke_col] if col not in data.columns]
    if missing_cols:
        st.error(f"Missing columns in the dataset for {location}, {year} at {selected_height}m: {missing_cols}")
        return
    
    # --- Descriptive Analysis with Box Plots ---
    st.subheader("Descriptive Analysis")
    fig_box, ax_box = plt.subplots(figsize=(10, 5))
    plot_data = []
    labels = []
    
    if "Wind Speed" in selected_params:
        plot_data.append(data[wind_speed_col])
        labels.append("Wind Speed (m/s)")
    if "Wind Direction" in selected_params:
        plot_data.append(data[wind_dir_col])
        labels.append("Wind Direction (deg)")
    if "TKE" in selected_params:
        plot_data.append(data[tke_col])
        labels.append("TKE (m²/s²)")
    
    ax_box.boxplot(plot_data, labels=labels, showfliers=False)
    ax_box.set_title("Box Plots of Selected Parameters")
    ax_box.set_ylabel("Values")
    st.pyplot(fig_box)
    
    # --- Diurnal Analysis (Hourly Average) ---
    if "Wind Speed" in selected_params:
        st.subheader("Diurnal Analysis (Hourly Average - Wind Speed)")
        if 'hour' not in data.columns:
            data['hour'] = data.index.hour
        diurnal_avg = data.groupby('hour')[wind_speed_col].mean()
        fig_diurnal, ax_diurnal = plt.subplots(figsize=(10, 4))
        ax_diurnal.bar(diurnal_avg.index, diurnal_avg.values, color='skyblue')
        ax_diurnal.set_xlabel("Hour of Day")
        ax_diurnal.set_ylabel("Average Wind Speed (m/s)")
        ax_diurnal.set_title("Hourly Wind Speed Pattern")
        st.pyplot(fig_diurnal)
    
    # --- Seasonal Analysis (Monthly Average) ---
    if "Wind Speed" in selected_params:
        st.subheader("Seasonal Analysis (Monthly Average - Wind Speed)")
        if 'month' not in data.columns:
            data['month'] = data.index.month
        monthly_avg = data.groupby('month')[wind_speed_col].mean()
        fig_monthly, ax_monthly = plt.subplots(figsize=(10, 4))
        ax_monthly.bar(monthly_avg.index, monthly_avg.values, color='lightgreen')
        ax_monthly.set_xlabel("Month")
        ax_monthly.set_ylabel("Average Wind Speed (m/s)")
        ax_monthly.set_title("Monthly Wind Speed Pattern")
        st.pyplot(fig_monthly)
    
    # --- Windrose Plot ---
    if "Wind Speed" in selected_params and "Wind Direction" in selected_params:
        st.subheader("Windrose Plot")
        fig_windrose = plt.figure(figsize=(8, 8))
        ax = WindroseAxes.from_ax(fig=fig_windrose)
        ax.contourf(data[wind_dir_col], data[wind_speed_col], bins=8, normed=True, cmap=plt.get_cmap('viridis'))
        ax.set_legend(title="Wind Speed (m/s)", loc="lower right", bbox_to_anchor=(1, 0))
        st.pyplot(fig_windrose)
    
    # --- Time vs. Wind Speed (with Date+Time Range) ---
    if "Wind Speed" in selected_params:
        st.subheader("Time vs. Wind Speed (Line Plot)")
        
        # We find the earliest and latest timestamps
        min_timestamp = data.index.min()
        max_timestamp = data.index.max()
        
        # Default start is min_timestamp, default end is min_timestamp (so user can pick both)
        st.write("Select start and end date/time to visualize wind speed over time.")
        
        # Start
        start_date = st.date_input("Start Date", value=min_timestamp.date(), min_value=min_timestamp.date(), max_value=max_timestamp.date())
        start_time = st.time_input("Start Time", value=datetime.time(min_timestamp.hour, min_timestamp.minute))
        
        # End
        end_date = st.date_input("End Date", value=min_timestamp.date(), min_value=min_timestamp.date(), max_value=max_timestamp.date())
        end_time = st.time_input("End Time", value=datetime.time(min_timestamp.hour, min_timestamp.minute))
        
        # Combine date & time into datetime
        start_dt = datetime.datetime.combine(start_date, start_time)
        end_dt = datetime.datetime.combine(end_date, end_time)
        
        if start_dt > end_dt:
            st.warning("Start datetime must be before end datetime.")
        else:
            data_range = data.loc[start_dt:end_dt]
            
            if not data_range.empty:
                fig_line, ax_line = plt.subplots(figsize=(10, 5))
                ax_line.plot(data_range.index, data_range[wind_speed_col],
                             marker="o", linestyle="-", color="blue",
                             label=f"{selected_height}m Wind Speed")
                ax_line.set_title(f"Wind Speed at {selected_height}m from {start_dt} to {end_dt}")
                ax_line.set_xlabel("Time")
                ax_line.set_ylabel("Wind Speed (m/s)")
                plt.xticks(rotation=45)
                ax_line.legend()
                st.pyplot(fig_line)
            else:
                st.warning("No data in this selected range.")
    
    # --- Show Raw Data ---
    if st.sidebar.checkbox("Show Raw Data", value=False):
        st.subheader("Raw Data Sample")
        st.dataframe(data.head(20))

if __name__ == "__main__":
    main()
