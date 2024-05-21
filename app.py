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
    # ... (Same as your provided data)
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
    
    y_position = 720
    for key, value in data.items():
        if isinstance(value, dict):
            y_position -= 15
            p.setFont("Helvetica-Bold", 12)
            p.drawString(30, y_position, f"{key.replace('_', ' ').capitalize()}:")
            for sub_key, sub_value in value.items():
                y_position -= 15
                p.setFont("Helvetica", 10)
                p.drawString(50, y_position, f"{sub_key}: {sub_value}")
        elif isinstance(value, list) and key == 'estimated_reach':
            y_position -= 15
            p.setFont("Helvetica-Bold", 12)
            p.drawString(30, y_position, f"{key.replace('_', ' ').capitalize()}:")
            for reach_type, (low, high) in value.items():
                y_position -= 15
                p.setFont("Helvetica", 10)
                p.drawString(50, y_position, f"{reach_type.capitalize()}: {low}M - {high}M")
        else:
            y_position -= 15
            p.setFont("Helvetica", 10)
            p.drawString(30, y_position, f"{key.replace('_', ' ').capitalize()}: {value}")

        if y_position < 100:
            p.showPage()
            y_position = 750

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

# Streamlit App
st.set_page_config(page_title="Digital Metrics Report", page_icon="sck.png", layout="wide", initial_sidebar_state="expanded")

# Add logo to sidebar
st.sidebar.image("sck.png", use_column_width=True)

st.title("Digital Metrics Report for Investors")

# Display sections

# Sections
sections = {
    "Followers": "followers",
    "Quality Audience": "quality_audience",
    "Followers Growth": "followers_growth",
    "Engagement Rate": "engagement_rate",
    "Authentic Engagement": "authentic_engagement",
    "Most Recent Post": "most_recent_post",
    "Global and Country Rank": "global_rank",
    "Top Countries": "top_countries",
    "Age & Gender": "age_gender",
    "Ethnicity": "ethnicity",
    "Languages": "languages",
    "Estimated Reach": "estimated_reach",
    "Estimated Impressions": "estimated_impressions",
    "Audience Interests": "audience_interests",
    "Household Income": "household_income",
    "Education Level": "education_level",
    "Marital Status": "marital_status",
    "Employment Status": "employment_status",
    "Device Usage": "device_usage",
    "Social Media Platforms": "social_media_platforms",
    "Content Preferences": "content_preferences",
    "Brand Engagement": "brand_engagement",
    "Post Frequency": "post_frequency",
    "Content Themes": "content_themes",
    "Sponsored Content": "sponsored_content",
    "Influencer Collaborations": "influencer_collaborations",
    "User Sentiment": "user_sentiment",
    "Engagement Trends": "engagement_trends",
    "Content Virality": "content_virality",
    "Audience Location": "audience_location",
    "Audience Age Range": "audience_age_range",
    "Content Format Preferences": "content_format_preferences",
    "Influencer Marketing Interest": "influencer_marketing_interest",
    "Social Causes Support": "social_causes_support",
}

# Display sections
for section, data_key in sections.items():
    st.header(section)
    if section == "Top Countries":
        df = pd.DataFrame.from_dict(data[data_key], orient='index', columns=['Percentage'])
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(x=df.index, y='Percentage', data=df, palette="Greens_d", ax=ax)
        ax.set_xlabel('Country', fontsize=12)
        ax.set_ylabel('Percentage', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    elif section in ["Age & Gender", "Ethnicity", "Languages", "Audience Interests", "Household Income", "Education Level", "Marital Status", "Employment Status", "Device Usage", "Social Media Platforms", "Content Preferences", "Brand Engagement", "Post Frequency", "Content Themes", "Sponsored Content", "Influencer Collaborations", "User Sentiment", "Engagement Trends", "Content Virality", "Audience Location", "Audience Age Range", "Content Format Preferences", "Influencer Marketing Interest", "Social Causes Support"]:
        df = pd.DataFrame.from_dict(data[data_key], orient='index', columns=['Percentage'])
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(x=df.index, y='Percentage', data=df, palette="Blues_d", ax=ax)
        ax.set_xlabel(section, fontsize=12)
        ax.set_ylabel('Percentage', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    elif section == "Estimated Reach":
        reach_data = data[data_key]
        reach_df = pd.DataFrame(reach_data).T
        reach_df.columns = ['Min Reach (M)', 'Max Reach (M)']
        fig, ax = plt.subplots(figsize=(8, 6))
        reach_df.plot(kind='bar', ax=ax)
        ax.set_xlabel('Reach Type', fontsize=12)
        ax.set_ylabel('Reach (M)', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    elif section == "Estimated Impressions":
        st.metric("Estimated Impressions", f"{data[data_key]}M")
    else:
        if isinstance(data[data_key], dict):
            for key, value in data[data_key].items():
                st.metric(key, value)
        else:
            st.metric(section, data[data_key])

# Generate PDF report
if st.button("Export Report as PDF"):
    pdf_buffer = create_pdf_report(data)
    st.download_button(
        label="Download PDF Report",
        data=pdf_buffer,
        file_name="Digital_Metrics_Report.pdf",
        mime="application/pdf"
    )

# Running the Streamlit App
if __name__ == "__main__":
    st.run()
