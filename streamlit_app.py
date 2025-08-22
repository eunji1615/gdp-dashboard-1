# streamlit 라이브러리를 불러옵니다.
import streamlit as st

# --- 앱 구조 설계 ---

# 1. 페이지 설정 및 제목
# 페이지 설정을 맨 처음에 한 번만 호출해야 합니다.
st.set_page_config(page_title="보이즈플래닛 2 매칭 테스트", layout="centered")
st.title("💖 나와 딱 맞는 '보이즈플래닛 2' 참가자는?")
st.markdown("---")

# 2. 참가자 데이터 정의 (13명으로 확장 및 이미지 URL 추가)
# 참가자들의 이미지 URL은 예시이며, 실제 이미지 주소로 변경하시면 더 좋습니다.
participants = {
    "이상원": {
        "description": "맑고 청아한 음색이 매력적인 참가자. 차분하고 다정한 성격으로 팬들의 마음을 편안하게 만들어 줍니다.",
        "image": "https://i.namu.wiki/i/cXelTBlx1gGcOjdFlCEvRYYbo6sA0jwjQKc4gJAG1kX3WqSYlI4A4fQbdEK1EgiVjey2vXf3ygV9wzKscgN69A.webp",
        "traits": {"position": "보컬", "concept": "감성&청순", "charm": "감성적인 아티스트"}
    },
    "조우안신": {
        "description": "독보적인 분위기와 신비로운 눈빛을 가진 참가자. 무대 위에서 자신만의 세계로 관객을 끌어들입니다.",
        "image": "https://pbs.twimg.com/media/GvouVyoWEAA2blx.jpg:large",
        "traits": {"position": "댄스", "concept": "신비&몽환", "charm": "감성적인 아티스트"}
    },
    "김준서": {
        "description": "시크한 비주얼과 대비되는 따뜻한 마음씨의 소유자. 랩과 댄스 등 다방면에서 준수한 실력을 보여주는 올라운더입니다.",
        "image": "https://talkimg.imbc.com/TVianUpload/tvian/TViews/image/2021/08/17/NdGR35BRwvdp637648037878368039.jpg",
        "traits": {"position": "올라운더", "concept": "시크&세련", "charm": "활기찬 반전 매력"}
    },
    "정상현": {
        "description": "힙합하는 개냥이, 랩 톤이 매력적인 실력파 래퍼. 카리스마 넘치는 무대 매너로 시선을 사로잡습니다.",
        "image": "https://pbs.twimg.com/media/GtAlb_zbIAAGdkE.jpg",
        "traits": {"position": "랩", "concept": "파워풀&카리스마", "charm": "카리스마 무대 장인"}
    },
    "최립우": {
        "description": "개성 있는 톤과 자신감 넘치는 래핑이 돋보이는 래퍼. 자신만의 스타일로 독보적인 존재감을 드러냅니다.",
        "image": "https://i.namu.wiki/i/XjGv_Q3cRi_ugIEGQiU4wePlfI2pBmAly5RI1m-1du1O6vKFMwOFjuNTyff0z4B2CMczT3bMMlCaNR58PgRe6A.webp",
        "traits": {"position": "랩", "concept": "힙합&유니크", "charm": "카리스마 무대 장인"}
    },
    "마사토": {
        "description": "보기만 해도 기분이 좋아지는 밝은 에너지를 가진 참가자. 귀여운 외모와 감미로운 보컬 실력을 갖췄습니다.",
        "image": "https://i.namu.wiki/i/ZC02QlKAJNVn4UxICGac5WqQTZHid5KV-w8tpBRm2aPSkXQffkgIjycd_aisAjRGep6k0lcxzxKlSCsCrbyJPQDIswJRIDJ41ce2vk3QAnBat9UXtuLCtge7femC0f6rpS8q1grPn4r8ZsbYsP_zeg.webp",
        "traits": {"position": "보컬", "concept": "큐트&활발", "charm": "활기찬 반전 매력"}
    },
    "유메키": {
        "description": "세계적인 안무가들과 협업한 경력의 천재 댄서. 창의적인 안무와 뛰어난 실력으로 무대를 예술로 만듭니다.",
        "image": "https://i.namu.wiki/i/q8VNS1vyENa6LkDoP3XhyamkvL_FmAiVE99O-v2e4tUzjKEVk0mKPTWyhaFEhcK0ZYt6Y9KWD6UGhyjI5jlJLA.webp",
        "traits": {"position": "댄스", "concept": "힙합&유니크", "charm": "카리스마 무대 장인"}
    },
    "전이정": {
        "description": "감미로운 미성과 안정적인 라이브 실력을 겸비한 보컬. 듣는 사람의 마음을 울리는 호소력이 짙습니다.",
        "image": "https://i.namu.wiki/i/18cTdSMRqIHoXmfJuczT7mVQgW5sRZEack7czNtIfpiadEg9Tggapk6Ap5S25qdsIFqCIRSB9QhV_bnLigXz3A.webp",
        "traits": {"position": "보컬", "concept": "감성&청순", "charm": "활기찬 반전 매력"}
    },
    "리즈하오": {
        "description": "모델 같은 피지컬과 화려한 비주얼이 돋보이는 올라운더. 비주얼 뿐만 아니라 실력까지 갖춘 노력파입니다.",
        "image": "https://pbs.twimg.com/media/GttITgbaQAIR1qP?format=jpg&name=large",
        "traits": {"position": "올라운더", "concept": "시크&세련", "charm": "압도적인 피지컬"}
    },
    "정현준": {
        "description": "다양한 컨셉을 완벽하게 소화하는 만능 재주꾼. 귀여운 외모 뒤에 숨겨진 탄탄한 실력으로 팬들을 놀라게 합니다.",
        "image": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.namu.wiki%2Fi%2FEx8EWgKLRsDnlyu5yQGKxEqo_OX4oAqkh3jmCm7OyIM5wdGZcmtvAUIX_TnoXJQaFrWQHAPf6_fROjOhAfry-Q.webp&type=sc960_832",
        "traits": {"position": "올라운더", "concept": "큐트&활발", "charm": "활기찬 반전 매력"}
    },
    "쑨지아양": {
        "description": "작지만 압도적인 피지컬에서 나오는 파워풀한 춤이 특기. 무대를 꽉 채우는 존재감과 열정이 돋보입니다.",
        "image": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDEyMDNfNTQg%2FMDAxNzMzMTk2MjM4NzQ5.KNgOm5oTesQwLMXAuJjHweGTw59POLY_A0P9s9maKEMg.ULpHf7-T6AbnnVdTYzhcSWFX3z62W5bx1pOOcQMYpU0g.JPEG%2FIMG_9116.JPG&type=sc960_832",
        "traits": {"position": "댄스", "concept": "파워풀&카리스마", "charm": "압도적인 피지컬"}
    },
    "이리오": {
        "description": "파워풀하고 절도 있는 춤으로 무대를 압도하는 댄스 실력자. 무대 위 카리스마와 일상의 엉뚱한 매력이 공존합니다.",
        "image": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.pinimg.com%2F736x%2F5e%2F0a%2Fc0%2F5e0ac0e2dd7435824200202221ffbba8.jpg&type=sc960_832",
        "traits": {"position": "댄스", "concept": "파워풀&카리스마", "charm": "카리스마 무대 장인"}
    },
    "김건우": {
        "description": "훈훈한 비주얼과 감미로운 목소리의 소유자. 안정적인 보컬 실력으로 팀의 중심을 잡아줍니다.",
        "image": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.namu.wiki%2Fi%2FAQCXLPKSfK-Ep5J-C4zsKYnX3Q3FiVNNq1RZ9PtENHVO888Qnm7KRocdw8dW6FkqeilAA7R5UaOlPDUTnARx-g.webp&type=sc960_832",
        "traits": {"position": "보컬", "concept": "감성&청순", "charm": "압도적인 피지컬"}
    }
}

