# Real-time Social Media Sentiment Analysis and Visualization

This project captures real-time social media data, performs sentiment analysis, and visualizes the trends using various AWS services.

## Project Overview

### Steps:
1. **Data Collection:** Stream data from Twitter API and store in S3.
2. **Data Ingestion:** Use AWS Glue to catalog and process data.
3. **Data Processing:** Use AWS Lambda for sentiment analysis.
4. **Data Storage:** Store processed data in Amazon Redshift.
5. **Sentiment Analysis:** Use Amazon Comprehend.
6. **Data Visualization:** Create dashboards using Amazon QuickSight.
7. **Monitoring and Alerts:** Use Amazon CloudWatch.

## Repository Structure
- `data/`: Raw and transformed data.
- `ingestion/`: Scripts to ingest data from Twitter.
- `etl/`: Glue jobs and ETL scripts.
- `sentiment_analysis/`: Lambda function for sentiment analysis.
- `warehouse/`: Redshift schema and data loading scripts.
- `visualization/`: Setup for QuickSight dashboards.
- `monitoring/`: CloudWatch setup.
- `README.md`: Project documentation.
- `LICENSE`: License information.
- `.gitignore`: Git ignore file.

## Setup and Usage

### Prerequisites
- AWS account with necessary permissions
- AWS CLI configured
- Python and Jupyter installed
- Twitter Developer account and API keys

### Steps
1. **Setup Twitter Streaming**:
   - Configure Twitter API keys in `ingestion/twitter_stream.py`.
   - Run the script to start streaming data to S3.

2. **ETL Process with AWS Glue**:
   - Define Glue crawlers and jobs as per the scripts in `etl/glue_jobs/`.
   - Run Glue jobs to transform data and load into Redshift.

3. **Redshift Setup**:
   - Create Redshift cluster.
   - Run SQL scripts in `warehouse/` to set up schema and load data.

4. **Sentiment Analysis**:
   - Deploy Lambda function using the script in `sentiment_analysis/lambda_function/`.

5. **Data Visualization**:
   - Set up QuickSight dashboards using the instructions in `visualization/quicksight_setup.md`.

6. **Monitoring**:
   - Configure CloudWatch using `monitoring/cloudwatch_setup.json`.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
