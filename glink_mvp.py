import os
import csv
import datetime
from openai import OpenAI

# ==========================================
# [Glink ACR 프로토타입 - V1.2 Path Finder]
# 기능: 윈도우 보안 권한 우회 (무조건 바탕화면에 저장)
# ==========================================

def get_desktop_path():
    """사용자의 바탕화면 절대 경로를 찾아내는 함수"""
    return os.path.join(os.path.expanduser("~"), "Desktop")

# 파일 이름을 바탕화면 경로와 합체시킵니다.
# 예: C:\Users\Seorian\Desktop\glink_asset_final.csv
FILENAME = os.path.join(get_desktop_path(), "glink_asset_final.csv")

def save_to_csv(input_text, output_text):
    """데이터를 CSV 파일에 저장"""
    file_exists = os.path.isfile(FILENAME)
    
    try:
        with open(FILENAME, mode='a', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Timestamp", "Input (KR)", "Output (EN) - Glink"])
            
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([now, input_text, output_text])
            return True # 저장 성공
    except PermissionError:
        return False # 저장 실패 (파일이 열려있음)

def run_glink_acr_v1_2():
    print("--- [Glink ACR V1.2] 절대 경로 모드 ---")
    
    # 저장될 위치를 미리 보여줍니다 (안심 확인용)
    print(f"📂 데이터 저장 위치: {FILENAME}")
    
    # API 키 입력
    api_key = input("OpenAI API 키를 입력하세요: ").strip()
    
    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        print(f"오류: {e}")
        return

# [수정된 시스템 프롬프트]
    system_instruction = """
    You are 'Glink ACR', a translator for Global Gamers.
    
    [CRITICAL INSTRUCTIONS]
    1. ROLE: You are a TRANSLATOR, not a chatbot.
    2. ACTION: Translate the input text from Korean to English.
    3. CONSTRAINT: 
       - If the input is a question (e.g., "Why?"), DO NOT ANSWER IT. Just translate the question itself.
       - NEVER output Korean characters. Output ONLY English.
    
    [GAMING SLANG MAPPING]
    - "구마빠" -> "Guma stans" or "Gumayusi fans"
    - "흐린눈" -> "Turning a blind eye"
    - "렌즈 씌어준 격" -> "Like putting rose-tinted glasses on"
    - "월즈 쓰리핏" -> "Worlds three-peat"
    - "살떨렸던" -> "Nerve-wracking" or "Heart-pounding"
    
    [EXAMPLES]
    Input: "걔네 왜 저럼?"
    Output: "Why are they acting like that?" (Do NOT explain why)
    
    Input: "월즈 우승 누가 할까?"
    Output: "Who's gonna win Worlds?" (Do NOT guess the winner)
    """

    print("\n" + "="*60)
    print("📢 시스템 가동! 이제 에러 없이 바탕화면에 저장됩니다.")
    print("="*60 + "\n")

    while True:
        user_input = input("🇰🇷 입력 (KR): ")
        
        if user_input.lower() in ['exit', 'quit', '종료']:
            print("시스템을 종료합니다.")
            break
            
        if not user_input:
            continue

        print("🔄 분석 중...", end="\r")

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
            )
            
            translated_text = response.choices[0].message.content
            
            print(f"🇺🇸 출력 (EN): {translated_text}")
            
            # 저장 시도
            if save_to_csv(user_input, translated_text):
                print(f"✅ [저장 완료] 바탕화면의 glink_asset_final.csv 파일을 확인하세요.\n")
            else:
                print(f"⚠️ [저장 실패] 엑셀 파일이 켜져 있나요? 파일을 닫고 다시 시도하면 저장됩니다.\n")
            
        except Exception as e:
            print(f"\n❌ 에러: {e}\n")

if __name__ == "__main__":
    run_glink_acr_v1_2()