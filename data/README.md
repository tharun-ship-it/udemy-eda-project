# Data Directory

## Dataset Information

**Source**: [Udemy Courses Dataset](https://www.kaggle.com/datasets/andrewmvd/udemy-courses)

### Files

| File | Description | Size |
|------|-------------|------|
| `udemy_courses.csv` | Raw dataset | ~4.5 MB |
| `udemy_courses_cleaned.csv` | Processed dataset | ~4.2 MB |

### Schema

| Column | Type | Description |
|--------|------|-------------|
| `course_id` | int | Unique course identifier |
| `course_title` | str | Course name |
| `url` | str | Course URL |
| `is_paid` | bool | Whether course is paid |
| `price` | float | Course price in USD |
| `num_subscribers` | int | Number of enrolled students |
| `num_reviews` | int | Number of reviews |
| `num_lectures` | int | Number of lectures |
| `level` | str | Difficulty level |
| `content_duration` | float | Total duration in hours |
| `published_timestamp` | datetime | Publication date |
| `subject` | str | Course category |

### Download Instructions

1. Visit the [Kaggle dataset page](https://www.kaggle.com/datasets/andrewmvd/udemy-courses)
2. Download `udemy_courses.csv`
3. Place it in this directory

### Note

The CSV files are excluded from version control via `.gitignore` to keep the repository lightweight.
