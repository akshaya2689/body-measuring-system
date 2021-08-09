def poseestimation(imagepath):


    import cv2

    # protoFile = "coco/openpose_pose_coco.prototxt.txt"
    # weightsFile = "coco/pose_iter_440000.caffemodel"
    protoFile = "openpose_pose_mpi_faster_4_stages.prototxt.txt"
    weightsFile = "pose_iter_160000.caffemodel"

    # Read the network into Memory
    net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)




    frame = cv2.imread(imagepath)

    h, w, c = frame.shape
    # Specify the input image dimensions
    inWidth = 368
    inHeight = 368
    # Prepare the frame to be fed to the network
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)

    # Set the prepared object as the input blob of the network
    net.setInput(inpBlob)

    out=net.forward()
    H = out.shape[2]
    W = out.shape[3]

    # Empty list to store the detected keypoints
    #
    points = []

    #
    for i in range(16):
        # confidence map of corresponding body's part.
        probMap = out[0, i, :, :]
        # print(probMap)
    #
    # # Find global maxima of the probMap.
    #
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
    #
    # Scale the point to fit on the original image
        x = (w * point[0]) / W
        y = (h * point[1]) / H

        if prob > 0.6:
            cv2.circle(frame, (int(x), int(y)), 15, (0, 255, 255), thickness=-1)

            cv2.putText(frame, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 2,
                    lineType=cv2.LINE_AA)

            points.append((i,int(x), int(y)))
    #
        else:

            cv2.circle(frame, (int(x), int(y)), 15, (0, 255, 255), thickness=-1)

            cv2.putText(frame, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 2,
                        lineType=cv2.LINE_AA)

            points.append((i, int(x), int(y)))
            pass

            # points.append(None)
    # cv2.imshow("Output-Keypoints", frame)
    # #
    cv2.waitKey(0)
    # #
    cv2.destroyAllWindows()

    cv2.imwrite("as_coco.jpg",frame)

    return points,w,h