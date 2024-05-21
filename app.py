import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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
}

# Function to create a PDF report
def create_pdf_report(data):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    p.drawString(30, 750, "Rick Ross Instagram Report")
    p.drawString(30, 735, "-----------------------------")
    
    p.drawString(30, 720, f"Total Followers: {data['followers']}M")
    p.drawString(30, 705, f"Quality Audience: {data['quality_audience']}M")
    p.drawString(30, 690, f"Followers Growth: {data['followers_growth']}%")
    p.drawString(30, 675, f"Engagement Rate: {data['engagement_rate']}%")
    p.drawString(30, 660, f"Authentic Engagement per Post: {data['authentic_engagement']}K")
    p.drawString(30, 645, f"Most Recent Post: {data['most_recent_post']}")
    
    p.drawString(30, 630, f"Global Rank: {data['global_rank']}")
    for country, rank in data['country_rank'].items():
        p.drawString(30, 615, f"Country Rank in {country}: {rank}")
    
    p.showPage()
    
    # Top Countries
    p.drawString(30, 750, "Top Countries:")
    top_countries = data["top_countries"]
    y = 735
    for country, value in top_countries.items():
        p.drawString(30, y, f"{country}: {value}%")
        y -= 15
    
    p.showPage()
    
    # Age & Gender
    p.drawString(30, 750, "Age & Gender:")
    age_gender = data["age_gender"]
    p.drawString(30, 735, f"Male: {age_gender['Male']}%")
    p.drawString(30, 720, f"Female: {age_gender['Female']}%")
    
    p.showPage()
    
    # Ethnicity
    p.drawString(30, 750, "Ethnicity:")
    ethnicity = data["ethnicity"]
    y = 735
    for key, value in ethnicity.items():
        p.drawString(30, y, f"{key}: {value}%")
        y -= 15
    
    p.showPage()
    
    # Languages
    p.drawString(30, 750, "Languages:")
    languages = data["languages"]
    y = 735
    for key, value in languages.items():
        p.drawString(30, y, f"{key}: {value}%")
        y -= 15
    
    p.showPage()
    
    # Audience Interests
    p.drawString(30, 750, "Audience Interests:")
    audience_interests = data["audience_interests"]
    y = 735
    for key, value in audience_interests.items():
        p.drawString(30, y, f"{key}: {value}%")
        y -= 15
    
    p.showPage()
    
    # Household Income
    p.drawString(30, 750, "Household Income:")
    household_income = data["household_income"]
    y = 735
    for key, value in household_income.items():
        p.drawString(30, y, f"{key}: {value}%")
        y -= 15
    
    p.showPage()
    
    p.save()
    buffer.seek(0)
    return buffer

# Streamlit App
st.title("Rick Ross Instagram Report")

# Followers Section
st.header("Followers")
st.metric("Total Followers (M)", data["followers"])

# Quality Audience Section
st.header("Quality Audience")
st.metric("Quality Audience (M)", data["quality_audience"])

# Followers Growth Section
st.header("Followers Growth")
st.metric("Followers Growth (%)", data["followers_growth"])

# Engagement Rate Section
st.header("Engagement Rate")
st.metric("Engagement Rate (%)", data["engagement_rate"])

# Authentic Engagement Section
st.header("Authentic Engagement")
st.metric("Authentic Engagement per Post (K)", data["authentic_engagement"])

# Most Recent Post Section
st.header("Most Recent Post")
st.text(f"{data['most_recent_post']}")

# Global and Country Rank Section
st.header("Global and Country Rank")
st.metric("Global Rank", data["global_rank"])
for country, rank in data["country_rank"].items():
    st.metric(f"Country Rank in {country}", rank)

# Top Countries Section
st.header("Top Countries")
country_names = list(data["top_countries"].keys())
country_values = list(data["top_countries"].values())
fig, ax = plt.subplots()
ax.pie(country_values, labels=country_names, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Age & Gender Section
st.header("Age & Gender")
age_gender_df = pd.DataFrame(data["age_gender"], index=[0])
st.bar_chart(age_gender_df)

# Ethnicity Section
st.header("Ethnicity")
ethnicity_df = pd.DataFrame(data["ethnicity"], index=[0])
st.bar_chart(ethnicity_df)

# Languages Section
st.header("Languages")
languages_df = pd.DataFrame(data["languages"], index=[0])
st.bar_chart(languages_df)

# Estimated Reach Section
st.header("Estimated Reach")
st.metric("Post Reach (M)", f"{data['estimated_reach']['post'][0]} - {data['estimated_reach']['post'][1]}")
st.metric("Story Reach (K)", f"{data['estimated_reach']['story'][0]} - {data['estimated_reach']['story'][1]}")

# Estimated Impressions Section
st.header("Estimated Impressions")
st.metric("Estimated Impressions (M)", data["estimated_impressions"])

# Audience Interests Section
st.header("Audience Interests")
interests_df = pd.DataFrame(data["audience_interests"], index=[0])
st.bar_chart(interests_df)

# Household Income Section
st.header("Household Income")
income_df = pd.DataFrame(data["household_income"], index=[0])
st.bar_chart(income_df)

# Add button to generate PDF report
if st.button("Export Report as PDF"):
    pdf_buffer = create_pdf_report(data)
    st.download_button(
        label="Download PDF Report",
        data=pdf_buffer,
        file_name="Rick_Ross_Instagram_Report.pdf",
        mime="application/pdf"
    )

# Running the Streamlit App
if __name__ == "__main__":
    st.run()
