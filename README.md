# 🤖 LLaMA 챗봇 (Meta LLaMA 3 + Together API)

Together API와 Meta LLaMA 3 모델을 활용한 범용 AI 챗봇입니다.  
사용자가 입력한 질문에 대해 친절하고 유익한 답변을 생성합니다.

---

## ✅ 주요 기능

- Meta-LLaMA-3.1-70B-Instruct-Turbo 모델 사용
- 시스템 역할 메시지 및 API 키를 `.env` 파일로 관리
- 토큰 수 초과 시 오래된 메시지 자동 제거
- 대화 기록은 `message_history.json` 파일에 저장

---

## 📦 설치 방법

1. 레포 클론

```bash
git clone https://github.com/your-username/llama-chatbot.git
cd llama-chatbot
```

2. 패키지 설치

```bash
pip install -r requirements.txt
```

---

## ⚙️ 환경 설정 (.env 파일)

1. `.env.example` 파일을 복사하여 `.env` 파일 생성

```bash
cp .env.example .env
```

2. 아래 정보를 입력

```env
API_KEY=your_together_api_key_here
SYSTEM_MESSAGE=당신은 친절하고 유용한 AI 챗봇입니다. 사용자 질문에 정확하고 간결하게 답변해주세요.
```

---

## ▶️ 실행 방법

```bash
python main.py
```

`exit` 또는 `quit`을 입력하면 종료됩니다.

---

## 📂 GitHub에 포함되지 않는 파일

`.gitignore`에 의해 아래 파일은 업로드되지 않습니다:

- `.env` (API 키 보안)
- `message_history.json` (대화 로그)
- `__pycache__/` (파이썬 캐시)

---

## 💡 확장 아이디어

- 웹 인터페이스 (Gradio, Streamlit 등)
- 다양한 시스템 역할 프리셋
- 대화 요약 및 히스토리 UI 구현

---

## 🧠 라이선스 & 출처

- 모델 제공: [Meta LLaMA 3](https://ai.meta.com/llama/)
- API 플랫폼: [Together API](https://www.together.ai/)

---

## 👤 MADE BY

- **김현민** 