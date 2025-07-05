# 🚀 AWS Python S3 Automation

This small Python project demonstrates how to automate AWS S3 using Python and Boto3.

✅ **Features:**
- Uploads local files (like `hello.py`) directly to an S3 bucket
- Uses secure IAM user credentials (never root!) via `aws configure`
- Runs inside a virtual environment (`venv`) for clean dependency management

---

## ☁️ How to run it
```bash
# (If not done yet)
python3 -m venv venv
source venv/bin/activate
pip install boto3

# Then run the uploader
python upload_to_s3.py
