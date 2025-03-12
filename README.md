# 🚀 FastAPI URL Shortener

A simple and efficient URL shortener API built with **FastAPI** and **Snowflake** as the database. This application provides an easy way to generate short URLs and track usage analytics.

## 📌 Features

✅ Generate short URLs for long URLs  
✅ Retrieve the original URL using a short code  
✅ Track click counts for shortened URLs  
✅ RESTful API built using FastAPI  
✅ Uses **Snowflake** for database storage  
✅ Dockerized for easy deployment  
✅ Deployable on **AWS ECS + Fargate** with **ECR** for container management  

---

## 📁 Folder Structure

FargateProject/ │-- .venv/ # Virtual environment (should not be committed) 
│-- config/
│ ├── config.yaml # Snowflake connection details 
│-- app/ │ ├── main.py # FastAPI application │ 
├── database.py # Database connection with Snowflake │ 
├── models.py # Database models │ ├── crud.py # Functions for database operations │ 
├── streamlit_app.py# Streamlit front-end 
│-- Dockerfile # Docker configuration for deployment 
│-- requirements.txt # Python dependencies 
│-- README.md # Project documentation 
│-- .gitignore # Git ignore file


---

## 🛠️ **Setup & Installation**

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/yourusername/fastapi-url-shortener.git
cd fastapi-url-shortener

2️⃣ Set Up Virtual Environment
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate       # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Snowflake Connection
Modify config/config.yaml to include your Snowflake credentials.

🚀 Running the Application Locally
1️⃣ Start the FastAPI Server
sh
Copy
Edit
uvicorn main:app --reload --host 127.0.0.1 --port 8080
2️⃣ Access API Docs
Open Swagger UI in your browser:
👉 http://127.0.0.1:8080/docs

3️⃣ Use the Streamlit UI
To launch the Streamlit app:

sh

streamlit run streamlit_app.py
📦 Dockerizing the Application
Create a Docker image and run the container:


docker build -t fastapi-url-shortener .
docker run -p 8080:8080 fastapi-url-shortener
🚀 Deploying on AWS ECS with Fargate
We use AWS ECR, ECS, and Fargate for deployment.

1️⃣ Push Docker Image to AWS ECR

aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
docker tag fastapi-url-shortener:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/fastapi-url-shortener
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/fastapi-url-shortener

2️⃣ Deploy to AWS ECS with Fargate
Create an ECS Cluster
Define a Task using the ECR image
Set up a Service and Application Load Balancer
Expose the API via the Load Balancer
🎨 Future Enhancements
🔹 Add user authentication (JWT-based)
🔹 Implement custom short codes
🔹 Introduce an ML-based link categorization model
🔹 Track geolocation & analytics for shortened URLs

🤝 Contributing
Feel free to open an issue or submit a pull request if you find bugs or want to improve the project.

📧 Contact: your.email@example.com

📝 License
This project is licensed under the MIT License.

✅ Now, you're ready to build, test, and deploy your URL shortener! 🚀🎉

markdown


### **📌 Explanation of Key Sections:**
- **Introduction & Features** → Summarizes the project goals  
- **Folder Structure** → Helps users navigate the codebase  
- **Setup Instructions** → Guides users on installing dependencies  
- **Running the App** → Covers FastAPI & Streamlit execution  
- **Dockerization** → Explains how to build & run the container  
- **AWS Deployment** → Provides AWS ECS + Fargate steps  
- **Future Enhancements** → Suggests potential improvements  

✅ **This README follows best practices, is well-structured, and helps any developer quickly understand and use your project!** 🎯 Let me know if you want any modifications.
