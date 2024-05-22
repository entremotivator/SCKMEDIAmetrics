import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Sample Data
data = {
    "followers": 18.4,
    "quality_audience": 9.2,
    "followers_growth": 1.2,
    "engagement_rate": 4.5,
    "authentic_engagement": 32.5,
    "most_recent_post": "Promoting New Album Release",
    "global_rank": 54,
    "top_countries": {"USA": 50, "Canada": 10, "UK": 15, "Germany": 8, "France": 7, "Australia": 10},
    "age_gender": {"18-24 Male": 30, "18-24 Female": 25, "25-34 Male": 20, "25-34 Female": 15, "35-44 Male": 5, "35-44 Female": 5},
    "ethnicity": {"African American": 50, "Caucasian": 30, "Hispanic": 10, "Asian": 7, "Other": 3},
    "languages": {"English": 80, "Spanish": 10, "French": 5, "German": 3, "Other": 2},
    "estimated_reach": {"organic": (1.5, 2.5), "paid": (0.5, 1.0)},
    "estimated_impressions": 12.5,
    "audience_interests": {"Music": 50, "Fashion": 20, "Sports": 15, "Tech": 10, "Travel": 5},
    "household_income": {"<$30K": 20, "$30K-$50K": 30, "$50K-$70K": 25, "$70K-$100K": 15, ">$100K": 10},
    "education_level": {"High School": 30, "Associate Degree": 20, "Bachelor's Degree": 35, "Master's Degree": 10, "PhD": 5},
    "marital_status": {"Single": 60, "Married": 30, "Divorced": 10},
    "employment_status": {"Employed": 70, "Unemployed": 10, "Student": 15, "Retired": 5},
    "device_usage": {"Mobile": 70, "Desktop": 20, "Tablet": 10},
    "social_media_platforms": {"Instagram": 50, "Facebook": 25, "Twitter": 15, "YouTube": 10},
    "content_preferences": {"Videos": 40, "Photos": 30, "Stories": 20, "Live Streams": 10},
    "brand_engagement": {"Nike": 30, "Adidas": 25, "Puma": 20, "Apple": 15, "Samsung": 10},
    "post_frequency": {"Daily": 50, "Weekly": 30, "Monthly": 20},
    "content_themes": {"Motivation": 30, "Lifestyle": 25, "Music": 20, "Fitness": 15, "Travel": 10},
    "sponsored_content": {"High": 40, "Medium": 35, "Low": 25},
    "influencer_collaborations": {"High": 45, "Medium": 35, "Low": 20},
    "user_sentiment": {"Positive": 70, "Neutral": 20, "Negative": 10},
    "engagement_trends": {"Increasing": 60, "Stable": 30, "Decreasing": 10},
    "content_virality": {"High": 50, "Medium": 30, "Low": 20},
    "audience_location": {"Urban": 70, "Suburban": 20, "Rural": 10},
    "audience_age_range": {"13-17": 10, "18-24": 40, "25-34": 30, "35-44": 15, "45-54": 5},
    "content_format_preferences": {"Short Videos": 45, "Long Videos": 30, "Images": 25},
    "influencer_marketing_interest": {"High": 50, "Medium": 30, "Low": 20},
    "social_causes_support": {"Environmental": 25, "Social Justice": 30, "Health": 20, "Education": 15, "Other": 10},
    "subscriptions": {"Monthly": 50, "Yearly": 30, "Lifetime": 20}
}

# Function to create a PDF report
def create_pdf_report(data):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    # Add Company Logo
    logo_path = "sck.png"  # Replace with the actual logo path
    p.drawImage(logo_path, 30, 750, width=100, height=50)
    
    p.setFont("Helvetica-Bold", 16)
    p.drawString(150, 750, "Rick Ross Instagram Report")
    p.setFont("Helvetica", 12)
    p.drawString(150, 735, "-----------------------------")
    
    # Report content
    y_position = 720
    for metric, value in data.items():
        if y_position < 150:
            p.showPage()
            p.setFont("Helvetica", 12)
            y_position = 750

        p.setFont("Helvetica-Bold", 12)
        p.drawString(30, y_position, f"{metric.replace('_', ' ').capitalize()}:")
        p.setFont("Helvetica", 10)
        if isinstance(value, dict):
            for sub_metric, sub_value in value.items():
                y_position -= 15
                p.drawString(40, y_position, f"{sub_metric}: {sub_value}")
        else:
            y_position -= 15
            p.drawString(40, y_position, str(value))
        y_position -= 30
    
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

# Streamlit app layout
st.title("Digital Metrics Report")

st.sidebar.title("Metrics Dashboard")
if st.sidebar.button("Download Full Report"):
    pdf_buffer = create_pdf_report(data)
    st.sidebar.download_button(
        label="Download Report",
        data=pdf_buffer,
        file_name="Digital_Metrics_Report.pdf",
        mime="application/pdf",
    )

# Display all metrics data on the main page
st.header("All Metrics Data")
for metric, value in data.items():
    st.subheader(metric.replace('_', ' ').capitalize())
    if isinstance(value, dict):
        metric_df = pd.DataFrame.from_dict(value, orient='index', columns=['Value'])
        st.table(metric_df)
        fig, ax = plt.subplots()
        sns.barplot(x=metric_df.index, y='Value', data=metric_df, palette="Blues_d", ax=ax)
        ax.set_title(f"{metric.replace('_', ' ').capitalize()} Distribution")
        plt.xticks(rotation=90)
        st.pyplot(fig)
    else:
        st.text(f"{metric.replace('_', ' ').capitalize()}: {value}")
