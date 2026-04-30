# 🚀 Static Website Deployment using GitHub & AWS Amplify

![AWS](https://img.shields.io/badge/AWS-Amplify-orange?logo=amazonaws\&logoColor=white)
![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)
![CI/CD](https://img.shields.io/badge/CI/CD-Automated-blue?logo=githubactions)
![HTML](https://img.shields.io/badge/HTML-5-orange?logo=html5)
![CSS](https://img.shields.io/badge/CSS-3-blue?logo=css3)
![JavaScript](https://img.shields.io/badge/JS-JavaScript-yellow?logo=javascript)

---

## 📌 Project Overview

This project demonstrates how to deploy a **static multi-page website** using **GitHub** and **AWS Amplify**.

The website consists of multiple pages such as Home, About, Blog, Projects, and Contact, along with organized assets like CSS, JavaScript, images, and fonts.

---

## 📁 Project Structure

```id="k2m4re"
project-root/
│
├── Code/
│   ├── index.html
│   ├── about.html
│   ├── blog.html
│   ├── contact.html
│   ├── projects.html
│   ├── singlepost.html
│   ├── proj1.html
│   │
│   ├── css/
│   ├── js/
│   ├── images/
│   ├── fonts/
│   ├── upload/
│   ├── source-for-web-designers/
│
├── Docs/
│   └── Amplify-Deployment.docx
│
├── amplify.yml
└── README.md
```

---

## ⚙️ Technologies Used

* HTML5
* CSS3
* JavaScript
* Git & GitHub
* AWS Amplify

---

## 🚀 Deployment Workflow

### 1️⃣ Push Code to GitHub

```id="2q4fya"
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

---

### 2️⃣ Deploy using AWS Amplify

1. Open AWS Console
2. Navigate to Amplify
3. Click **New App → Host Web App**
4. Connect GitHub repository
5. Select repository & branch (`main`)
6. Choose **No Framework (Static Site)**
7. Deploy

---

## ⚙️ Amplify Configuration

Create `amplify.yml` in root:

```id="4y6gch"
version: 1
frontend:
  phases:
    build:
      commands:
        - echo "Static site - no build required"
  artifacts:
    baseDirectory: Code
    files:
      - '**/*'
  cache:
    paths: []
```

---

## 🌍 Live Website

After deployment, your site will be available at:

```id="2u8lmz"
https://main.xxxxxx.amplifyapp.com
```

---

## 📄 Documentation

Detailed setup guide:

* 📄 `Docs/Amplify-Deployment.docx`

---

## ⚠️ Important Notes

* Ensure all pages have `.html` extension
* `index.html` must be present inside `Code/`
* Use relative paths for assets (css/, js/, images/)
* Do not use absolute file paths (C:/...)
* Select **Static Site / No Framework** in Amplify

---

## 🎯 Key Features

* Multi-page static website
* Clean and organized folder structure
* CI/CD deployment using AWS Amplify
* Fast and scalable hosting
* Easy integration with GitHub

---

## 📈 Future Improvements

* Add responsive UI enhancements
* Integrate backend (Node.js / APIs)
* Add authentication system
* Optimize performance and SEO

---

## 👨‍💻 Author

**Rohith**

---
