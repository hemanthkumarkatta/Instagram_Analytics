import pandas as pd
import random
from datetime import datetime, timedelta

categories = [
    "Entertainment",
    "Traveling & Tourism",
    "Food",
    "Gaming",
    "Educational",
    "Personal Branding",
    "Trend-Based",
    "Sports & Games",
    "Fashion & Style",
    "Beauty & Makeup",
    "Fitness & Health",
    "Technology & Gadgets",
    "Motivational & Quotes",
    "News & Current Affairs",
    "Photography & Art",
    "Finance & Business",
    "Spirituality & Devotion",
    "Emotional",
    "Daily Vlogs",
    "Exposing/Bold Content",
    "Cinematic/Film Edits",
    "Others"
]


# Instagram Click-Through-Rate (CTR)
ctr = {
    "likes": {
        "Entertainment": (0.06, 0.16),
        "Traveling & Tourism": (0.05, 0.14),
        "Food": (0.04, 0.12),
        "Gaming": (0.04, 0.12),
        "Educational": (0.03, 0.12),
        "Personal Branding": (0.03, 0.10),
        "Trend-Based": (0.06, 0.16),
        "Sports & Games": (0.04, 0.14),
        "Fashion & Style": (0.04, 0.12),
        "Beauty & Makeup": (0.04, 0.12),
        "Fitness & Health": (0.03, 0.10),
        "Technology & Gadgets": (0.04, 0.12),
        "Motivational & Quotes": (0.06, 0.14),
        "News & Current Affairs": (0.05, 0.12),
        "Photography & Art": (0.04, 0.10),
        "Finance & Business": (0.03, 0.10),
        "Spirituality & Devotion": (0.05, 0.14),
        "Emotional": (0.05, 0.16),
        "Daily Vlogs": (0.04, 0.10),
        "Exposing/Bold Content": (0.06, 0.16),
        "Cinematic/Film Edits": (0.05, 0.16),
        "Others": (0.02, 0.10)
    },
    "comments": {
        "Entertainment": (0.004, 0.02),
        "Traveling & Tourism": (0.003, 0.015),
        "Food": (0.002, 0.018),
        "Gaming": (0.002, 0.012),
        "Educational": (0.003, 0.03),
        "Personal Branding": (0.003, 0.01),
        "Trend-Based": (0.007, 0.015),
        "Sports & Games": (0.004, 0.02),
        "Fashion & Style": (0.004, 0.025),
        "Beauty & Makeup": (0.004, 0.03),
        "Fitness & Health": (0.003, 0.028),
        "Technology & Gadgets": (0.003, 0.015),
        "Motivational & Quotes": (0.004, 0.02),
        "News & Current Affairs": (0.003, 0.02),
        "Photography & Art": (0.003, 0.022),
        "Finance & Business": (0.002, 0.015),
        "Spirituality & Devotion": (0.003, 0.02),
        "Emotional": (0.004, 0.03),
        "Daily Vlogs": (0.002, 0.018),
        "Exposing/Bold Content": (0.004, 0.032),
        "Cinematic/Film Edits": (0.004, 0.024),
        "Others": (0.002, 0.03)
    },
    "saves": {
        "Entertainment": (0.003, 0.015),
        "Traveling & Tourism": (0.002, 0.02),
        "Food": (0.003, 0.025),
        "Gaming": (0.001, 0.01),
        "Educational": (0.003, 0.03),
        "Personal Branding": (0.002, 0.02),
        "Trend-Based": (0.001, 0.012),
        "Sports & Games": (0.002, 0.015),
        "Fashion & Style": (0.003, 0.03),
        "Beauty & Makeup": (0.004, 0.035),
        "Fitness & Health": (0.003, 0.032),
        "Technology & Gadgets": (0.002, 0.018),
        "Motivational & Quotes": (0.003, 0.025),
        "News & Current Affairs": (0.003, 0.02),
        "Photography & Art": (0.003, 0.028),
        "Finance & Business": (0.002, 0.02),
        "Spirituality & Devotion": (0.003, 0.025),
        "Emotional": (0.004, 0.02),
        "Daily Vlogs": (0.002, 0.02),
        "Exposing/Bold Content": (0.004, 0.028),
        "Cinematic/Film Edits": (0.004, 0.026),
        "Others": (0.002, 0.02)
    },
    "shares": {
        "Entertainment": (0.03, 0.08),
        "Traveling & Tourism": (0.02, 0.07),
        "Food": (0.02, 0.06),
        "Gaming": (0.02, 0.06),
        "Educational": (0.02, 0.04),
        "Personal Branding": (0.02, 0.04),
        "Trend-Based": (0.04, 0.10),
        "Sports & Games": (0.02, 0.05),
        "Fashion & Style": (0.02, 0.05),
        "Beauty & Makeup": (0.02, 0.05),
        "Fitness & Health": (0.02, 0.05),
        "Technology & Gadgets": (0.02, 0.05),
        "Motivational & Quotes": (0.03, 0.07),
        "News & Current Affairs": (0.02, 0.05),
        "Photography & Art": (0.02, 0.05),
        "Finance & Business": (0.02, 0.04),
        "Spirituality & Devotion": (0.02, 0.05),
        "Emotional": (0.04, 0.08),
        "Daily Vlogs": (0.02, 0.05),
        "Exposing/Bold Content": (0.03, 0.08),
        "Cinematic/Film Edits": (0.03, 0.08),
        "Others": (0.02, 0.08)
    }
}

