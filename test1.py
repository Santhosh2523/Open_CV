import cv2
import numpy as np
import json
import neoapi

Manual_ROI = True
while True:
    try:
        image = cv2.imread('D:\Santhosh\Picture1.png')
        if Manual_ROI:
            # Manually draw the ROI
            roi = cv2.selectROI('Draw_ROI_Image', image)
            cv2.destroyAllWindows()
            # Save the ROI data
            with open('roi_data.json', 'w') as f:
                json.dump(roi, f)
                Manual_ROI = False
        else:
            # Load the ROI data
            with open('roi_data.json', 'r') as f:
                roi = json.load(f)

        # Extract the ROI from the image
        x, y, w, h = roi
        roi_image = image[y:y+h, x:x+w]

        # Display the ROI image
        cv2.imshow('ROI Image', roi_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # Create a mask (binary image)
        mask = np.zeros_like(image[:, :, 0], dtype=np.uint8)
        cv2.rectangle(mask, (x, y), (x+w, y+h), (255, 255, 255), -1)  # Draw a white rectangle on the mask

        # Apply the mask to the image using bitwise AND
        masked_image = cv2.bitwise_and(image, image, mask=mask)

        # Display the original image and the masked image
        cv2.imshow('Original Image', image)
        cv2.imshow('Masked Image', masked_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray_masked_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray Masked Image', gray_masked_image)
        cv2.waitKey(0)

        threshold = 50

        ret, binary_image = cv2.threshold( gray_masked_image, threshold, 255, cv2.THRESH_BINARY)

        # Display the original and binary threshold images
        cv2.imshow('Original Image', image)
        cv2.imshow('Binary Threshold Image', binary_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Find contours of contaminated areas
        # Find contours of contaminated areas
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours on the original image
        #contour_image = image.copy()
        #cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

        # Display the original image and the contour image
        #cv2.imshow('Original Image', image)
        #cv2.imshow('Contour Image', contour_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        if not contours:
            result = 100
        else:
            result = 101  
    except (neoapi.NeoException, Exception) as exc:
        print('error in Processing: ', exc)