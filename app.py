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
    "followers": 1500000.05,
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
    "device_usage": {"Mobile": 78.4, "Desktop": 16.2, "Tablet": 5.4},
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
    "sponsored_content": {"Interested": 62.8, "Not Interested": 37.2},
    "influencer_collaborations": {"Interested": 74.6, "Not Interested": 25.4},
    "user_sentiment": {"Positive": 82.4, "Neutral": 14.2, "Negative": 3.4},
    "engagement_trends": {
        "Increasing": 48.6,
        "Stable": 32.8,
        "Decreasing": 18.6,
    },
    "content_virality": {"High": 22.4, "Medium": 54.2, "Low": 23.4},
    "audience_location": {"Urban": 62.8, "Suburban": 24.6, "Rural": 12.6},
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
    "monthly_subscribers": 22000,
    "ppv_subscriptions": 2.2,
}

def create_pdf_report(data):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Add Company Logo
    logo_path = "sck.png"  # Replace with the actual logo path
    p.drawImage(logo_path, 30, 750, width=100, height=50)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(150, 750, "SCK Media Metrics Report")
    p.setFont("Helvetica", 12)
    p.drawString(150, 735, "-----------------------------")

    # Add Company Description
    p.setFont("Helvetica", 10)
    p.drawString(
        30,
        720,
        "SCK MEDIA TV IS AN INNOVATIVE GLOBAL PAY-PER-VIEW (PPV) PLATFORM DEDICATED TO SOCIAL CONTENT CREATORS,",
    )
    p.drawString(
        30,
        705,
        "ALLOWING CONTENT CREATORS TO MONETIZE THEIR 'eSCKlusive' CONTENT ON THEIR OWN TERMS.",
    )
    p.drawString(30, 690, "DO YOU CREATE CONTENT 'eSCKlusive' ENOUGH FOR PAY-PER-VIEW?")
    p.drawString(
        30,
        675,
        "DO YOU HAVE AN ACTIVE SOCIAL MEDIA FOLLOWING, TRENDING CONTENT OR MONETIZABLE CONCEPTS?",
    )
    p.drawString(
        30,
        660,
        "ARE YOU READY TO BE YOUR OWN SOCIAL CONTENT CHANNEL, OWN YOUR CONTENT & RECEIVE THE LION'S SHARE OF YOUR CONTENT'S ENGAGEMENT, ADVERTISING & RESIDUAL REVENUE?",
    )

    # Report content
    report_content = [
        "Total Followers: {0}M".format(data['followers'] / 1e6),
        "Quality Audience: {0}M".format(data['quality_audience']),
        "Followers Growth: {0}%".format(data['followers_growth']),
        "Engagement Rate: {0}%".format(data['engagement_rate']),
        "Authentic Engagement per Post: {0}K".format(data['authentic_engagement']),
        "Most Recent Post: {0}".format(data['most_recent_post']),
        "Global Rank: {0}".format(data['global_rank']),
        "Monthly Subscribers: {0}K".format(data['monthly_subscribers'] / 1e3),
        "PPV Subscriptions: {0}M".format(data['ppv_subscriptions']),
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

    # Format the report content with the actual data
    formatted_content = [
        report_content[0],
        report_content[1],
        report_content[2],
        report_content[3],
        report_content[4],
        report_content[5],
        report_content[6],
        report_content[7],
        report_content[8],
        report_content[9],
        report_content[10],
        report_content[11],
        report_content[12],
        report_content[13],
        report_content[14],
        report_content[15],
        report_content[16],
        report_content[17],
        report_content[18],
        report_content[19],
        report_content[20],
        report_content[21],
        report_content[22],
        report_content[23],
        report_content[24],
        report_content[25],
        report_content[26],
        report_content[27],
        report_content[28],
        report_content[29],
        report_content[30],
        report_content[31],
        report_content[32],
        report_content[33],
        report_content[34],
        report_content[35],
    ]

    y_position = 640
    for line in formatted_content:
        if line.endswith(":"):
            p.setFont("Helvetica-Bold", 12)
        else:
            p.setFont("Helvetica", 10)
        p.drawString(30, y_position, line)
        y_position -= 15

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

# PDF Report
buffer = create_pdf_report(data)
st.download_button(
    label="Download PDF Report",
    data=buffer,
    file_name="SCK_Media_Metrics_Report.pdf",
    mime="application/pdf"
)