# Instagram Peak Hours
category_peak_hours_by_day = {
    "Monday": {
        "Entertainment": [12, 13, 14, 19, 20, 21, 22],
        "Traveling & Tourism": [13, 14, 20, 21],
        "Food": [12, 13, 14, 17, 18, 19, 20, 21],
        "Gaming": [19, 20, 21, 22],
        "Educational": [8, 9, 10, 11, 18, 19, 20],
        "Personal Branding": [7, 8, 9, 12, 13, 18, 19, 20],
        "Trend-Based": [10, 11, 12, 13, 19, 20, 21, 22],
        "Sports & Games": [6, 7, 8, 13, 14, 19, 20, 21],
        "Fashion & Style": [12, 13, 14, 18, 19, 20],
        "Beauty & Makeup": [11, 12, 13, 17, 18, 19],
        "Fitness & Health": [6, 7, 8, 18, 19],
        "Technology & Gadgets": [9, 10, 12, 18, 20],
        "Motivational & Quotes": [6, 7, 20, 21, 22],
        "News & Current Affairs": [7, 8, 9, 13, 18, 19],
        "Photography & Art": [10, 11, 12, 19, 20],
        "Finance & Business": [7, 8, 9, 12, 18],
        "Spirituality & Devotion": [5, 6, 7, 8, 20, 21],
        "Emotional": [18, 19, 20, 21, 22],
        "Daily Vlogs": [12, 13, 14, 19, 20],
        "Exposing/Bold Content": [20, 21, 22, 23],
        "Cinematic/Film Edits": [14, 15, 19, 20, 21, 22, 23],
        "Others": [12, 13, 14, 18, 19]
    },
    "Tuesday": {
        "Entertainment": [12, 13, 14, 19, 20, 21, 22],
        "Traveling & Tourism": [13, 14, 15, 18, 19, 20, 21],
        "Food": [11, 12, 13, 14, 18, 19],
        "Gaming": [17, 18, 19, 20, 21, 22],
        "Educational": [7, 8, 9, 11, 12, 18, 19, 20],
        "Personal Branding": [8, 9, 10, 12, 18],
        "Trend-Based": [10, 11, 12, 13, 19, 20, 21, 22],
        "Sports & Games": [6, 7, 13, 14, 15, 19, 20, 21],
        "Fashion & Style": [11, 12, 13, 18, 19, 20],
        "Beauty & Makeup": [11, 12, 18, 19, 20],
        "Fitness & Health": [6, 7, 8, 18, 19],
        "Technology & Gadgets": [9, 10, 11, 18, 19, 20],
        "Motivational & Quotes": [6, 7, 8, 21, 22],
        "News & Current Affairs": [7, 8, 12, 18, 19, 20],
        "Photography & Art": [11, 12, 13, 19, 20],
        "Finance & Business": [7, 8, 9, 12, 18,],
        "Spirituality & Devotion": [5, 6, 7, 8, 21, 22],
        "Emotional": [18, 19, 20, 21, 22],
        "Daily Vlogs": [12, 13, 14, 19, 20],
        "Exposing/Bold Content": [13, 14, 20, 21, 22, 23],
        "Cinematic/Film Edits": [14, 15, 19, 20, 21, 22, 23],
        "Others": [13, 14, 18, 19]
    },
    "Wednesday": {
        "Entertainment": [12, 13, 14, 18, 19, 20, 21, 22],
        "Traveling & Tourism": [13, 14, 15, 18, 19, 20],
        "Food": [11, 12, 13, 14, 17, 18, 19],
        "Gaming": [18, 19, 20, 21, 22],
        "Educational": [7, 8, 9, 10, 12, 18],
        "Personal Branding": [8, 9, 10, 12, 18, 19],
        "Trend-Based": [10, 11, 12, 13, 19, 20, 21, 22, 23],
        "Sports & Games": [6, 7, 13, 14, 15, 18, 19, 20, 21],
        "Fashion & Style": [12, 13, 14, 18, 19, 20],
        "Beauty & Makeup": [11, 12, 13, 18, 19, 20],
        "Fitness & Health": [6, 7, 8, 18, 19],
        "Technology & Gadgets": [10, 11, 12, 18, 19],
        "Motivational & Quotes": [6, 7, 8, 22, 23],
        "News & Current Affairs": [7, 8, 9, 12, 17, 18, 19],
        "Photography & Art": [11, 12, 13, 18, 19, 20],
        "Finance & Business": [7, 8, 9, 12, 17, 18, 19],
        "Spirituality & Devotion": [5, 6, 7, 8, 22, 23],
        "Emotional": [10, 11, 18, 19, 20, 21, 22],
        "Daily Vlogs": [12, 13, 14, 17, 18, 20],
        "Exposing/Bold Content": [14, 15, 19, 20, 21, 22],
        "Cinematic/Film Edits": [14, 15, 20, 21, 22, 23],
        "Others": [13, 14, 15, 18, 19]
    },
    "Thursday": {
        "Entertainment": [12, 13, 14, 18, 19, 20, 21, 22],
        "Traveling & Tourism": [13, 14, 15, 19, 20, 21, 22],
        "Food": [11, 12, 13, 14, 18, 19, 20],
        "Gaming": [18, 19, 20, 21, 22],
        "Educational": [7, 8, 9, 12, 13, 18],
        "Personal Branding": [8, 9, 10, 12, 18],
        "Trend-Based": [11, 12, 13, 14, 19, 20, 21, 22],
        "Sports & Games": [6, 7, 13, 14, 15, 19, 20, 21],
        "Fashion & Style": [12, 13, 18, 19, 20],
        "Beauty & Makeup": [11, 12, 13, 17, 18, 19, 20],
        "Fitness & Health": [6, 7, 8, 18, 19],
        "Technology & Gadgets": [9, 10, 12, 19],
        "Motivational & Quotes": [6, 7, 8, 11, 12, 21, 22],
        "News & Current Affairs": [7, 8, 9, 12, 18, 19],
        "Photography & Art": [11, 12, 13, 19, 20, 21],
        "Finance & Business": [7, 8, 9, 12, 13],
        "Spirituality & Devotion": [5, 6, 7, 8, 22],
        "Emotional": [18, 19, 20, 21, 22],
        "Daily Vlogs": [12, 13, 14, 19, 20, 21],
        "Exposing/Bold Content": [13, 14, 19, 20, 22, 23],
        "Cinematic/Film Edits": [15, 16, 19, 20, 21, 22, 23],
        "Others": [13, 14, 15, 19]
    },
    "Friday": {
        "Entertainment": [13, 14, 15, 19, 20, 21, 22, 23],
        "Traveling & Tourism": [14, 15, 16, 19, 20, 21, 22],
        "Food": [12, 13, 14, 19, 20, 21],
        "Gaming": [18, 19, 20, 21, 22, 23],
        "Educational": [7, 8, 9, 10, 12],
        "Personal Branding": [8, 9, 10, 12, 18],
        "Trend-Based": [11, 12, 13, 14, 19, 20, 21, 22],
        "Sports & Games": [6, 7, 13, 14, 15, 19, 20, 21, 22],
        "Fashion & Style": [13, 14, 19, 20, 21],
        "Beauty & Makeup": [12, 13, 14, 18, 19],
        "Fitness & Health": [6, 7, 8, 18, 20, 21],
        "Technology & Gadgets": [10, 12, 18, 20],
        "Motivational & Quotes": [6, 7, 8, 12, 20, 21, 22],
        "News & Current Affairs": [7, 8, 12, 18],
        "Photography & Art": [11, 12, 13, 20, 21],
        "Finance & Business": [7, 8, 9, 12],
        "Spirituality & Devotion": [5, 6, 7, 8, 20, 21, 22],
        "Emotional": [9, 10, 14, 15, 18, 19, 20, 21],
        "Daily Vlogs": [12, 13, 14, 20, 21],
        "Exposing/Bold Content": [14, 15, 19, 20, 21, 22],
        "Cinematic/Film Edits": [15, 16, 20, 21, 22],
        "Others": [14, 15, 16, 19, 20]
    },
    "Saturday": {
        "Entertainment": [9, 10, 11, 12, 13, 15, 16, 19, 20, 21, 22],
        "Traveling & Tourism": [9, 10, 11, 12, 13, 14, 16, 17, 20, 21],
        "Food": [9, 10, 11, 12, 13, 14, 19, 20, 21],
        "Gaming": [9, 10, 11, 14, 15, 16, 18, 19, 20, 21, 22],
        "Educational": [9, 10, 11, 16, 17],
        "Personal Branding": [10, 11, 12, 17, 18],
        "Trend-Based": [11, 12, 13, 15, 16, 20, 21, 22],
        "Sports & Games": [8, 9, 10, 11, 19, 20, 21, 22],
        "Fashion & Style": [11, 12, 13, 16, 19, 20, 21],
        "Beauty & Makeup": [11, 12, 13, 17, 18, 19],
        "Fitness & Health": [7, 8, 9, 18, 19, 20],
        "Technology & Gadgets": [11, 12, 13, 19, 20],
        "Motivational & Quotes": [7, 8, 9, 12, 21, 22, 23],
        "News & Current Affairs": [8, 9, 10, 13, 18],
        "Photography & Art": [10, 11, 12, 19, 20, 21],
        "Finance & Business": [9, 10, 11, 12],
        "Spirituality & Devotion": [6, 7, 8, 9, 20, 21, 22, 23],
        "Daily Vlogs": [12, 13, 14, 20, 21, 22],
        "Emotional": [14, 15, 18, 19, 20, 21, 22],
        "Exposing/Bold Content": [14, 15, 19, 20, 21, 22],
        "Cinematic/Film Edits": [9, 10, 11, 12, 15, 16, 20, 21, 22],
        "Others": [13, 14, 15, 19, 20, 21]
    },
    "Sunday": {
        "Entertainment": [8, 9, 10, 11, 12, 13, 16, 19, 20, 21],
        "Traveling & Tourism": [9, 10, 11, 12, 13, 16, 17, 20, 21],
        "Food": [9, 10, 11, 12, 13, 14, 19, 20, 21],
        "Gaming": [11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22],
        "Educational": [9, 10, 11, 16],
        "Personal Branding": [10, 11, 12, 16, 17],
        "Trend-Based": [10, 11, 12, 13, 15, 16, 20, 21, 22],
        "Sports & Games": [8, 9, 10, 11, 12, 19, 20, 21, 22],
        "Fashion & Style": [11, 12, 13, 16, 19, 20, 21],
        "Beauty & Makeup": [11, 12, 13, 17, 18, 19],
        "Fitness & Health": [7, 8, 9, 18, 19],
        "Technology & Gadgets": [11, 12, 13, 19, 20],
        "Motivational & Quotes": [7, 8, 9, 12, 20, 21, 22],
        "News & Current Affairs": [8, 9, 10, 13, 18],
        "Photography & Art": [10, 11, 12, 20, 21],
        "Finance & Business": [9, 10, 11, 12],
        "Spirituality & Devotion": [6, 7, 8, 9, 20, 21],
        "Emotional": [10, 11, 13, 14, 18, 19, 20, 21],
        "Daily Vlogs": [12, 13, 14, 18, 19, 20, 21],
        "Exposing/Bold Content": [9, 10, 11, 14, 15, 19, 20, 21],
        "Cinematic/Film Edits": [9, 10, 11, 15, 16, 18, 19, 20, 21],
        "Others": [13, 14, 15, 19, 20, 21]
    }
}