# 3. 진단 문항 리스트 (참가자 특성에 맞춰 선택지 확장)
questions = [
    {
        "q": "내가 가장 중요하게 생각하는 포지션은?",
        "options": ["보컬", "랩", "댄스", "올라운더"],
        "trait": "position"
    },
    {
        "q": "더 끌리는 무대 컨셉은?",
        "options": ["감성&청순", "파워풀&카리스마", "시크&세련", "큐트&활발", "힙합&유니크", "신비&몽환"],
        "trait": "concept"
    },
    {
        "q": "참가자에게서 가장 보고 싶은 매력은?",
        "options": ["감성적인 아티스트", "카리스마 무대 장인", "활기찬 반전 매력", "압도적인 피지컬"],
        "trait": "charm"
    }
]

# 4. 세션 상태 초기화 (수정 없음)
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# 5. 결과 계산 함수 (수정 없음)
def find_best_match(user_answers):
    best_match_name = None
    max_score = -1

    # 모든 참가자를 순회하며 점수 계산
    for name, data in participants.items():
        current_score = 0
        # 사용자의 답변과 참가자의 특징을 비교
        for trait, user_choice in user_answers.items():
            if data["traits"][trait] == user_choice:
                current_score += 1
        
        # 최고 점수 갱신 (동점일 경우 먼저 나온 참가자 선택)
        if current_score > max_score:
            max_score = current_score
            best_match_name = name
            
    return best_match_name

