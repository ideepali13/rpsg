import cv2
import mediapipe as mp
import random
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

TIP_IDS = [4, 8, 12, 16, 20]

def detect_gesture(lm, handedness):
    fingers = []

    if handedness == "Right":
        fingers.append(1 if lm[TIP_IDS[0]].x < lm[TIP_IDS[0] - 1].x else 0)
    else:
        fingers.append(1 if lm[TIP_IDS[0]].x > lm[TIP_IDS[0] - 1].x else 0)

    for i in range(1, 5):
        fingers.append(1 if lm[TIP_IDS[i]].y < lm[TIP_IDS[i] - 2].y else 0)

    total = sum(fingers)

    if total == 0:
        return "rock"
    if total == 5:
        return "paper"
    if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
        return "scissors"
    return None


def decide_winner(user, comp):
    if user == comp:
        return "Tie"
    if (user == "rock" and comp == "scissors") or \
       (user == "paper" and comp == "rock") or \
       (user == "scissors" and comp == "paper"):
        return "You Win"
    return "You Lose"


def draw_box(frame, text, pos, color=(255, 255, 255)):
    cv2.rectangle(frame, (pos[0], pos[1] - 35), (pos[0] + 350, pos[1] + 5), (0, 0, 0), -1)
    cv2.putText(frame, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)


def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.6)

    user_move = "Show Gesture"
    comp_move = "-"
    result = "-"

    user_score = 0
    comp_score = 0

    last_time = 0
    cooldown = 1.3

    print("🤚 Show Rock / Paper / Scissors — Press Q to exit")

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result_mp = hands.process(rgb)

        if result_mp.multi_hand_landmarks:
            for lm_s, handedness_obj in zip(result_mp.multi_hand_landmarks, result_mp.multi_handedness):
                mp_draw.draw_landmarks(frame, lm_s, mp_hands.HAND_CONNECTIONS)

                handedness = handedness_obj.classification[0].label
                gesture = detect_gesture(lm_s.landmark, handedness)

                now = time.time()
                if gesture and now - last_time > cooldown:
                    user_move = gesture
                    comp_move = random.choice(["rock", "paper", "scissors"])
                    result = decide_winner(user_move, comp_move)

                    if result == "You Win":
                        user_score += 1
                    elif result == "You Lose":
                        comp_score += 1

                    last_time = now

        color_result = (0, 255, 0) if result == "You Win" else (0, 0, 255) if result == "You Lose" else (255, 255, 0)

        # ==== UI Overlays ====
        draw_box(frame, f"Your Move: {user_move}", (20, 60))
        draw_box(frame, f"Computer: {comp_move}", (20, 120))
        draw_box(frame, f"Result: {result}", (20, 180), color_result)
        draw_box(frame, f"Score → You: {user_score}  CPU: {comp_score}", (20, 240), (0, 255, 255))

        cv2.imshow("Rock Paper Scissors - Enhanced UI", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
