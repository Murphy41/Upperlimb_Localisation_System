import cv2
import pose

#config
POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]

#start job
poseDecoder = pose.Pose()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 640)
cap.set(10, 150)

while True:
    success, img = cap.read()
    frame = cv2.bilateralFilter(img, 5, 50, 100)
    cmd, draw_skeleton_flag, points = poseDecoder.detect(frame)

    print(cmd)

    if draw_skeleton_flag:
        for i in range(15):
            cv2.circle(frame, points[i], 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frame, "{}".format(i), points[i], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                            lineType=cv2.LINE_AA)

        for pair in POSE_PAIRS:
            partA = pair[0]
            partB = pair[1]
            if points[partA] and points[partB]:
                cv2.line(frame, points[partA], points[partB], (0, 255, 255), 2)
                cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break