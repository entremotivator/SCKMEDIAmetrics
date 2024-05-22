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
    "followers": 19.5,
    "quality_audience": 12.4,
    "followers_growth": 0.39,
    "engagement_rate": 1.36,
    "authentic_engagement": 168.3,
    "most_recent_post": "a day ago",
    "global_rank": 582,
    "country_rank": {"Haiti": 2, "Nigeria": 12},
    "top_countries": {
        "United States": 55.2,
        "Nigeria": 6.0,
        "South Africa": 2.8,
        "Haiti": 2.7,
        "United Kingdom": 2.7,
        "Other": 30.6,
    },
    "age_gender": {"Male": 67.2, "Female": 32.8},
    "ethnicity": {
        "African": 30.4,
        "Caucasian": 46.1,
        "Asian": 21.4,
        "Indian": 2.1,
    },
    "languages": {
        "English": 92.1,
        "French": 1.6,
        "Spanish": 1.6,
        "Portuguese": 1.2,
        "German": 0.6,
        "Other": 3.0,
    },
    "estimated_reach": {"post": (1.3, 3.7), "story": (0.246, 0.737)},
    "estimated_impressions": 2.8,
    "audience_interests": {
        "Entertainment": 92.0,
        "Dance": 84.0,
        "Stand-up Comedy": 84.0,
        "Music": 81.0,
        "Theater": 72.0,
        "Film & Television": 37.0,
        "Fashion": 31.0,
        "Social Issues": 22.0,
        "Beauty": 23.0,
        "Sports": 60.0,
    },
    "household_income": {
        "$0K—5K": 8.9,
        "$5K—10K": 10.1,
        "$10K—25K": 14.7,
        "$25K—50K": 14.8,
        "$50K—75K": 12.9,
        "$75K—100K": 10.2,
        "$100K—150K": 13.0,
        "$150K—200K": 7.1,
        "$200K+": 8.4,
    },
    "education_level": {
        "High School or Less": 25.6,
        "Some College": 32.4,
        "Bachelor's Degree": 27.8,
        "Graduate Degree": 14.2,
    },
    "marital_status": {
        "Single": 48.7,
        "Married": 36.5,
        "Divorced": 9.2,
        "Widowed": 5.6,
    },
    "employment_status": {
        "Employed": 62.3,
        "Unemployed": 12.7,
        "Student": 15.4,
        "Retired": 9.6,
    },
    "device_usage": {
        "Mobile": 78.4,
        "Desktop": 16.2,
        "Tablet": 5.4,
    },
    "social_media_platforms": {
        "Instagram": 100.0,
        "Facebook": 72.6,
        "Twitter": 48.9,
        "TikTok": 36.7,
        "Snapchat": 24.5,
    },
    "content_preferences": {
        "Videos": 85.2,
        "Photos": 72.4,
        "Stories": 61.8,
        "Live Streams": 38.6,
        "Reels": 27.4,
    },
    "brand_engagement": {
        "Likes": 72.8,
        "Comments": 48.6,
        "Shares": 32.4,
        "Saves": 19.2,
    },
    "post_frequency": {
        "Daily": 25.6,
        "2-3 Times a Week": 38.4,
        "Once a Week": 22.8,
        "Less Than Once a Week": 13.2,
    },
    "content_themes": {
        "Lifestyle": 68.4,
        "Comedy": 62.2,
        "Music": 54.8,
        "Fashion": 42.6,
        "Travel": 38.2,
        "Food": 32.8,
        "Fitness": 28.4,
    },
    "sponsored_content": {
        "Interested": 62.8,
        "Not Interested": 37.2,
    },
    "influencer_collaborations": {
        "Interested": 74.6,
        "Not Interested": 25.4,
    },
    "user_sentiment": {
        "Positive": 82.4,
        "Neutral": 14.2,
        "Negative": 3.4,
    },
    "engagement_trends": {
        "Increasing": 48.6,
        "Stable": 32.8,
        "Decreasing": 18.6,
    },
    "content_virality": {
        "High": 22.4,
        "Medium": 54.2,
        "Low": 23.4,
    },
    "audience_location": {
        "Urban": 62.8,
        "Suburban": 24.6,
        "Rural": 12.6,
    },
    "audience_age_range": {
        "18-24": 28.4,
        "25-34": 36.2,
        "35-44": 22.8,
        "45+": 12.6,
    },
    "content_format_preferences": {
        "Short Videos": 72.4,
        "Long Videos": 38.6,
        "Carousel Posts": 48.2,
        "Text Posts": 22.8,
    },
    "influencer_marketing_interest": {
        "Interested": 68.4,
        "Not Interested": 31.6,
    },
    "social_causes_support": {
        "Environmental": 42.8,
        "Social Justice": 36.4,
        "Education": 28.2,
        "Health": 24.6,
    },
}

