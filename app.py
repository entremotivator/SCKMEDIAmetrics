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
        "Sports": 60.0,  # New metric
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
    
    # Add Company Logo
    logo_path = "company_logo.png"  # Replace with the actual logo path
    p.drawImage(logo_path, 30, 750, width=100, height=50)

    p.drawString(150, 750, "Rick Ross Instagram Report")
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
        "Estimated Impressions:"
    ]
    
    y_position = 720
    for content in report_content:
        if content == "Top Countries:":
            y_position -= 15
            p.drawString(150, y_position, content)
            top_countries = data["top_countries"]
            for country, value in top_countries.items():
                y_position -= 15
                p.drawString(150, y_position, f"{country}: {value}%")
            # Plot pie chart for top countries
            fig, ax = plt.subplots()
            ax.pie(list(top_countries.values()), labels=list(top_countries.keys()), autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)
        elif content in ["Age & Gender:", "Ethnicity:", "Languages:", "Audience Interests:", "Household Income:"]:
            y_position -= 15
            p.drawString(150, y_position, content)
            metrics_data = data[content.split(':')[0].lower().replace(' ', '_')]
            df = pd.DataFrame(metrics_data, index=[0])
            st.bar_chart(df)
        elif content == "Estimated Reach:":
            y_position -= 15
            p.drawString(150, y_position, content)
            reach_data = data["estimated_reach"]
            for key, value in reach_data.items():
                y_position -= 15
                p.drawString(150, y_position, f"{key.capitalize()} Reach: {value[0]}M - {value[1]}M")
        elif content == "Estimated Impressions:":
            y_position -= 15
            p.drawString(150, y_position, content)
            impressions_data = data["estimated_impressions"]
            p.drawString(150, y_position - 15, f"Estimated Impressions: {impressions_data}M")
        else:
            y_position -= 15
            p.drawString(150, y_position, content.format(*[data[key] for key in content.split(':')[1].split()]))
    
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

# Streamlit App
st.title("Digital Metrics Report for Investors")

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
    "Household Income": "household_income"
}

# Display sections
for section, data_key in sections.items():
    st.header(section)
    if section == "Top Countries":
        st.text("Top Countries")
    elif section in ["Age & Gender", "Ethnicity", "Languages", "Audience Interests", "Household Income"]:
        st.bar_chart(pd.DataFrame(data[data_key], index=[0]))
    elif section == "Estimated Reach":
        for key, value in data[data_key].items():
            st.text(f"{key.capitalize()} Reach: {value[0]}M - {value[1]}M")
    elif section == "Estimated Impressions":
        st.text(f"Estimated Impressions: {data[data_key]}M")
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
