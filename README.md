# 🌐 Glink Project: AI Context Router

> **"Beyond Translation, Towards Connection."**
> 언어는 장벽이 아니라 프로토콜일 뿐입니다. Glink는 전 세계의 파편화된 인터넷 커뮤니티를 '문화적 맥락(Context)'으로 연결합니다.

![Project Status](https://img.shields.io/badge/Status-Prototype-green) ![Python](https://img.shields.io/badge/Language-Python-blue) ![Engine](https://img.shields.io/badge/Engine-OpenAI_GPT-orange)

## 💡 What is Glink?

**Glink**는 단순한 번역기(Translator)가 아닙니다. 발화자의 **'의도(Intent)'**를 추출하여 수신자의 **'문화(Culture)'**로 라우팅하는 **AI Context Router (ACR)**입니다.

기존 번역기가 놓치는 '게임 은어', '밈(Meme)', '팬덤 용어'의 뉘앙스를 완벽하게 현지화하여, 언어 장벽 없는 단일 시장(Single Market)을 구축하는 것을 목표로 합니다.

### 🚫 The Problem: "Uncanny Valley of Translation"
* **Source:** "아 우리 정글 **던지네**."
* **Legacy Translator:** "Ah, our jungle is **throwing**." (의미 불명, 투척 중?)
* **Result:** 소통 단절 및 트래픽 파편화.

### ✅ The Solution: Glink ACR
* **Source:** "아 우리 정글 **던지네**."
* **Glink Engine:** [Intent: Complain] + [Context: LoL] + [Mapping: Throwing -> Inting]
* **Output:** "Our jungler is **inting** hard." (완벽한 게이머 화법)

---

## 🏗️ Core Architecture

### 1. AI Context Router (ACR) Engine
* **Context Awareness:** 게임/팬덤 맥락 자동 감지.
* **Sentiment Shield:** 악의적 비방 및 가스라이팅을 감지하여 차단하거나 정중한 표현으로 강제 순화(Filtering).
* **Slang Mapping:** 자체 구축한 데이터셋(`glink_asset_final.csv`)을 기반으로 한 고정밀 은어 변환.

### 2. Business Ecosystem
* **Glink HUB:** 글로벌 게임 공략/정보 실시간 동기화 (Traffic).
* **Glink CLUB:** 텍스트 기반 소통 멤버십 & Safe Zone (Subscription).
* **Glink TICKET:** AI 활동 분석 기반 암표 방지 및 진성 팬 우선 예매 시스템 (Retention).

---

## 🚀 Getting Started (Prototype)

이 저장소(Repository)에는 Glink의 핵심 기술인 **ACR 엔진의 MVP(Minimum Viable Product)** 코드가 포함되어 있습니다.

### Prerequisites
* Python 3.8+
* OpenAI API Key

### Installation

1. 저장소를 클론(Clone)합니다.
```bash
git clone [https://github.com/YOUR_GITHUB_ID/Glink-Prototype.git](https://github.com/YOUR_GITHUB_ID/Glink-Prototype.git)
cd Glink-Prototype
