
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set(style="whitegrid")
output_dir = "analysis_results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def load_data():
    print("Loading data...")
    # Load first chunk of each
    bio_path = "data/biometric/api_data_aadhar_biometric/api_data_aadhar_biometric_0_500000.csv"
    demo_path = "data/demographic/api_data_aadhar_demographic/api_data_aadhar_demographic_0_500000.csv"
    enrol_path = "data/enrolment/api_data_aadhar_enrolment/api_data_aadhar_enrolment_0_500000.csv"

    df_bio = pd.read_csv(bio_path)
    df_demo = pd.read_csv(demo_path)
    df_enrol = pd.read_csv(enrol_path)
    
    # Parse dates with correct format dd-mm-yyyy based on the file view
    df_bio['date'] = pd.to_datetime(df_bio['date'], format='%d-%m-%Y', errors='coerce')
    df_demo['date'] = pd.to_datetime(df_demo['date'], format='%d-%m-%Y', errors='coerce')
    df_enrol['date'] = pd.to_datetime(df_enrol['date'], format='%d-%m-%Y', errors='coerce')
    
    return df_bio, df_demo, df_enrol

def analyze_enrolment(df):
    print("Analyzing Enrolment...")
    
    # 1. Total Enrolments by Age Group
    total_0_5 = df['age_0_5'].sum()
    total_5_17 = df['age_5_17'].sum()
    total_18_plus = df['age_18_greater'].sum()
    
    # Pie Chart
    plt.figure(figsize=(8, 8))
    labels = ['0-5 Years', '5-17 Years', '18+ Years']
    sizes = [total_0_5, total_5_17, total_18_plus]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Distribution of Aadhaar Enrolments by Age Group')
    plt.savefig(f"{output_dir}/enrolment_age_pie_chart.png")
    plt.close()
    
    # 2. Top 10 States for Enrolment
    df['total_enrolment'] = df['age_0_5'] + df['age_5_17'] + df['age_18_greater']
    state_enrol = df.groupby('state')['total_enrolment'].sum().sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x=state_enrol.values, y=state_enrol.index, palette="viridis")
    plt.title('Top 10 States by Total Enrolment')
    plt.xlabel('Total Enrolments')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_10_states_enrolment.png")
    plt.close()

    return state_enrol

def analyze_updates(df_bio, df_demo):
    print("Analyzing Updates...")
    
    # Compare Biometric vs Demographic Total Volume
    total_bio = df_bio['bio_age_5_17'].sum() + df_bio['bio_age_17_'].sum()
    total_demo = df_demo['demo_age_5_17'].sum() + df_demo['demo_age_17_'].sum()
    
    plt.figure(figsize=(8, 6))
    plt.bar(['Biometric', 'Demographic'], [total_bio, total_demo], color=['#FF5733', '#C70039'])
    plt.title('Comparison of Update Volumes: Biometric vs Demographic')
    plt.ylabel('Count')
    plt.savefig(f"{output_dir}/updates_comparison_bar.png")
    plt.close()
    
    # Age group split for Biometric
    bio_5_17 = df_bio['bio_age_5_17'].sum()
    bio_17_plus = df_bio['bio_age_17_'].sum()
    
    plt.figure(figsize=(6, 6))
    plt.pie([bio_5_17, bio_17_plus], labels=['5-17 Years', '17+ Years'], autopct='%1.1f%%', colors=['#FFC300', '#DAF7A6'])
    plt.title('Biometric Updates by Age Group')
    plt.savefig(f"{output_dir}/biometric_updates_pie.png")
    plt.close()

def identify_trends_and_anomalies(df_enrol):
    print("Identifying Trends...")
    # Time Series of Enrolments
    daily_enrol = df_enrol.groupby('date')['total_enrolment'].sum()
    
    plt.figure(figsize=(12, 6))
    plt.plot(daily_enrol.index, daily_enrol.values, marker='o', linestyle='-', color='b')
    plt.title('Daily Enrolment Trend')
    plt.xlabel('Date')
    plt.ylabel('Enrolments')
    plt.grid(True)
    plt.savefig(f"{output_dir}/enrolment_time_trend.png")
    plt.close()
    
    # Anomaly: Find district with highest enrolment in a single day
    max_enrol_row = df_enrol.loc[df_enrol['total_enrolment'].idxmax()]
    print(f"ANOMALY_MAX_ENROL: District {max_enrol_row['district']} in {max_enrol_row['state']} saw {max_enrol_row['total_enrolment']} enrolments on {max_enrol_row['date'].date()}")

def main():
    df_bio, df_demo, df_enrol = load_data()
    
    analyze_enrolment(df_enrol)
    analyze_updates(df_bio, df_demo)
    identify_trends_and_anomalies(df_enrol)
    
    print("Analysis Complete. Images saved to analysis_results.")

if __name__ == "__main__":
    main()