# Instagram category reach parameters by day
category_day_params = {
    "Monday": {
        "Educational": (80, 10),
        "Personal Branding": (70, 10),
        "Trend-Based": (90, 30),
        "Entertainment": (70, 10),
        "Gaming": (65, 10),
        "Traveling & Tourism": (65, 10),
        "Food": (65, 10),
        "Sports & Games": (75, 10),
        "Fashion & Style": (65, 10),
        "Beauty & Makeup": (65, 10),
        "Fitness & Health": (65, 10),
        "Technology & Gadgets": (70, 8),
        "Motivational & Quotes": (75, 10),
        "News & Current Affairs": (80, 12),
        "Photography & Art": (65, 10),
        "Finance & Business": (60, 9),
        "Spirituality & Devotion": (70, 10),
        "Emotional": (75, 10),
        "Daily Vlogs": (65, 10),
        "Exposing/Bold Content": (95, 15),
        "Cinematic/Film Edits": (85, 12),
        "Others": (70, 30)
    },
    "Tuesday": {
        "Educational": (85, 10),
        "Personal Branding": (80, 10),
        "Trend-Based": (90, 30),
        "Entertainment": (75, 10),
        "Gaming": (60, 10),
        "Traveling & Tourism": (60, 10),
        "Food": (70, 5),
        "Sports & Games": (75, 8),
        "Fashion & Style": (65, 10),
        "Beauty & Makeup": (68, 10),
        "Fitness & Health": (70, 10),
        "Technology & Gadgets": (70, 10),
        "Motivational & Quotes": (80, 10),
        "News & Current Affairs": (80, 12),
        "Photography & Art": (70, 10),
        "Finance & Business": (65, 9),
        "Spirituality & Devotion": (72, 10),
        "Emotional": (75, 10),
        "Daily Vlogs": (65, 10),
        "Exposing/Bold Content": (98, 15),
        "Cinematic/Film Edits": (88, 12),
        "Others": (75, 25)
    },
    "Wednesday": {
        "Educational": (75, 10),
        "Personal Branding": (70, 10),
        "Trend-Based": (100, 20),
        "Entertainment": (80, 5),
        "Gaming": (60, 10),
        "Traveling & Tourism": (60, 5),
        "Food": (75, 10),
        "Sports & Games": (75, 10),
        "Fashion & Style": (68, 10),
        "Beauty & Makeup": (70, 10),
        "Fitness & Health": (78, 10),
        "Technology & Gadgets": (70, 9),
        "Motivational & Quotes": (85, 10),
        "News & Current Affairs": (88, 12),
        "Photography & Art": (72, 10),
        "Finance & Business": (68, 9),
        "Spirituality & Devotion": (75, 10),
        "Emotional": (80, 10),
        "Daily Vlogs": (70, 8),
        "Exposing/Bold Content": (100, 15),
        "Cinematic/Film Edits": (90, 12),
        "Others": (80, 30)
    },
    "Thursday": {
        "Educational": (80, 10),
        "Personal Branding": (80, 10),
        "Trend-Based": (100, 20),
        "Entertainment": (75, 5),
        "Gaming": (60, 10),
        "Traveling & Tourism": (60, 10),
        "Food": (70, 5),
        "Sports & Games": (80, 5),
        "Fashion & Style": (66, 10),
        "Beauty & Makeup": (68, 10),
        "Fitness & Health": (76, 10),
        "Technology & Gadgets": (70, 9),
        "Motivational & Quotes": (80, 10),
        "News & Current Affairs": (86, 12),
        "Photography & Art": (70, 10),
        "Finance & Business": (66, 9),
        "Spirituality & Devotion": (73, 10),
        "Emotional": (78, 10),
        "Daily Vlogs": (70, 8),
        "Exposing/Bold Content": (100, 15),
        "Cinematic/Film Edits": (90, 12),
        "Others": (80, 30)
    },
    "Friday": {
        "Educational": (60, 10),
        "Personal Branding": (60, 10),
        "Trend-Based": (100, 30),
        "Entertainment": (90, 10),
        "Gaming": (85, 10),
        "Traveling & Tourism": (85, 10),
        "Food": (80, 10),
        "Sports & Games": (80, 10),
        "Fashion & Style": (75, 12),
        "Beauty & Makeup": (78, 12),
        "Fitness & Health": (85, 12),
        "Technology & Gadgets": (68, 10),
        "Motivational & Quotes": (88, 10),
        "News & Current Affairs": (95, 14),
        "Photography & Art": (80, 12),
        "Finance & Business": (78, 10),
        "Spirituality & Devotion": (78, 12),
        "Emotional": (85, 10),
        "Daily Vlogs": (75, 9),
        "Exposing/Bold Content": (110, 18),
        "Cinematic/Film Edits": (100, 14),
        "Others": (80, 25)
    },
    "Saturday": {
        "Educational": (60, 10),
        "Personal Branding": (55, 5),
        "Trend-Based": (110, 30),
        "Entertainment": (110, 20),
        "Gaming": (105, 10),
        "Traveling & Tourism": (95, 10),
        "Food": (95, 10),
        "Sports & Games": (95, 10),
        "Fashion & Style": (90, 15),
        "Beauty & Makeup": (90, 15),
        "Fitness & Health": (90, 10),
        "Technology & Gadgets": (80, 12),
        "Motivational & Quotes": (95, 12),
        "News & Current Affairs": (105, 15),
        "Photography & Art": (90, 14),
        "Finance & Business": (85, 12),
        "Spirituality & Devotion": (90, 12),
        "Emotional": (110, 12),
        "Daily Vlogs": (80, 10),
        "Exposing/Bold Content": (130, 20),
        "Cinematic/Film Edits": (120, 16),
        "Others": (90, 25)
    },
    "Sunday": {
        "Educational": (60, 10),
        "Personal Branding": (55, 10),
        "Trend-Based": (120, 30),
        "Entertainment": (110, 20),
        "Gaming": (110, 10),
        "Traveling & Tourism": (105, 10),
        "Food": (110, 10),
        "Sports & Games": (105, 10),
        "Fashion & Style": (90, 15),
        "Beauty & Makeup": (90, 15),
        "Fitness & Health": (90, 10),
        "Technology & Gadgets": (85, 12),
        "Motivational & Quotes": (100, 12),
        "News & Current Affairs": (110, 15),
        "Photography & Art": (100, 14),
        "Finance & Business": (88, 12),
        "Spirituality & Devotion": (80, 12),
        "Emotional": (120, 12),
        "Daily Vlogs": (85, 10),
        "Exposing/Bold Content": (135, 20),
        "Cinematic/Film Edits": (125, 16),
        "Others": (100, 30)
    }
}



