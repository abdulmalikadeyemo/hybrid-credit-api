# Hybrid Credit API

This Flask API provides a simple endpoint to handle hybrid credit data. It expects a POST request with a JSON body containing 'user' and 'prompt' as string parameters. The API validates the input and responds with a JSON object containing the same parameters if the input is valid.


## **Dockerized Application**
This Flask API has been dockerized and pushed to the Docker Hub repository which can be pulled using:

        docker pull abdulmalikadeyemo/hybrid-credit-api:latest

You can run the application using Docker with the following command:

        docker run -p 5000:5000 -d abdulmalikadeyemo/hybrid-credit-api


After running the above command, the API will be accessible at http://localhost:5000.

## **Running the API Locally**
If you prefer to run the API locally without Docker, make sure you have Python and Flask installed (Check the `requirements.txt` for the version of Flask used). Then, you can run the following commands:

        python app.py

The API will be accessible at http://localhost:5000.


## How to Use

### **Sending a POST Request**
Send a POST request to the following endpoint:

        http://<API_SERVER>/api/hybrid-credit

#### **Request Body:**

        {
            "user": "user_value",
            "prompt": "prompt_value"
        }

- user: A string representing the user data.
- prompt: A string representing the prompt data.
- Replace `user_value` and `prompt_value` with the desired user and prompt values.

#### **Example using curl**

        curl -X POST -H "Content-Type: application/json" -d '{"user":"user_value", "prompt":"prompt_value"}' http://<API_SERVER>/api/hybrid-credit



### **API Response**
- If the request is valid, the API will respond with a JSON object containing the same parameters:

        {
            "user": "user_value",
            "prompt": "prompt_value"
        }







