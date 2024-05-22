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
    report_content = [
        "Total Followers: {0}M",
        "Quality Audience: {1}M",
        "Followers Growth: {2}%",
        "Engagement Rate: {3}%",
        "Authentic Engagement per Post: {4}K",
        "Most Recent Post: {5}",
        "Global Rank: {6}",
        "Top Countries:",
        "Age & Gender:",
        "Ethnicity:",
        "Languages:",
        "Audience Interests:",
        "Household Income:",
        "Estimated Reach:",
        "Estimated Impressions:",
        "Education Level:",
        "Marital Status:",
        "Employment Status:",
        "Device Usage:",
        "Social Media Platforms:",
        "Content Preferences:",
        "Brand Engagement:",
        "Post Frequency:",
        "Content Themes:",
        "Sponsored Content:",
        "Influencer Collaborations:",
        "User Sentiment:",
        "Engagement Trends:",
        "Content Virality:",
        "Audience Location:",
        "Audience Age Range:",
        "Content Format Preferences:",
        "Influencer Marketing Interest:",
        "Social Causes Support:",
        "Subscriptions:",
    ]

    y_position = 720
    for content in report_content:
        if content == "Top Countries:":
            y_position -= 15
            p.setFont("Helvetica-Bold", 12)
            p.drawString(150, y_position, content)
            top_countries = data["top_countries"]
            for country, value in top_countries.items():
                y_position -= 15
                p.setFont("Helvetica", 10)
                p.drawString(150, y_position, f"{country}: {value}%")
        elif content in ["Age & Gender:", "Ethnicity:", "Languages:", "Audience Interests:", "Household Income:", "Education Level:", "Marital Status:", "Employment Status:", "Device Usage:", "Social Media Platforms:", "Content Preferences:", "Brand Engagement:", "Post Frequency:", "Content Themes:", "Sponsored Content:", "Influencer Collaborations:", "User Sentiment:", "Engagement Trends:", "Content Virality:", "Audience Location:", "Audience Age Range:", "Content Format Preferences:", "Influencer Marketing Interest:", "Social Causes Support:", "Subscriptions:"]:
            y_position -= 15
            p.setFont("Helvetica-Bold", 12)
            p.drawString(150, y_position, content)
            metrics_data = data[content.split(':')[0].lower().replace(' ', '_')]
            df = pd.DataFrame.from_dict(metrics_data, orient='index', columns=['Percentage'])
            fig, ax = plt.subplots(figsize=(6, 4))
            ax = sns.barplot(x=df.index, y='Percentage', data=df, palette="Blues_d")
            ax.set_xlabel(content.split(':')[0], fontsize=10)
            ax.set_ylabel('Percentage', fontsize=10)
            plt.tight_layout()
            plt.savefig("temp_plot.png", format="png", bbox_inches="tight")
            p.drawInlineImage("temp_plot.png", inch, y_position - 15, width=400, height=300)
            y_position -= 315
        elif content == "Estimated Reach:":
            y_position -= 15
            p.setFont("Helvetica-Bold", 12)
            p.drawString(150, y_position, content)
            reach_data = data["estimated_reach"]
            for key, value in reach_data.items():
                y_position -= 15
                p.setFont("Helvetica", 10)
                p.drawString(150, y_position, f"{key.capitalize()} Reach: {value[0]}M - {value[1]}M")
        elif content == "Estimated Impressions:":
            y_position -= 15
            p.setFont("Helvetica-Bold", 12)
            p.drawString(150, y_position, content)
            impressions_data = data["estimated_impressions"]
            p.setFont("Helvetica", 10)
            p.drawString(150, y_position - 15, f"Estimated Impressions: {impressions_data}M")
            y_position -= 30
        else:
            y_position -= 15
            p.setFont("Helvetica", 12)
            p.drawString(150, y_position, content.format(*[data.get(key.lower().replace(" ", "_")) for key in content.split(':')[0].split() if key.lower() != "per"]))

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

# Streamlit app layout
st.title("Digital Metrics Report")

st.sidebar.title("Metrics Dashboard")
selected_metric = st.sidebar.selectbox("Select Metric", list(data.keys()))

# Display selected metric data
st.header(f"{selected_metric.capitalize()} Data")
if isinstance(data[selected_metric], dict):
    metric_df = pd.DataFrame.from_dict(data[selected_metric], orient='index', columns=['Value'])
    st.table(metric_df)
    fig, ax = plt.subplots()
    sns.barplot(x=metric_df.index, y='Value', data=metric_df, palette="Blues_d", ax=ax)
    ax.set_title(f"{selected_metric.capitalize()} Distribution")
    st.pyplot(fig)
else:
    st.text(f"{selected_metric.capitalize()}: {data[selected_metric]}")

# Generate PDF Report Button
if st.button("Generate PDF Report"):
    pdf_buffer = create_pdf_report(data)
    st.download_button(
        label="Download Report",
        data=pdf_buffer,
        file_name="Digital_Metrics_Report.pdf",
        mime="application/pdf",
    )