# Function to create a PDF report
def create_pdf_report(data):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Add Company Logo
    logo_path = "sck.png"  # Replace with the actual logo path
    p.drawImage(logo_path, 30, height - 60, width=100, height=50)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(150, height - 60, "Rick Ross Instagram Report")
    p.setFont("Helvetica", 12)
    p.drawString(150, height - 80, "-----------------------------")

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
    ]

    y_position = height - 100
    for content in report_content:
        if content == "Top Countries:":
            y_position -= 20
            p.setFont("Helvetica-Bold", 12)
            p.drawString(30, y_position, content)
            top_countries = data["top_countries"]
            for country, value in top_countries.items():
                y_position -= 15
                p.setFont("Helvetica", 10)
                p.drawString(50, y_position, f"{country}: {value}%")
        elif content in ["Age & Gender:", "Ethnicity:", "Languages:", "Audience Interests:", "Household Income:", "Education Level:", "Marital Status:", "Employment Status:", "Device Usage:", "Social Media Platforms:", "Content Preferences:", "Brand Engagement:", "Post Frequency:", "Content Themes:", "Sponsored Content:", "Influencer Collaborations:", "User Sentiment:", "Engagement Trends:", "Content Virality:", "Audience Location:", "Audience Age Range:", "Content Format Preferences:", "Influencer Marketing Interest:", "Social Causes Support:"]:
            y_position -= 20
            p.setFont("Helvetica-Bold", 12)
            p.drawString(30, y_position, content)
            key = content.strip(":").lower().replace(" ", "_")
            values = data[key]
            for sub_key, sub_value in values.items():
                y_position -= 15
                p.setFont("Helvetica", 10)
                p.drawString(50, y_position, f"{sub_key}: {sub_value}%")
        elif content == "Estimated Reach:":
            y_position -= 20
            p.setFont("Helvetica-Bold", 12)
            p.drawString(30, y_position, content)
            reach_values = data["estimated_reach"]
            for reach_key, reach_value in reach_values.items():
                y_position -= 15
                p.setFont("Helvetica", 10)
                p.drawString(50, y_position, f"{reach_key.capitalize()} Reach: {reach_value[0]}M - {reach_value[1]}M")
        else:
            y_position -= 20
            p.setFont("Helvetica", 12)
            if content == "Estimated Impressions:":
                p.drawString(30, y_position, content + f" {data['estimated_impressions']}M")
            else:
                p.drawString(30, y_position, content.format(data["followers"], data["quality_audience"], data["followers_growth"], data["engagement_rate"], data["authentic_engagement"], data["most_recent_post"], data["global_rank"]))

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

# Function to create a seaborn chart
def create_seaborn_chart(data, title, color_palette):
    plt.figure(figsize=(10, 6))
    keys = list(data.keys())
    values = list(data.values())
    sns.barplot(x=values, y=keys, palette=color_palette)
    plt.title(title)
    plt.xlabel('Percentage')
    plt.ylabel('Category')
    plt.tight_layout()

    # Save the plot to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    return buffer

# Streamlit Interface
st.title("Instagram Data Analysis & PDF Report")

st.write("### Rick Ross Instagram Report")

# Display Charts
color_palettes = {
    "top_countries": "viridis",
    "age_gender": "coolwarm",
    "ethnicity": "magma",
    "languages": "inferno",
    "audience_interests": "cubehelix",
    "household_income": "plasma",
}

for key in color_palettes.keys():
    st.write(f"#### {key.replace('_', ' ').title()}")
    chart_buffer = create_seaborn_chart(data[key], key.replace('_', ' ').title(), color_palettes[key])
    st.image(chart_buffer)

# Generate and Download PDF Report
st.write("### Generate PDF Report")
if st.button("Download PDF Report"):
    pdf_buffer = create_pdf_report(data)
    st.download_button(label="Download PDF", data=pdf_buffer, file_name="rick_ross_instagram_report.pdf", mime="application/pdf")