user_ids=[]
for i in range(24):
  user_number = i+1
  user_id = "user_"+str(user_number).zfill(2)
  user_ids.append(user_id)

data = []
start_date = datetime(2025, 6, 23)
for day_offset in range(7):
  date = start_date + timedelta(days=day_offset)
  day_name = date.strftime('%A')

  for hour, user_id in enumerate(user_ids):
    post_time = datetime(date.year, date.month, date.day, hour)

    for category in categories:
      for hashtag_type in ["Generic_Hashtags", "Niche_Hashtags", "Trending_Hashtags", "Spammy_Hashtags", "without_hastags"]:
        mu, sigma = category_day_params[day_name][category]
        base_reach = round(random.normalvariate(mu, sigma), 1)

        if hashtag_type == "Generic_Hashtags":
          category_multiplier = round(random.normalvariate(1.15, 0.05), 3)
          if hour in category_peak_hours_by_day.get(day_name, {}).get(category, []):
            time_factor = random.uniform(1.1, 1.15)
          elif 1 < hour < 6:
            time_factor = random.uniform(0.6, 1)
          else:
            time_factor = 1.0
          base_reach_extension = round(base_reach * category_multiplier * time_factor, 1)
          random_values = random.random()
          if random_values < 0.05:
            base_reach_extension *= random.uniform(3,10)
          else:
            base_reach_extension *= 1
          final_reach = round(base_reach_extension, 1)

        elif hashtag_type == "Niche_Hashtags":
          category_multiplier = round(random.normalvariate(1.2, 0.05), 3)
          if hour in category_peak_hours_by_day.get(day_name, {}).get(category, []):
            time_factor = random.uniform(1.1, 1.25)
          elif 1 < hour < 6:
            time_factor = random.uniform(0.6, 1)
          else:
            time_factor = 1.0
          base_reach_extension = round(base_reach * category_multiplier * time_factor, 1)
          random_values = random.random()
          if random_values < 0.05:
            base_reach_extension *= random.uniform(3,10)
          else:
            base_reach_extension *= 1
          final_reach = round(base_reach_extension, 1)

        elif hashtag_type == "Trending_Hashtags":
          multiplier = random.normalvariate(1.8, 0.7)
          category_multiplier = round(max(multiplier, 1.2), 3)
          if hour in category_peak_hours_by_day.get(day_name, {}).get(category, []):
            time_factor = random.uniform(1.1, 1.35)
          elif 1 < hour < 6:
            time_factor = random.uniform(0.6, 1)
          else:
            time_factor = 1.0
          base_reach_extension = round(base_reach * category_multiplier * time_factor, 1)
          random_values = random.random()
          if random_values < 0.05:
            base_reach_extension *= random.uniform(3,10)
          else:
            base_reach_extension *= 1
          final_reach = round(base_reach_extension, 1)

        elif hashtag_type == "Spammy_Hashtags":
          multiplier = random.normalvariate(0.8, 0.1)
          category_multiplier = round(max(multiplier, 0.7), 3)
          if hour in category_peak_hours_by_day.get(day_name, {}).get(category, []):
            time_factor = random.uniform(0.9, 1.1)
          elif 1 < hour < 6:
            time_factor = random.uniform(0.6, 1)
          else:
            time_factor = 1.0
          base_reach_extension = round(base_reach * category_multiplier * time_factor, 1)
          random_values = random.random()
          if random_values < 0.05:
            base_reach_extension *= random.uniform(3,10)
          else:
            base_reach_extension *= 1
          final_reach = round(base_reach_extension, 1)

        else:
          if hour in category_peak_hours_by_day.get(day_name, {}).get(category, []):
            time_factor = random.uniform(1.2, 1.35)
          if 1 < hour < 6:
            time_factor = random.uniform(0.6, 1)
          else :
            time_factor = 1.0
          base_reach_extension = round(base_reach * time_factor, 1)
          random_values = random.random()
          if random_values < 0.05:
            base_reach_extension *= random.uniform(3,10)
          else:
            base_reach_extension *= 1
          final_reach = round(base_reach_extension, 1)


        min_likes, max_likes = ctr["likes"][category]
        likes = round(final_reach * random.uniform(min_likes, max_likes), 1)
        min_comments, max_comments = ctr['comments'][category]
        comments = round(final_reach * random.uniform(min_comments, max_comments), 1)
        min_saves, max_saves = ctr["saves"][category]
        saves = round(final_reach * random.uniform(min_saves, max_saves), 1)
        min_shares, max_shares = ctr["shares"][category]
        shares = round(final_reach * random.uniform(min_shares, max_shares), 1)

        data.append({
            "User_id": user_id,
            "Post_time": post_time,
            "Category": category,
            "Hashtag_type": hashtag_type,
            "Reach": final_reach,
            "Likes": likes,
            "Comments": comments,
            "Saves": saves,
            "Shares": shares
            })

df = pd.DataFrame(data)
print(df)