# YouTube Intro Generator 🎬

🌟 **Live Demo**: [Preview the App](https://app.bluedothq.com/preview/67ae6e45bc7812dc8d7ee5e8)


[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-%2300C7B7.svg)](https://fastapi.tiangolo.com/)


A lightweight AI-powered solution for generating engaging YouTube intros from video scripts. Built with FastAPI and OpenAI's async API.

## Features ✨
- 🚀 **Async Processing**: Non-blocking OpenAI API calls using `await openai.Completion.acreate`
- 📦 **Modular Design**: Clean separation of concerns with configurable components
- 🔒 **Rate Limiting**: Built-in protection against API abuse
- 📝 **Validation**: Robust input validation with Pydantic models

## Project Structure 📂

### Backend Architecture
```
backend/
├── 📁 api/
│   └── 📄 intro.py           # REST API endpoints
├── 📁 services/
│   └── 📄 openai_service.py  # OpenAI integration layer
├── 📄 config.py              # Environment configuration
├── 📄 models.py              # Pydantic data models
├── 📄 limiter.py             # Rate limiting middleware
└── 📄 main.py                # FastAPI app initialization
```

### Frontend Architecture (React)
```
frontend/
├── 📁 public/
│   ├── 📄 index.html         # Main HTML template
│   └── 📄 favicon.ico        # Application icon
├── 📁 src/
│   ├── 📁 components/        # Reusable UI components
│   │   ├── 📄 ScriptInput.js  # Textarea for script input
│   │   └── 📄 IntroDisplay.js # Result display component
│   ├── 📁 services/          # API communication
│   │   └── 📄 api.js         # Axios API client configuration
│   ├── 📄 App.js             # Root component
│   ├── 📄 index.js           # Application entry point  
├── 📄 package.json           # NPM dependencies
└── 📄 .env                   # Frontend environment variables
```

### Full Stack Features
| Layer       | Technologies                          | Key Features                             |
|-------------|---------------------------------------|------------------------------------------|
| **Frontend**| React, Axios, CSS-in-JS               | Responsive UI, Real-time preview         |
| **Backend** | FastAPI, Python 3.9, AsyncIO          | REST API, Async processing, Rate limiting|
| **AI**      | OpenAI API, Prompt engineering        | GPT-3.5/4 integration, Content generation|
| **DevOps**  | Docker, Uvicorn, Poetry               | Containerization, Dependency management |

### Frontend Setup
To set up the React frontend:
```bash
cd frontend
npm install  # Install dependencies
npm start    # Start development server
```

### Frontend Environment
Create `.env` in frontend directory:
```env
REACT_APP_API_URL=http://localhost:8000
REACT_APP_MAX_INPUT_LENGTH=5000
```

## Quick Start 🚀

### Prerequisites
- Python 3.9+
- OpenAI API key

### Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# venv\Scripts\activate  # Windows
```

```bash
# Install dependencies
pip install -r requirements.txt
```

```bash
# Configure environment variables - create .env file
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_ENGINE=text-davinci-003
OPENAI_MAX_TOKENS=100
OPENAI_TEMPERATURE=0.7
```

### Running the Server ⚡
uvicorn main:app --reload

How It Works 🔄
1. **User Input**  
   Paste video script into frontend interface
2. **API Processing**  
   ```mermaid
   graph LR
   A[POST /api/generate-intro] --> B{Validation}
   B --> C[Construct Prompt]
   C --> D[Async OpenAI Call]
   ```
3. **Response Handling**  
   Returns JSON with generated intro text

## Production Considerations 🏗️
| Aspect              | Recommendation                          |
|---------------------|-----------------------------------------|
| **Architecture**    | Microservices + API Gateway            |
| **Security**        | JWT Authentication + TLS Encryption    |
| **Scalability**     | Kubernetes + Redis Caching             |
| **Observability**   | Prometheus + Grafana Monitoring         |

## Roadmap 🗺️
- [ ] **Caching Layer** (Redis integration)
- [ ] **Enhanced Error Handling**
- [ ] **User Authentication** (JWT/OAuth)
- [ ] **Analytics Dashboard**

## Contributing 🤝
We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License 📄
Distributed under the Apache 2.0 License. See `LICENSE` for more information.

---

> **Note**: This is a demo implementation. For production use, consider implementing additional security measures and error handling.
