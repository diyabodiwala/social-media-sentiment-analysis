CREATE TABLE twitter_sentiment (
    created_at TIMESTAMP,
    text VARCHAR(500),
    user VARCHAR(50),
    sentiment VARCHAR(10),
    sentiment_score FLOAT
);
