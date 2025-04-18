# Create bucket (replace UNIQUE-BUCKET-NAME with your chosen name)
aws s3 mb s3://UNIQUE-BUCKET-NAME

# Enable static website hosting
aws s3 website s3://UNIQUE-BUCKET-NAME --index-document index.html --error-document error.html

# Upload files
aws s3 cp index.html s3://UNIQUE-BUCKET-NAME/
aws s3 cp game.js s3://UNIQUE-BUCKET-NAME/
aws s3 cp error.html s3://UNIQUE-BUCKET-NAME/