# 6. 사용자 인터페이스(UI) 구성
with st.form("participant_form"):
    st.info("각 질문에 하나씩 답변을 선택하고 결과를 확인하세요!")
    user_answers = {}

    for i, q in enumerate(questions):
        # st.radio를 사용하여 각 질문에 대한 선택지를 만듭니다.
        answer = st.radio(
            label=f"**Q{i+1}. {q['q']}**",
            options=q['options'],
            key=f"q{i}",
            horizontal=True, # 라디오 버튼을 가로로 배치하여 공간을 효율적으로 사용합니다.
        )
        user_answers[q['trait']] = answer

    # '결과 확인하기' 버튼
    submitted = st.form_submit_button("결과 확인하기")

    if submitted:
        st.session_state.submitted = True
        st.session_state.answers = user_answers
        st.rerun()

# 7. 결과 표시 (오류 수정 완료)
if st.session_state.submitted:
    # 올바른 함수 이름인 find_best_match로 호출합니다.
    match_name = find_best_match(st.session_state.answers)
    
    if match_name and match_name in participants:
        match_data = participants[match_name]

        st.markdown("---")
        st.subheader("🎉 당신과 운명의 참가자는 바로...!")
        st.balloons() # 풍선 효과로 결과 발표를 축하합니다.

        # 레이아웃을 컬럼으로 나누어 사진과 설명을 함께 보여줍니다.
        col1, col2 = st.columns([1, 2])

        with col1:
            # st.image로 참가자 사진을 표시합니다.
            st.image(match_data['image'], caption=match_name, use_column_width=True)
        
        with col2:
            st.success(f"### {match_name}")
            st.write(match_data['description'])
            # 참가자의 주요 특징을 추가로 보여줍니다.
            st.markdown(f"**- 포지션:** {match_data['traits']['position']}")
            st.markdown(f"**- 컨셉:** {match_data['traits']['concept']}")
            st.markdown(f"**- 매력:** {match_data['traits']['charm']}")
        
        st.markdown("---")
        # 다시 하기 버튼
        if st.button("처음부터 다시 하기"):
            st.session_state.submitted = False
            st.session_state.answers = {}
            st.rerun()
    else:
        st.error("결과를 찾을 수 없습니다. 다시 시도해 주세요.")