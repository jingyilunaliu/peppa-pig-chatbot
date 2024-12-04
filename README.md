# Peppa Pig Interactive Chatbot 

## Overview
An interactive chatbot that mimics Peppa Pig's personality, with voice interactions and playful responses!

## Prerequisites
- Python 3.8+
- OpenAI API Key
- Working microphone

## Setup Instructions
1. Clone the repository
2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Replace `YOUR_OPENAI_API_KEY` in `peppa_chatbot.py` with your actual OpenAI API key

## Running the Chatbot
```bash
python peppa_chatbot.py
```

## Features
- Voice-based interaction
- Peppa Pig personality responses
- Text-to-speech capabilities
- Fun, child-friendly conversation

## Dependencies
- OpenAI for conversational AI
- gTTS for text-to-speech
- SpeechRecognition for voice input
- Pygame for audio playback

## Troubleshooting
- Ensure microphone permissions are granted
- Check internet connection
- Verify API key is valid

## 如何在终端中启动Peppa聊天机器人

### 启动步骤（两步）：

1. 首先在终端中输入以下命令进入项目文件夹：
```bash
cd /Users/liujingyi/CascadeProjects/windsurf-project/peppa_pig_chatbot
```

2. 然后输入以下命令启动最新版本的聊天机器人：
```bash
python3 peppa_chatbot_elevenlabs_v4.py
```

### 使用说明：
- 当看到"Peppa is listening..."时，可以开始说话
- 每次对话后，输入'y'继续聊天，输入'n'结束对话
- 也可以直接说"bye"或"quit"来结束对话

## Note
This is a fun, experimental project and may require additional refinement!
