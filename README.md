# Smart Phishing Detection Dashboard

A web-based dashboard to detect phishing URLs using Python and Flask.

## Features

- HTTPS Detection
- IP Address Detection
- URL Shortener Detection
- URL Length Analysis
- Suspicious Keyword Detection
- Login Form Detection
- Domain Age Analysis (WHOIS)
- Risk Score Calculation
- Interactive Dashboard UI

## Technologies Used

- Python
- Flask
- Requests
- BeautifulSoup4
- Python-WHOIS
- HTML
- CSS

## How It Works

The system analyzes a URL using multiple phishing indicators and calculates a risk score based on detected suspicious patterns.

### Risk Indicators

- Non-HTTPS URLs
- IP Address Usage Instead of Domain Names
- URL Shortening Services
- Suspicious Keywords
- Long URLs
- Login Forms
- Newly Registered Domains

## 📸 Screenshots

**Medium Risk Detection**
![Medium Risk]<img width="1311" height="778" alt="Screenshot 1" src="https://github.com/user-attachments/assets/d2f2279d-a947-44dd-aaea-a18b19220692" />

**Low Risk Detection**
![Low Risk]<img width="1362" height="791" alt="Screenshot 2" src="https://github.com/user-attachments/assets/2d5f4142-c317-4c9b-afc7-5ede40ed78e5" />


## How to Run
1. Clone the repo
   git clone https://github.com/SurbhiPanwar66/Phishing-Detector.git
2. Install dependencies
   pip install -r requirements.txt
3. Run the app
   python app.py
4. Open browser → http://localhost:5000

## Project Structure

```text
PHISHING-DETECTOR
│
├── app.py
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── assets
│   └── Screenshot 1.png
│   └── Screenshot 2.png
│
└── templates
    └── index.html
```

## Future Improvements

- Machine Learning Based Detection
- URL Reputation Checking
- Blacklist Integration
- PDF Report Generation
- Real-Time Threat Intelligence

